import get_secret as secrets


def test_get_secret():
    key = "prod/test"
    region = "eu-west-2"
    result = secrets.get_secret(key, region)
    assert result == {'abc': '123'}


def test_get_bad_secret():
    key = "prod/badtest"
    region = "eu-west-2"
    result = secrets.get_secret(key, region)
    assert result == {'error': 'Resource Not Found'}
