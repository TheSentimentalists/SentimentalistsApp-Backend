import json
import getCredibilityScore as cr
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
        "results" : []
    }

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

    #### Try add each result set
    try:
        credibilityresult = cr.getCredibilityScore(url) # {"type" : "reliability", "results" :....}
        # > maybe this? object['results'].append(credibilityresult)
    except:
        # > maybe this? object['results'].append(""

    #### Try add the article data
    try:
        # get the article
        # try append article {"heading":"British credit risk", "summary":"Something..."} to object {}
    except:
        # append articler error "article" : {"error":"The article could not be retrieved."}

    
    jsonresponse = json.dumps(object)
    return jsonresponse