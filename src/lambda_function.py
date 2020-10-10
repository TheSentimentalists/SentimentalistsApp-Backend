import json
import uuid
import getCredibilityScore as cr
import validators

def lambda_handler(event, context):
    
    print(event)
    requestid = str(uuid.uuid4())
    
    try:
        url = event['url']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps("no url")
        }
    
    if (not validators.url(url)):
        return json.dumps({"error" : "Invalid URL"})
    
    credibilityresult = cr.getCredibilityScore(url)
    
    object = {
        "requestid" : requestid,
        "url" : url,
        "status" : "processed",
        "results" : [
            credibilityresult
        ]
    }
    
    jsonresponse = json.dumps(object)
    return jsonresponse

    
    print(lambda_handler({"url":"http://bbc.co.uk"}, ""))