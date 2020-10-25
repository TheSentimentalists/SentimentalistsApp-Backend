import json
import getCredibilityScore as cr
import sentimentAnalysis as sa
import validators

def lambda_handler(event, context):
## event must be a dict with a url key, and context can be nothing:
## lambda_handler({"url":"http://bbc.co.uk"}, "")
    
    try:
        url = event['url']
    except KeyError:
        return {"error" : "No URL provided"}

    #### Adding "https://" to the URL if not present
    if (not url.startswith('https://') and not url.startswith('http://')):
        url = 'https://' + url

    if (not validators.url(url)):
        return {"error" : "The url was bad"}

    #### Define the object skeleton
    object = {
        "url" : url,
        "results" : []
    }

    try:
        credibilityresult = cr.getCredibilityScore(url)
        object['results'].append(credibilityresult)
    except Exception as e:
        object['results'].append({'type': 'credibility', 'outcome': {"error" : "The credibility score was not available."}})

    try:
        console.log("lambda_function: Getting sentiment analysis...")
        sentanalysisresult = sa.sentimentAnalysis(url)
        console.log("lambda_function: Dumping result:")
        console.log(sentanalysisresult)
        if sentanalysisresult['text'] == '-1':
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


print(lambda_handler({"url":"http://www.bbc.co.uk/"}, ""))