## Function: test_getText.py
## Author: The Sentimentalists / Ana B Potje
## Date: 01/10/2020
##
## Tests the Function "getText.py"
## Uses PYTEST framework
###########################################################################################################

import getText as getTxt   # The code to test

list_kw = ['test', 'day', 'horrible', 'today', 'daytoday']
dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test", 
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw}

def test_getText_check_Text():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['text'] == dict_return['text']

def test_getText_check_Header():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['header'] == dict_return['header']

def test_getText_check_Summary():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['summary'] == dict_return['summary']

def test_getText_check_Keywords():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['keywords'].sort() == dict_return['keywords'].sort()

def test_get_Text_from_Invalid_URL():
    url = "https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['text'] == '-1'

dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test", 
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw,
               'image': 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/test.png'}

def test_getText_check_Image():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/image_test.html"
    getText_dict = getTxt.getText(url)
    assert  getText_dict['image'] == dict_return['image']