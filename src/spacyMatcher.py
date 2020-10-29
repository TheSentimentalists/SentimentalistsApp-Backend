## Function: spacyMatcher
## Input: TEXT and TAG (PERSON, ORG, GPE, etc)
##        If TAG = '' will return all TAGs 
## Output: List of dictionaries for all TAGs found in the text (os a specific tag if passed)
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## This function uses the Python Library Spacy. The user will input an URL and a "TAG" such as:
##    PERSON - People, including fictional.
##    ORG - Companies, agencies, institutions, etc.
##    GPE - Countries, cities, states.
##    PERCENT - Percentage, including ”%“.
##    LANGUAGE - Any named language.
##    DATE - Absolute or relative dates or periods.
##    TIME - Times smaller than a day.
##    LOC - Non-GPE locations, mountain ranges, bodies of water.
##    NORP - Nationalities or religious or political groups.
##    EVENT - Named hurricanes, battles, wars, sports events, etc.
##    WORK_OF_ART - Titles of books, songs, etc.
##    MONEY - Monetary values, including unit.
##    QUANTITY - Measurements, as of weight or distance.
##    ORDINAL - “first”, “second”, etc.
##    CARDINAL - Numerals that do not fall under another type (not ordinal, quantity ..)
##
## It will return a list with distinct values of all occurrences of that entity in the text.
###########################################################################################################

from aws_xray_sdk.core import xray_recorder

@xray_recorder.capture('spacyMatcher')
def spacyMatcher(text, tag): 
    import spacy

    if tag == '':
        all_tags = ['PERSON','GPE','ORG','PERCENT','LANGUAGE','DATE','TIME','LOC','NORP','EVENT','WORK_OF_ART',
                    'MONEY','QUANTITY','ORDINAL','CARDINAL']
    else:
        all_tags = [tag]

    all_topics = []
    if text != '-1':
        ### analysing the text 
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        interestWords = [(ent.text, ent.label_) for ent in doc.ents]

        for tag in all_tags:
            values_set = []
            list_all_values = [tup[0] for tup in interestWords if any(i in tup for i in [tag])]        
            values_set = set(list_all_values)
            for obj in values_set:
                all_topics.append({'type' : tag, 'topic' : obj})                    

    return(all_topics) ### RETURNS A LIST of DICTIONARIES!
