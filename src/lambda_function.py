from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
import json
import getCredibilityScore as cr
import sentimentAnalysis as sa
import getBiasScore as bs
import spacyMatcher as sm
import validators
import sys
import logging
import traceback

segment = xray_recorder.begin_segment('lambda_handler')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):

    ## event must be a dict with a url key, and context can be nothing:
    ## lambda_handler({"url":"http://bbc.co.uk"}, "")

    subsegment = xray_recorder.begin_subsegment('lambda_function: check URL')
    logger.info(f'LambdaFunction: Checking we have a URL...')
    try:
        url = event['url']
    except KeyError:
        logger.info(f'LambdaFunction: URL is not present.')
        return {"error" : "No URL provided"}

    xray_recorder.end_subsegment()

    #### Adding "https://" to the URL if not present
    logger.info(f'LambdaFunction: Checking URL has protocol...')
    subsegment = xray_recorder.begin_subsegment('lambda_function: check URL protocol')
    if (not url.startswith('https://') and not url.startswith('http://')):
        url = 'https://' + url
    xray_recorder.end_subsegment()

    logger.info(f'LambdaFunction: Validating URL...')
    subsegment = xray_recorder.begin_subsegment('lambda_function: validate URL')
    if (not validators.url(url)):
        logger.info(f'LambdaFunction: URL is not valid.')
        return {"error" : "The url was bad"}
    xray_recorder.end_subsegment()

    #### Define the object skeleton
    object = {
        "url" : url,
        "results" : []
    }

    # CredibilityScore
    logger.info(f'LambdaFunction: Trying to get credibility score...')
    credibilityresult = {}
    try:
        credibilityresult = cr.getCredibilityScore(url)
        object['results'].append(credibilityresult)
    except Exception as e:
        logger.info(f'LambdaFunction: Could not get Credibility Score.')
        logger.info(e)
        credibilityresult = {'type': 'credibility', 'outcome': {"error" : "The credibility score was not available."}}
        object['results'].append(credibilityresult)


    # SentimentAnalisys
    logger.info(f'LambdaFunction: Trying to get sentimentAnalysis score...')
    sentanalysisresult = {}
    try:
        sentanalysisresult = sa.sentimentAnalysis(url)
        if sentanalysisresult['text'] == '-1':
            logger.info(f'LambdaFunction: sentimentAnalysis returned -1, dumping:')
            logger.info(sentanalysisresult)
            object['article'] = {'error': "The article summary could not be generated"}
            object['results'].append({'type': 'polarity',     "outcome": {"error" : "The polarity score could not be calculated."}})
            object['results'].append({'type': 'objectivity', "outcome": {"error" : "The objectivity score could not be calculated."}})
        else:
            object['article'] = {'header': sentanalysisresult['header'], 
                                    'summary': sentanalysisresult['summary'],
                                    'keywords': sentanalysisresult['keywords']}
            object['results'].append({'type': 'polarity',     'outcome': {"score": sentanalysisresult['polarity']}})
            object['results'].append({'type': 'objectivity', 'outcome': {"score": abs(1 - sentanalysisresult['subjectivity'])}})
    except Exception as e:
        logger.info(f'LambdaFunction: Could not get sentimentAnalysis Score.')
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)

        sentanalysisresult = {'text': -1}
        object['article'] = {'error': "The article summary could not be generated"}
        object['results'].append({'type': 'polarity',     "outcome": {"error" : "The polarity score could not be calculated."}})
        object['results'].append({'type': 'objectivity', "outcome": {"error" : "The objectivity score could not be calculated."}})


    # BiasScore
    logger.info(f'LambdaFunction: Trying to get bias score...')
    if sentanalysisresult['text'] != '-1': #### if there is no POL or SUBJ, getBiasScore will not be called
        if 'error' in credibilityresult['outcome']:
            cred_input = -1
        else:
            cred_input = credibilityresult['outcome']['score']
        try:
            biasscoreresult = bs.getBiasScore(cred_input, sentanalysisresult['polarity'], sentanalysisresult['subjectivity'])
            object['results'].append(biasscoreresult)
        except Exception as e:
            logger.info(f'LambdaFunction: Could not get Bias Score.')
            logger.info(e)
            object['results'].append({'type': 'bias', 'outcome': {"error" : "The bias score was not available."}})
    else:
        object['results'].append({'type': 'bias', 'outcome': {"error" : "The bias score was not available."}})

    # SpacyMatcher
    logger.info(f'LambdaFunction: Trying to get Spacy Matcher...')
    if sentanalysisresult['text'] != '-1':
        try:
            article_topics = []
            tags = ['PERSON','GPE','ORG','PERCENT','LANGUAGE','DATE','TIME','LOC','NORP','EVENT','WORK_OF_ART',
                    'MONEY','QUANTITY','ORDINAL','CARDINAL']
            for i in tags:
                list_objs = sm.spacyMatcher(sentanalysisresult['text'], i) ### {'Toyota', 'BBC', 'BMW', 'Chanel'}
                for obj in list_objs:
                    article_topics.append({'type' : i, 'topic' : obj})                    
            object['article']['topics'] = article_topics            
        except Exception as e:
            logger.info(f'LambdaFunction: Could not get Topics.')
            logger.info(e)
            object['article']['topics'] = {"error" : "No topics available."}

    #### JSON to return:
    # {
    #   'url':'https://www.theguardian.com/world/2020/',
    #   'article' : {
    #     'header' : 'PM admits failings as England's Covid contact',
    #     'summary' : Boris Johnson and his chief scientific ...',
    #     'keywords' : ['Boris Johnson', 'Brexit'],
    #     'topics': [{'type': 'DATE', 'topic': 'Today'}]}}
    #   },
    #   'results' : [
    #     { 'type' : 'credibility', 'outcome': {'score': 100.0, 'source ...
    #     { 'type' : 'polarity',    'outcome': {'score': 0.108126295001 ...
    #     { 'type' : 'objectivity', 'outcome': {'score': 0.487846736596 ...
    #     { 'type' : 'bias',        'outcome': {'score': 20.67598528015 ...
    #   ]
    # }

    return object

xray_recorder.end_segment()