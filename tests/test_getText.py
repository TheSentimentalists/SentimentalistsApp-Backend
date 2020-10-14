## Function: test_getText.py
## Author: The Sentimentalists / Ana B Potje
## Date: 01/10/2020
##
## Tests the Function "getText.py"
## Uses PYTEST framework
###########################################################################################################

import getText as getTxt   # The code to test

def test_get_Text_from_valid_URL():
    url = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
    Text = getTxt.getText(url)    
    assert Text == "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day."

def test_get_Text_from_Invalid_URL():
    url = 'https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    Text = getTxt.getText(url)    
    assert Text == '-1'
