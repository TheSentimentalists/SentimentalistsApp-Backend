## Function: test_getText.py
## Author: The Sentimentalists / Ana B Potje
## Date: 01/10/2020
##
## Tests the Function "getText.py"
## Uses PYTEST framework
###########################################################################################################

import getSecret as secrets   # The code to test

def test_get_Secret():
    key = "prod/test"
    region = "eu-west-2"
    result = secrets.getSecret(key, region)
    assert result == {'abc': '123'}

def test_get_Bad_Secret():
    key = "prod/badtest"
    region = "eu-west-2"
    result = secrets.getSecret(key, region)
    assert result == {'error':'Resource Not Found'}
