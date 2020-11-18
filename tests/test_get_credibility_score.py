import get_credibility_score as get_cred_score
news_url = "https://www.bbc.co.uk/news/uk-54234084"
canary_url = "https://www.thecanary.co/"


def test_url_with_score():
    result_score = {'type': 'credibility',
                    'outcome': {'score': 95.0,
                                'source': 'Media Bias/Fact Check',
                                'category': 'UNS'}}
    assert get_cred_score.get_credibility_score(news_url) == result_score


def test_url_with_no_score():
    result_score = {'type': 'credibility',
                    'outcome': {"error":
                                "The credibility score was not available."}}
    assert get_cred_score.get_credibility_score(canary_url) == result_score
