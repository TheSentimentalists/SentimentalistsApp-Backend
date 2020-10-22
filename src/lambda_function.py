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
        return {
            'statusCode': 400,
            'body': json.dumps("no url")
        }

    #### Adding "https://" to the URL if not present
    if (not url.startswith('https://') and not url.startswith('http://')):
        url = 'https://' + url

    if (not validators.url(url)):
        return json.dumps({"error" : "Invalid URL"})
    
    #### Define the object skeleton
    object = {
        "url" : url,
        "article" : {},
        "results" : []
    }

    try:
        credibilityresult = cr.getCredibilityScore(url)
        object['results'].append(credibilityresult)
    except Exception as e:
        object['results'].append({'type': 'credibility', 'outcome': {'score': -1}})
        
    try:
        sentanalysisresult = sa.sentimentAnalysis(url)
        object['article'] = {'header': sentanalysisresult['header'], 
                             'summary': sentanalysisresult['summary'],
                             'keywords': sentanalysisresult['keywords']}
        object['results'].append({'type': 'polarity',     'outcome': sentanalysisresult['polarity']})
        object['results'].append({'type': 'subjectivity', 'outcome': sentanalysisresult['subjectivity']})
    except Exception as e:
        object['article'] = {'error': 'The article could not be retrieved.'}
        object['results'].append({'type': 'polarity',     'error': 'no data available'})
        object['results'].append({'type': 'subjectivity', 'error': 'no data available'})

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

    jsonresponse = json.dumps(object)
    return jsonresponse
