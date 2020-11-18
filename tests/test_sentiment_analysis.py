import sentiment_analysis as sent_analysis
url_today = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
bad_url_today = "https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"


list_kw = ['test', 'day', 'horrible', 'today', 'daytoday']
dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test",
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw,
               'polarity': -1.0,
               'subjectivity': 1.0}


def test_polarity():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['polarity'] == dict_return['polarity']


def test_sentiment_check_text():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['text'] == dict_return['text']


def test_sentiment_check_header():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['header'] == dict_return['header']


def test_subjectivity():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['subjectivity'] == dict_return['subjectivity']


def test_sentiment_check_summary():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['summary'] == dict_return['summary']


def test_sentiment_check_keywords():
    get_dict = sent_analysis.sentiment_analysis(url_today)
    assert get_dict['keywords'].sort() == dict_return['keywords'].sort()


def test_sentiment_for_invalid_url():
    get_dict = sent_analysis.sentiment_analysis(bad_url_today)
    assert get_dict['text'] == '-1'
