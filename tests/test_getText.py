## Function: test_getText.py
## Author: The Sentimentalists / Ana B Potje
## Date: 01/10/2020
##
## Tests the Function "getText.py"
## Uses PYTEST framework
###########################################################################################################

import getText as getTxt   # The code to test

def test_get_Text():
    url = "https://www.wsj.com/articles/covid-19-left-u-k-s-boris-johnson-and-brazils-jair-bolsonaro-unscathed-politically-11601739583"
    Text = getTxt.getText(url)
    assert Text == "President Trump’s contraction of Covid-19 puts him in the company of two other conservative leaders who also made light of the risks of the coronavirus only to fall ill themselves, U.K. Prime Minister Boris Johnson and Brazilian President Jair Bolsonaro.For both of those leaders, getting ill not only didn’t hurt their political fortunes, but may have boosted them, at least in the short term.Soon..."
