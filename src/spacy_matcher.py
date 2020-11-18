from aws_xray_sdk.core import xray_recorder
import spacy


@xray_recorder.capture('spacy_matcher')
def spacy_matcher(text):
    """
    Calls the Python Library Spacy with a TEXT to be analysed.

    Input: text (raw text, which was extracted from the user input URL
    Output: List of dictionary objects: [{'type': <tag>, 'topic': <str>},..]
    """

    all_topics = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    interesting_words = set([(ent.text, ent.label_) for ent in doc.ents])
    all_topics = [{'type': i[1], 'topic': i[0]} for i in interesting_words]

    return all_topics
