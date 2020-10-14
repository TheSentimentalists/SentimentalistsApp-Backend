## Function: getCredibilityScore
## Input: URL
## Output: Credibility Score, Category and Source
## Author: The Sentimentalists / Ana B Potje
## Date: 24/Sep/2020
##
## This function calls the API Gate Source Credibility passing the URL to be analized.
## It returns the Score, Category (Left Center, Fake News, ...) and the Source.
## If the website is reated in the source 'Media Bias/Fact Check', this source is then used.
## Otherwise it will a different source that rated the website, or return "-1" in case no rating is found.
###########################################################################################################

def getCredibilityScore(url):
    import requests
    import getSecret as secrets

    p_score = 0
    p_category = '' 
    p_source = ''
    return_dict = {'type': 'credibility', 'outcome': {'score': -1} }

    aws_secrets = secrets.getSecret("prod/getCredibilityScore/GATEKey", "eu-west-2")
    if "error" in aws_secrets:
        return return_dict
    
    Gate_Source_Cred_API = "https://cloud-api.gate.ac.uk/process-document/source-credibility?annotations=:DomainCredibility"
    cred_txt = requests.post(Gate_Source_Cred_API, data = url, headers={'Content-Type': 'text/plain'}, 
                                    auth=(aws_secrets['apiid'], aws_secrets['apikey']))
    rel_json = cred_txt.json()

    if (rel_json['entities'] != {}):
        for item in rel_json['entities']['DomainCredibility']:
            p_score = item.get('credibility-score', 0)
            p_category = item.get('credibility-category', '')
            p_source = item.get('credibility-source', '')

            return_dict = {'type': 'credibility', 'outcome' : { 'score': p_score, 'source': p_source, 'category': p_category }}

            if item['credibility-source'] == 'Media Bias/Fact Check':
                return(return_dict)
    else:
        return_dict = {'type': 'credibility', 'outcome': {'score': -1}}
        return(return_dict)
    
    ## in case there is no 'Media Bias/Fact Check' but a different source:    
    return(return_dict)