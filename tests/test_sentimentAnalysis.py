## Function: test_sentimentAnalysis.py
## Author: The Sentimentalists / Ana B Potje
## Date: 05/10/2020
##
## Tests the Function "sentimentAnalysis.py", uses the function "getText.py" to get the text from the URL
## Uses PYTEST framework
###########################################################################################################

import sentimentAnalysis as sentAnalysis   # The code to test

list_kw = ['test', 'day', 'horrible', 'today', 'daytoday']
dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test", 
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw,
               'polarity': -1.0,
               'subjectivity': 1.0}

def test_Polarity():
    url = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['polarity'] == dict_return['polarity']

def test_Subjectivity():
    url = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['subjectivity'] == dict_return['subjectivity']

def test_sentiment_check_Text():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['text'] == dict_return['text']

def test_sentiment_check_Header():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['header'] == dict_return['header']

def test_sentiment_check_Summary():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['summary'] == dict_return['summary']

def test_sentiment_check_Keywords():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['keywords'].sort() == dict_return['keywords'].sort()

def test_Sentiment_for_Invalid_url():
    url = 'https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    get_dict = sentAnalysis.sentimentAnalysis(url)
    assert  get_dict['text'] == '-1'
