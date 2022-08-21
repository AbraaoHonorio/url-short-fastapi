from _pytest.python_api import raises

from application.domain.url_short import UrlShort


class TestUrlShort:
    def test_should_is_valid(self):
        long_url_expect = "https://www.google.com"
        ## given
        url_short = UrlShort(long_url=long_url_expect)

        ## when
        hash_in_base62 = url_short.to_base62()

        ## then

        assert long_url_expect == url_short.long_url
        assert hash_in_base62 == url_short.hash
        assert isinstance(url_short.id, int)

    def test_should_is_not_invalid(self):
        ## given
        long_url_expect = ""


        # When / Then
        with raises(ValueError):
            url_short = UrlShort(long_url=long_url_expect)
            print(url_short)
