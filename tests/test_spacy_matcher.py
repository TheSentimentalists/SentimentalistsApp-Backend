import spacy_matcher as spacymat


def test_spacy_matcher_tag_today():
    text = ('Today News ...')
    tags_matched = [{'type': 'DATE', 'topic': 'Today'}]
    assert spacymat.spacy_matcher(text) == tags_matched
