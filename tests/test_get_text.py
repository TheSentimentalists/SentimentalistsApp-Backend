import get_text as get_txt
url_today = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
bad_url_today = "https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
url_image = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/test.png'
url_today_image = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/image_test.html"

list_kw = ['test', 'day', 'horrible', 'today', 'daytoday']
dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test",
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw}


def test_get_text_check_text():
    get_text_dict = get_txt.get_text(url_today)
    assert get_text_dict['text'] == dict_return['text']


def test_get_text_check_header():
    get_text_dict = get_txt.get_text(url_today)
    assert get_text_dict['header'] == dict_return['header']


def test_get_text_check_summary():
    get_text_dict = get_txt.get_text(url_today)
    assert get_text_dict['summary'] == dict_return['summary']


def test_get_text_check_keywords():
    get_text_dict = get_txt.get_text(url_today)
    assert get_text_dict['keywords'].sort() == dict_return['keywords'].sort()


def test_get_text_from_invalid_url():
    get_text_dict = get_txt.get_text(bad_url_today)
    assert get_text_dict['text'] == '-1'


dict_return = {'text': "Horrible Day!Today is a horrible day. Today is a horrible day. Today is a horrible day.",
               'header': "Test",
               'summary': 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.',
               'keywords': list_kw,
               'image': url_image}


def test_get_text_check_image():
    get_text_dict = get_txt.get_text(url_today_image)
    assert get_text_dict['image'] == dict_return['image']
