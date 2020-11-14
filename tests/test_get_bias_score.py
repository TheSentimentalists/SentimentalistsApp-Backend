import get_bias_score as get_bias_scr


def test_get_bias_score_without_valid_credibility():
    result_score = {'type': 'bias', 'outcome': {'score': 50.0}}
    assert get_bias_scr.get_bias_score(-1, -1, 0) == result_score


def test_get_bias_score_with_credibility():
    result_score = {'type': 'bias', 'outcome': {'score': 66.66666666666667}}
    assert get_bias_scr.get_bias_score(0, -1, 0) == result_score
