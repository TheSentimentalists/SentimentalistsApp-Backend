from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
import json
import get_credibility_score as cr
import sentiment_analysis as sa
import get_bias_score as bs
import spacy_matcher as sm
import validators
import sys
import logging
import traceback

segment = xray_recorder.begin_segment('lambda_handler')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    """
    event must be a dict with a url key, and context can be nothing:
    lambda_handler({"url":"http://bbc.co.uk"}, "")
    """

    subsegment = xray_recorder.begin_subsegment('lambda_function: check URL')
    logger.info(f'LambdaFunction: Checking we have a URL...')
    try:
        url = event['url']
    except KeyError:
        logger.info(f'LambdaFunction: URL is not present.')
        return {"error": "No URL provided"}

    xray_recorder.end_subsegment()

    """
    Adding "https://" to the URL if not present
    """
    logger.info(f'LambdaFunction: Checking URL has protocol...')
    subsegment = xray_recorder.begin_subsegment('lambda_function: '
                                                'check URL protocol')
    if (not url.startswith('https://') and not url.startswith('http://')):
        url = 'https://' + url
    xray_recorder.end_subsegment()

    logger.info(f'LambdaFunction: Validating URL...')
    subsegment = xray_recorder.begin_subsegment('lambda_function: '
                                                'validate URL')
    if (not validators.url(url)):
        logger.info(f'LambdaFunction: URL is not valid.')
        return {"error": "The url was bad"}
    xray_recorder.end_subsegment()

    """
    Define the object skeleton
    """
    object = {
        "url": url,
        "results": []
    }

    """
    CredibilityScore
    """
    logger.info(f'LambdaFunction: Trying to get credibility score...')
    credibility_result = {}
    try:
        credibility_result = cr.get_credibility_score(url)
        object['results'].append(credibility_result)
    except Exception as e:
        logger.info(f'LambdaFunction: Could not get Credibility Score.')
        logger.info(e)
        credibility_result = {'type': 'credibility',
                              'outcome': {"error": 'The credibility score '
                                                   'was not available.'}}
        object['results'].append(credibility_result)

    """
    SentimentAnalisys
    """
    logger.info(f'LambdaFunction: Trying to get sentimentAnalysis score...')
    sentresult = {}
    try:
        sentresult = sa.sentiment_analysis(url)
        if sentresult['text'] == '-1':
            logger.info(f'LambdaFunction: sentimentAnalysis returned -1, '
                        'dumping:')
            logger.info(sentresult)
            object['article'] = {'error':
                                 "The article summary could not be generated"}
            object['results'].append({'type': 'polarity',
                                      "outcome": {"error":
                                                  'The polarity score could '
                                                  'not be calculated.'}})
            object['results'].append({'type': 'objectivity',
                                      "outcome":
                                      {"error": 'The objectivity score could '
                                                'not be calculated.'}})
        else:
            object['article'] = {'header': sentresult['header'],
                                 'summary': sentresult['summary'],
                                 'keywords': sentresult['keywords'],
                                 'image': sentresult['image']}
            object['results'].append({'type': 'polarity',
                                      'outcome':
                                     {"score": sentresult['polarity']}})
            objectivity = abs(1 - sentresult['subjectivity'])
            object['results'].append({'type': 'objectivity',
                                      'outcome': {"score": objectivity}})

    except Exception as e:
        logger.info(f'LambdaFunction: Could not get sentimentAnalysis Score.')
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type,
                                                      exception_value,
                                                      exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)

        sentresult = {'text': -1}
        object['article'] = {'error': 'The article summary could not be '
                                      'generated'}
        object['results'].append({'type': 'polarity',
                                  "outcome": {"error": 'The polarity score '
                                                       'could not be '
                                                       'calculated.'}})
        object['results'].append({'type': 'objectivity',
                                  "outcome": {"error": 'The objectivity score '
                                                       'could not be '
                                                       'calculated.'}})

    """
    BiasScore
    """
    logger.info(f'LambdaFunction: Trying to get bias score...')
    if sentresult['text'] != '-1':
        if 'error' in credibility_result['outcome']:
            cred_input = -1
        else:
            cred_input = credibility_result['outcome']['score']
        try:
            bresult = bs.get_bias_score(cred_input,
                                        sentresult['polarity'],
                                        sentresult['subjectivity'])
            object['results'].append(bresult)
        except Exception as e:
            logger.info(f'LambdaFunction: Could not get Bias Score.')
            logger.info(e)
            object['results'].append({'type': 'bias',
                                      'outcome': {"error":
                                                  'The bias score was not '
                                                  'available.'}})
    else:
        object['results'].append({'type': 'bias',
                                  'outcome': {"error":
                                              'The bias score was not '
                                              'available.'}})

    """
    SpacyMatcher
    """
    logger.info(f'LambdaFunction: Trying to get Spacy Matcher...')
    if sentresult['text'] != '-1':
        try:
            list_objs = sm.spacy_matcher(sentresult['text'])
            object['article']['topics'] = list_objs
        except Exception as e:
            logger.info(f'LambdaFunction: Could not get Topics.')
            logger.info(e)
            object['article']['topics'] = {"error": "No topics available."}

    """
    JSON to return:
        {
        'url':'https://www.theguardian.com/world/2020/',
        'article' : {
            'text' : 'PM admits failings as England's Covid contact ....',
            'header' : 'PM admits failings as England's Covid contact',
            'summary' : Boris Johnson and his chief scientific ...',
            'keywords' : ['Boris Johnson', 'Brexit'],
            'image' : 'http://sentimentalists..../test.png',
            'topics': [{'type': 'DATE', 'topic': 'Today'}]}}
            },
        'results' : [
            { 'type' : 'credibility', 'outcome': {'score': 100.0, 'source ...
            { 'type' : 'polarity',    'outcome': {'score': 0.108126295001 ...
            { 'type' : 'objectivity', 'outcome': {'score': 0.487846736596 ...
            { 'type' : 'bias',        'outcome': {'score': 20.67598528015 ...
            ]
        }
    """

    return object


xray_recorder.end_segment()
