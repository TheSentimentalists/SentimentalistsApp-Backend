## Function: test_spacyMatcher.py
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## Tests the Function "spacyMatcher.py"
## Uses PYTEST framework
###########################################################################################################

import spacyMatcher as spacyMat    # The code to test

def test_Person():
# PERSON - People, including fictional.
    url = 'https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post'
    set_person = {'Covid', 'Donald Trump', 'Miller', 'Stephen Miller', 'Trump'}
    assert spacyMat.spacyMatcher(url, 'PERSON') == set_person

def test_Org():
#ORG - Companies, agencies, institutions, etc.
    url = 'https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post'
    set_org = {'White House', 'Trump', 'the White House', 'Walter Reed'}
    assert spacyMat.spacyMatcher(url, 'ORG') == set_org

def test_GPE():
#GPE - Countries, cities, states.
    url = 'https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post'
    set_gpe = {'US'}
    assert spacyMat.spacyMatcher(url, 'GPE') == set_gpe
