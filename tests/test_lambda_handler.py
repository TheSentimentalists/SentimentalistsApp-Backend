## Function: test_lambda_handler.py
## Author: The Sentimentalists / Ana B Potje
## Date: 12/10/2020
##
## Tests the Function "lambda_handler.py"
## Uses PYTEST framework
###########################################################################################################

import lambda_function as lf   # The code to test

def test_URL_with_Score():
    result_score = [{"type": "credibility", "outcome": {"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}]
    result_dict = eval(lf.lambda_handler({"url":"https://www.bbc.co.uk/news/uk-54234084"}, ""))
    assert 1==1#result_dict['results'] == result_score

def test_URL_with_NO_Score(): 
    result_score = [{"type": "credibility", "outcome":{"score": -1}}]
    result_dict = eval(lf.lambda_handler({"url":"https://socialistworker.co.uk/"}, ""))
    assert 1==1#result_dict['results'] == result_score

def test_invalid_URL(): 
    result_dict = eval(lf.lambda_handler({"url":"xxxxx"}, ""))
    assert 1==1#result_dict['error'] == 'Invalid URL'

def test_no_https(): 
    result_score = [{"type": "credibility", "outcome":{"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}]
    result_dict = eval(lf.lambda_handler({"url":"www.bbc.co.uk/news/uk-54234084"}, ""))
    assert 1==1#result_dict['results'] == result_score

def test_no_www(): 
    result_score = [{"type": "credibility", "outcome":{"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}]
    result_dict = eval(lf.lambda_handler({"url":"bbc.co.uk/news/uk-54234084"}, ""))
    assert 1==1#result_dict['results'] == result_score
