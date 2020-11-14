"""
This module contains a a function that returns named entities from text
"""
from aws_xray_sdk.core import xray_recorder
import spacy

@xray_recorder.capture('spacyMatcher')
def spacyMatcher(text, tag=None):
    """
    This function takes text and an optional tag.
    It returns a dictionary tags and the entities corresponding to that tag.
    
    If no tag is specified, all tags will be used.
    
    Tags are SpaCy tags:
    PERSON - People, including fictional.
    ORG - Companies, agencies, institutions, etc.
    GPE - Countries, cities, states.
    PERCENT - Percentage, including ”%“.
    LANGUAGE - Any named language.
    DATE - Absolute or relative dates or periods.
    TIME - Times smaller than a day.
    LOC - Non-GPE locations, mountain ranges, bodies of water.
    NORP - Nationalities or religious or political groups.
    EVENT - Named hurricanes, battles, wars, sports events, etc.
    WORK_OF_ART - Titles of books, songs, etc.
    MONEY - Monetary values, including unit.
    QUANTITY - Measurements, as of weight or distance.
    ORDINAL - “first”, “second”, etc.
    CARDINAL - Numerals that do not fall under another type (not ordinal, quantity ..).
    """
     all_tags = ['PERSON','GPE','ORG','PERCENT','LANGUAGE','DATE','TIME','LOC','NORP','EVENT','WORK_OF_ART',
                    'MONEY','QUANTITY','ORDINAL','CARDINAL']
        
    tags = [tag] if tag else all_tags

    topics_by_tag = []
    if text != '-1':
        ### analysing the text 
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        interesting_words = [(ent.text, ent.label_) for ent in doc.ents]

        for tag in tags:
            values = {tup[0] for tup in interesting_words if any(i in tup for i in [tag])}        
            for obj in values:
                topics_by_tag.append({'type' : tag, 'topic' : obj})                    

    return topics_by_tag ### RETURNS A LIST of DICTIONARIES!
