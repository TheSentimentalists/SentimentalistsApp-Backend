## Function: test_lambda_handler.py
## Author: The Sentimentalists / Ana B Potje
## Date: 12/10/2020
##
## Tests the Function "lambda_handler.py"
## Uses PYTEST framework
###########################################################################################################

import lambda_function as lf   # The code to test

def test_URL_with_Score(): 
    result_score = [{"type": "credibility", "score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}]
    result_dict = eval(lf.lambda_handler({"url":"https://www.bbc.co.uk/news/uk-54234084"}, ""))
    assert result_dict['results'] == result_score
    
def test_invalid_URL(): 
    result_dict = eval(lf.lambda_handler({"url":"xxxxx"}, ""))
    assert result_dict['error'] == 'Invalid URL'
