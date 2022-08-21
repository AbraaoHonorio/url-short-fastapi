from application.domain.url_short import UrlShort
from application.domain.url_short_repository import URLRepository


class URLShortener:

    def __init__(self, url_repository: URLRepository) -> None:
        self.url_repository = url_repository

    def excute(self, long_url: str) -> str:
        url_short = self.url_repository.get_by_long_url(long_url)
        if url_short:
            return url_short.hash

        url_short = UrlShort(0, long_url, "")
        self.url_repository.add(url_short)
        return url_short.hash
