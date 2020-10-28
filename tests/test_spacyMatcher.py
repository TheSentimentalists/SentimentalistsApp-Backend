## Function: test_spacyMatcher.py
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## Tests the Function "spacyMatcher.py"
## Uses PYTEST framework
###########################################################################################################

import spacyMatcher as spacyMat    # The code to test

text = ('Today - News from BBC: Interesting day for Donald Trump in USA, 90% of the population complain '
'and a thousand people shout in English on the streets. This happened on 12th October at 11:00. '
'Also, the Rocky Mountains seems to be more and more in risk ...Cars manufacturers such as Toyota and '
'BMW are starting a big strike. French and german speaking countries are currently the ones most visited. '
'The new World War II book was released. The Bible is the most read book in the world. '
'The Chanel third released collection is worth £10,000,000. It took more than 5 hours '
'to walk 20 kilometers in that pace...')

def test_Person(): # PERSON - People, including fictional.
    set_person = {'Donald Trump'}
    assert spacyMat.spacyMatcher(text, 'PERSON') == set_person

def test_GPE(): #GPE - Countries, cities, states.
    set_gpe = {'USA'}
    assert spacyMat.spacyMatcher(text, 'GPE') == set_gpe

def test_Org(): #ORG - Companies, agencies, institutions, etc.
    set_org = {'Toyota', 'BBC', 'BMW', 'Chanel'}
    assert spacyMat.spacyMatcher(text, 'ORG') == set_org

def test_Percent(): #Percentage, including ”%“.
    set_pct = {'90%'}
    assert spacyMat.spacyMatcher(text, 'PERCENT') == set_pct

def test_Language(): #Any named language.
    set_lang = {'English'}
    assert spacyMat.spacyMatcher(text, 'LANGUAGE') == set_lang

def test_Date(): #Absolute or relative dates or periods.
    set_date = {'Interesting day', 'Today', '12th October'}
    assert spacyMat.spacyMatcher(text, 'DATE') == set_date

def test_Time(): #Times smaller than a day.
    set_time = {'11:00', 'more than 5 hours'}
    assert spacyMat.spacyMatcher(text, 'TIME') == set_time

def test_Loc(): #Non-GPE locations, mountain ranges, bodies of water.
    set_loc = {'Rocky Mountains'}
    assert spacyMat.spacyMatcher(text, 'LOC') == set_loc

def test_Norp(): #Nationalities or religious or political groups.
    set_norp = {'French', 'german'}
    assert spacyMat.spacyMatcher(text, 'NORP') == set_norp

def test_Event(): #Named hurricanes, battles, wars, sports events, etc.
    set_event = {'World War II'}
    assert spacyMat.spacyMatcher(text, 'EVENT') == set_event

def test_WorkArt(): #Titles of books, songs, etc.
    set_art = {'Bible'}
    assert spacyMat.spacyMatcher(text, 'WORK_OF_ART') == set_art

def test_Money(): #Monetary values, including unit.
    set_money = {'10,000,000'}
    assert spacyMat.spacyMatcher(text, 'MONEY') == set_money

def test_Quantity(): #Measurements, as of weight or distance.
    set_qty = {'20 kilometers'}
    assert spacyMat.spacyMatcher(text, 'QUANTITY') == set_qty

def test_Ordinal(): #“first”, “second”, etc.
    set_ord = {'third'}
    assert spacyMat.spacyMatcher(text, 'ORDINAL') == set_ord

def test_Cardinal(): #Numerals that do not fall under another type (not ordinal, quantity ..)
    set_card = {'a thousand'}
    assert spacyMat.spacyMatcher(text, 'CARDINAL') == set_card
