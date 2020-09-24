## Function: getReliabilityScore
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

def getReliabilityScore(url):
    import requests
    import statistics 
    
    Gate_Source_Cred_API = "https://cloud-api.gate.ac.uk/process-document/source-credibility?annotations=:DomainCredibility"
    reliability_txt = requests.post(Gate_Source_Cred_API, data = url, headers={'Content-Type': 'text/plain'}, 
                                    auth=('gcc3g8cmwyob', '8ypn2huuqhu43zm3i2in'))
    rel_json = reliability_txt.json()

    if (rel_json['entities'] != {}):
        for item in rel_json['entities']['DomainCredibility']:
            p_score = item.get('credibility-score', 0)
            p_category = item.get('credibility-category', '')
            p_source = item.get('credibility-source', '')

            if item['credibility-source'] == 'Media Bias/Fact Check':
                return(p_score, p_category, p_source)
    else:
        return(-1)
    
    ## in case there is no 'Media Bias/Fact Check' but a different source:
    return(p_score, p_category, p_source)
    