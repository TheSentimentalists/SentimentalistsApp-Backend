## Function: test_getCredibilityScore.py
## Author: The Sentimentalists / Ana B Potje
## Date: 05/10/2020
##
## Tests the Function "getCredibilityScore.py"
## Uses PYTEST framework
###########################################################################################################

import getCredibilityScore as getCredScore    # The code to test 

def test_URL_with_Score():
    result_score = (95.0, 'UNS', 'Media Bias/Fact Check')
    assert getCredScore.getCredibilityScore("https://www.bbc.co.uk/news/uk-54234084") == result_score

def test_URL_with_noScore():
    result_score = -1
    assert getCredScore.getCredibilityScore("https://www.thecanary.co/") == result_score