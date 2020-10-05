## Function: test_getText.py
## Author: The Sentimentalists / Ana B Potje
## Date: 01/10/2020
##
## Tests the Function "getText.py"
## Uses PYTEST framework
###########################################################################################################

import getText as getTxt   # The code to test

def test_get_Text():
    url = "https://www.ft.com/content/fde4b931-6cd9-4cb2-8cec-89b3ac876b88"
    Text = getTxt.getText(url)
    assert Text == "Make informed decisions with the FTKeep abreast of significant corporate, financial and political developments around the world. Stay informed and spot emerging risks and opportunities with independent global reporting, expert commentary and analysis you can trust."
