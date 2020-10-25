import json
import getCredibilityScore as cr
import sentimentAnalysis as sa
import validators
import sys
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
## event must be a dict with a url key, and context can be nothing:
## lambda_handler({"url":"http://bbc.co.uk"}, "")
    
    logger.info(f'LambdaFunction: Checking we have a URL...')
    try:
        url = event['url']
    except KeyError:
        logger.info(f'LambdaFunction: URL is not present.')
        return {"error" : "No URL provided"}

    #### Adding "https://" to the URL if not present
    logger.info(f'LambdaFunction: Checking URL has protocol...')
    if (not url.startswith('https://') and not url.startswith('http://')):
        url = 'https://' + url

    logger.info(f'LambdaFunction: Validating URL...')
    if (not validators.url(url)):
        logger.info(f'LambdaFunction: URL is not valid.')
        return {"error" : "The url was bad"}

    #### Define the object skeleton
    object = {
        "url" : url,
        "results" : []
    }

    logger.info(f'LambdaFunction: Trying to get credibility score...')
    try:
        credibilityresult = cr.getCredibilityScore(url)
        object['results'].append(credibilityresult)
    except Exception as e:
        logger.info(f'LambdaFunction: Could not get Credibility Score.')
        logger.info(e)
        object['results'].append({'type': 'credibility', 'outcome': {"error" : "The credibility score was not available."}})

    logger.info(f'LambdaFunction: Trying to get sentimentAnalysis score...')
    try:
        sentanalysisresult = sa.sentimentAnalysis(url)
        if sentanalysisresult['text'] == '-1':
            logger.info(f'LambdaFunction: sentimentAnalysis returned -1, dumping:')
            logger.info(sentanalysisresult)
            object['article'] = {'error': "The article summary could not be generated"}
            object['results'].append({'type': 'polarity',     "outcome": {"error" : "The polarity score could not be calculated."}})
            object['results'].append({'type': 'subjectivity', "outcome": {"error" : "The subjectivity score could not be calculated."}})
        else:
            object['article'] = {'header': sentanalysisresult['header'], 
                                 'summary': sentanalysisresult['summary'],
                                 'keywords': sentanalysisresult['keywords']}
            object['results'].append({'type': 'polarity',     'outcome': {"score": sentanalysisresult['polarity']}})
            object['results'].append({'type': 'subjectivity', 'outcome': {"score": sentanalysisresult['subjectivity']}})
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
        object['results'].append({'type': 'subjectivity', "outcome": {"error" : "The subjectivity score could not be calculated."}})

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
    #     { 'type' : 'subjectivity' .....},
    #     { 'type' : 'biasscore' .....}
    #   ]
    # }

    return object