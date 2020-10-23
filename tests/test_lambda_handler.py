## Function: test_lambda_handler.py
## Author: The Sentimentalists / Ana B Potje
## Date: 12/10/2020
##
## Tests the Function "lambda_handler.py"
## Uses PYTEST framework
###########################################################################################################

import lambda_function as lf   # The code to test

def test_URL_with_CredScore():
    result_score = {"type": "credibility", "outcome": {"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}
    result_dict = eval(lf.lambda_handler({"url":"https://www.bbc.co.uk/news/uk-54234084"}, ""))
    assert result_dict['results'][0] == result_score

def test_URL_with_NO_CredScore(): 
    result_score = {"type": "credibility", 'outcome': {"error" : "The credibility score was not available."}}
    result_dict = eval(lf.lambda_handler({"url":"https://socialistworker.co.uk/"}, ""))
    assert result_dict['results'][0] == result_score

def test_invalid_URL(): 
    result_dict = eval(lf.lambda_handler({"url":"xxxxx"}, ""))
    assert result_dict['error'] == "The url was bad"

def test_no_https(): 
    result_score = {"type": "credibility", "outcome":{"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}
    result_dict = eval(lf.lambda_handler({"url":"www.bbc.co.uk/news/uk-54234084"}, ""))
    assert result_dict['results'][0] == result_score

def test_no_www(): 
    result_score = {"type": "credibility", "outcome":{"score": 95.0, "source": "Media Bias/Fact Check", "category": "UNS"}}
    result_dict = eval(lf.lambda_handler({"url":"bbc.co.uk/news/uk-54234084"}, ""))
    assert result_dict['results'][0] == result_score

def test_SentAnalPolarity():
    result_score = {"type": "polarity", 'outcome': {"score": -1.0}}
    result_dict = eval(lf.lambda_handler({"url":"http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"}, ""))
    assert result_dict['results'][1] == result_score

def test_SentAnalSubjectivity():
    result_score = {"type": "subjectivity",  'outcome': {"score": 1.0}}
    result_dict = eval(lf.lambda_handler({"url":"http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"}, ""))
    assert result_dict['results'][2] == result_score

def test_ArticleHeader():
    result_score = 'Test'
    result_dict = eval(lf.lambda_handler({"url":"http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"}, ""))
    assert result_dict['article']['header'] == result_score

def test_ArticleSummary():
    result_score = 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.'
    result_dict = eval(lf.lambda_handler({"url":"http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"}, ""))
    assert result_dict['article']['summary'] == result_score

def test_ArticleKeywords():
    result_score = ['test', 'horrible', 'today', 'day', 'daytoday']
    result_dict = eval(lf.lambda_handler({"url":"http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"}, ""))
    assert result_dict['article']['keywords'].sort() == result_score.sort()
