## Function: test_validateURL.py
## Author: The Sentimentalists / Ana B Potje
## Date: 30/Sep/2020
##
## Tests the Function "validateURL.py"
## Uses PYTEST framework
###########################################################################################################

import validateURL as valURL    # The code to test

def test_valid_URL():
    assert valURL.validateURL("https://www.bbc.co.uk/") == 1

def test_invalid_URL():
    assert valURL.validateURL("1234") == -1
