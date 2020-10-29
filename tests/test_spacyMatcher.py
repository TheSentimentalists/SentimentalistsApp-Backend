## Function: test_spacyMatcher.py
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## Tests the Function "spacyMatcher.py"
## Uses PYTEST framework
###########################################################################################################

import spacyMatcher as spacyMat    # The code to test

text = ('Today - News from BBC: Bad news for Donald Trump in USA, 90% of the population complain '
'and a thousand people shout in English on the streets - this happened at 11:00. '
'Also, the Rocky Mountains seems to be more and more in risk ... Spanish nationals are applying for a permit. '
'World War II truly changed the world. The Bible is the most read book in the world. '
'The third released collection is worth £10,000,000. Not easy to walk 20 kilometers in that steep hilly place...')

def test_Person(): # PERSON - People, including fictional.
    set_person = [{'type': 'PERSON', 'topic': 'Donald Trump'}]
    assert spacyMat.spacyMatcher(text, 'PERSON') == set_person

def test_GPE(): #GPE - Countries, cities, states.
    set_gpe = [{'type': 'GPE', 'topic': 'USA'}]
    assert spacyMat.spacyMatcher(text, 'GPE') == set_gpe

def test_Org(): #ORG - Companies, agencies, institutions, etc.
    set_org = [{'type': 'ORG', 'topic': 'BBC'}]
    assert spacyMat.spacyMatcher(text, 'ORG') == set_org

def test_Percent(): #Percentage, including ”%“.
    set_pct = [{'type': 'PERCENT', 'topic': '90%'}]
    assert spacyMat.spacyMatcher(text, 'PERCENT') == set_pct

def test_Language(): #Any named language.
    set_lang = [{'type': 'LANGUAGE', 'topic': 'English'}]
    assert spacyMat.spacyMatcher(text, 'LANGUAGE') == set_lang

def test_Date(): #Absolute or relative dates or periods.
    set_date = [{'type': 'DATE', 'topic': 'Today'}]
    assert spacyMat.spacyMatcher(text, 'DATE') == set_date

def test_Time(): #Times smaller than a day.
    set_time = [{'type': 'TIME', 'topic': '11:00'}]
    assert spacyMat.spacyMatcher(text, 'TIME') == set_time

def test_Loc(): #Non-GPE locations, mountain ranges, bodies of water.
    set_loc = [{'type': 'LOC', 'topic': 'Rocky Mountains'}]
    assert spacyMat.spacyMatcher(text, 'LOC') == set_loc

def test_Norp(): #Nationalities or religious or political groups.
    set_norp = [{'type': 'NORP', 'topic': 'Spanish'}]
    assert spacyMat.spacyMatcher(text, 'NORP') == set_norp

def test_Event(): #Named hurricanes, battles, wars, sports events, etc.
    set_event = [{'type': 'EVENT', 'topic': 'World War II'}]
    assert spacyMat.spacyMatcher(text, 'EVENT') == set_event

def test_WorkArt(): #Titles of books, songs, etc.
    set_art = [{'type': 'WORK_OF_ART', 'topic': 'Bible'}]
    assert spacyMat.spacyMatcher(text, 'WORK_OF_ART') == set_art

def test_Money(): #Monetary values, including unit.
    set_money = [{'type': 'MONEY', 'topic': '10,000,000'}]
    assert spacyMat.spacyMatcher(text, 'MONEY') == set_money

def test_Quantity(): #Measurements, as of weight or distance.
    set_qty = [{'type': 'QUANTITY', 'topic': '20 kilometers'}]
    assert spacyMat.spacyMatcher(text, 'QUANTITY') == set_qty

def test_Ordinal(): #“first”, “second”, etc.
    set_ord = [{'type': 'ORDINAL', 'topic': 'third'}]
    assert spacyMat.spacyMatcher(text, 'ORDINAL') == set_ord

def test_Cardinal(): #Numerals that do not fall under another type (not ordinal, quantity ..)
    set_card = [{'type': 'CARDINAL', 'topic': 'a thousand'}]
    assert spacyMat.spacyMatcher(text, 'CARDINAL') == set_card

def test_ALL(): #ALL tages
    set_all = [{'type': 'PERSON', 'topic': 'Donald Trump'}, {'type': 'GPE', 'topic': 'USA'}, {'type': 'ORG', 'topic': 'BBC'}, {'type': 'PERCENT', 'topic': '90%'}, {'type': 'LANGUAGE', 'topic': 'English'}, {'type': 'DATE', 'topic': 'Today'}, {'type': 'TIME', 'topic': '11:00'}, {'type': 'LOC', 'topic': 'Rocky Mountains'}, {'type': 'NORP', 'topic': 'Spanish'}, {'type': 'EVENT', 'topic': 'World War II'}, {'type': 'WORK_OF_ART', 'topic': 'Bible'}, {'type': 'MONEY', 'topic': '10,000,000'}, {'type': 'QUANTITY', 'topic': '20 kilometers'}, {'type': 'ORDINAL', 'topic': 'third'}, {'type': 'CARDINAL', 'topic': 'a thousand'}]
    assert spacyMat.spacyMatcher(text, '') == set_all
