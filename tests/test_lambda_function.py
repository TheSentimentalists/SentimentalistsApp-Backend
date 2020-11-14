import lambda_function as lf
url_today = "http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html"
bad_url_today = 'https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
url_bias_score = "https://www.bbc.co.uk/news/uk-54234084"
url_today_image = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/image_test.html'
url_image = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/test.png'
text_horrible_day = 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.'


def test_url_with_cred_score():
    result_score = {"type": "credibility", "outcome": {"score": 95.0,
                    "source": "Media Bias/Fact Check", "category": "UNS"}}
    result_dict = lf.lambda_handler(
                       {"url":
                        "https://www.bbc.co.uk/news/uk-54234084"}, "")
    assert result_dict['results'][0] == result_score


def test_url_with_no_cred_score():
    result_score = {"type": "credibility",
                    'outcome': {"error": 'The credibility score was not '
                                         'available.'}}
    result_dict = lf.lambda_handler({"url":
                                     "https://socialistworker.co.uk/"}, "")
    assert result_dict['results'][0] == result_score


def test_invalid_url():
    result_dict = lf.lambda_handler({"url": "xxxxx"}, "")
    print(result_dict)
    print(type(result_dict))
    assert result_dict['error'] == "The url was bad"


def test_no_https():
    result_score = {"type": "credibility",
                    "outcome": {"score": 95.0,
                                "source": "Media Bias/Fact Check",
                                "category": "UNS"}}
    result_dict = lf.lambda_handler({"url":
                                     "www.bbc.co.uk/news/uk-54234084"}, "")
    assert result_dict['results'][0] == result_score


def test_no_www():
    result_score = {"type": "credibility",
                    "outcome": {"score": 95.0,
                                "source": "Media Bias/Fact Check",
                                "category": "UNS"}}
    result_dict = lf.lambda_handler({"url": "bbc.co.uk/news/uk-54234084"}, "")
    assert result_dict['results'][0] == result_score


def test_sent_anal_polarity():
    result_score = {"type": "polarity", 'outcome': {"score": -1.0}}
    result_dict = lf.lambda_handler({"url": url_today}, "")
    assert result_dict['results'][1] == result_score


def test_sent_anal_subjectivity():
    result_score = {"type": "objectivity",  'outcome': {"score": 0.0}}
    result_dict = lf.lambda_handler({"url": url_today}, "")
    assert result_dict['results'][2] == result_score


def test_article_header():
    result_score = 'Test'
    result_dict = lf.lambda_handler({"url": url_today}, "")
    assert result_dict['article']['header'] == result_score


def test_article_summary():
    result_score = text_horrible_day
    result_dict = lf.lambda_handler({"url": url_today}, "")
    assert result_dict['article']['summary'] == result_score


def test_article_keywords():
    result_score = ['test', 'horrible', 'today', 'day', 'daytoday']
    result_dict = lf.lambda_handler({"url": url_today}, "")
    assert result_dict['article']['keywords'].sort() == result_score.sort()


def test_bias_score_with_no_credibility():
    result_dict = lf.lambda_handler({"url": url_today}, "")
    result_score = {'type': 'bias', 'outcome': {'score': 100.0}}
    assert result_dict['results'][3] == result_score


def test_bias_score_with_credibility():
    result_dict = lf.lambda_handler({"url": url_bias_score}, "")
    result_score = {'type': 'bias', 'outcome': {'score': 45.0}}
    assert result_dict['results'][3] == result_score


def test_bias_score_no_pol_subj():
    result_dict = lf.lambda_handler({"url": bad_url_today}, "")
    result_score = {'type': 'bias',
                    'outcome': {"error": "The bias score was not available."}}
    assert result_dict['results'][3] == result_score


def test_topics():
    result_dict = lf.lambda_handler({"url": url_today}, "")
    result_score = [{'type': 'DATE', 'topic': 'Today'}]
    assert result_dict['article']['topics'] == result_score


def test_image():
    result_dict = lf.lambda_handler({"url": url_today_image}, "")
    assert result_dict['article']['image'] == url_image
