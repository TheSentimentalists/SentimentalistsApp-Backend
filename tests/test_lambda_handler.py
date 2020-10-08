## Function: test_lambda_handler.py
## Author: The Sentimentalists / Ana B Potje
## Date: 05/10/2020
##
## Tests the Function "lambda_handler.py"
## Uses PYTEST framework
###########################################################################################################

import src.lambda_function as lf   # The code to test 

def test_URL_with_Score():
    result_score = {'type': 'credibility', 'score': 95.0, 'source': 'Media Bias/Fact Check', 'category': 'UNS'}
    assert lf.lambda_handler("https://www.bbc.co.uk/news/uk-54234084") == result_score
