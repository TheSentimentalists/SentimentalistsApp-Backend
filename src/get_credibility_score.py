from aws_xray_sdk.core import xray_recorder
import requests
import get_secret as secrets


@xray_recorder.capture('get_credibility_score')
def get_credibility_score(url):
    """
    Input: URL
    Output: Credibility Score, Category and Source
    This function calls the API Gate Source Credibility passing the URL to
    be analysed. It returns the Score, Category (Left Center, Fake News, ...)
    and the Source. If the website is reated in the source 'Media Bias/Fact
    Check', this source is then used. Otherwise it will a different source that
    rated the website, or return "-1" in case no rating is found.
    """

    p_score = 0
    p_category = ''
    p_source = ''
    return_dict = {'type': 'credibility', 'outcome': {'score': -1}}

    aws_secrets = secrets.get_secret("prod/getCredibilityScore/GATEKey",
                                     "eu-west-2")
    if "error" in aws_secrets:
        return return_dict

    gate_cred_api = "https://cloud-api.gate.ac.uk/process-document/source-credibility?annotations=:DomainCredibility"
    cred_txt = requests.post(gate_cred_api, data=url,
                             headers={'Content-Type': 'text/plain'},
                             auth=(aws_secrets['apiid'],
                                   aws_secrets['apikey']))
    rel_json = cred_txt.json()

    if (rel_json['entities'] != {}):
        for item in rel_json['entities']['DomainCredibility']:
            p_score = item.get('credibility-score', 0)
            p_category = item.get('credibility-category', '')
            p_source = item.get('credibility-source', '')

            return_dict = {'type': 'credibility',
                           'outcome': {'score': p_score,
                                       'source': p_source,
                                       'category': p_category}}

            if item['credibility-source'] == 'Media Bias/Fact Check':
                return(return_dict)
    else:
        return_dict = {'type': 'credibility',
                       'outcome': {"error":
                                   "The credibility score was not available."}}
        return(return_dict)

    return(return_dict)
