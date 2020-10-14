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
    
    credibilityresult = cr.getCredibilityScore(url)
    
    object = {
        "url" : url,
        "results" : [
            credibilityresult
        ]
    }
    
    jsonresponse = json.dumps(object)
    return jsonresponse


print(lambda_handler({"url":"http://bbc.co.uk"}, ""))