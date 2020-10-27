from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
import json
import getCredibilityScore as cr
import sentimentAnalysis as sa
import getBiasScore as bs
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

        object['article'] = {'error': "The article summary could not be generated"}
        object['results'].append({'type': 'polarity',     "outcome": {"error" : "The polarity score could not be calculated."}})
        object['results'].append({'type': 'objectivity', "outcome": {"error" : "The objectivity score could not be calculated."}})

    logger.info(f'LambdaFunction: Trying to get bias score...')
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

    #### Intended object to return:
    # {
    #   'url':'http://bbc.co.uk',
    #   'article' : {
    #     'header' : 'An Article Title',
    #     'summary' : 'The Article Summary',
    #     'keywords' : ['Boris Johnson', 'Brexit']
    #   },
    #   'results' : [
    #     { 'type' : 'credibility' ...... },
    #     { 'type' : 'polarity' ..... },
    #     { 'type' : 'objectivity' .....},
    #     { 'type' : 'biasscore' .....}
    #   ]
    # }

    return object

xray_recorder.end_segment()