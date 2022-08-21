from abc import ABC, abstractmethod

from application.domain.url_short import UrlShort


class URLRepository(ABC):

    @abstractmethod
    def get(self, id: int) -> UrlShort:
        pass

    @abstractmethod
    def get_by_long_url(self, long_url: str) -> UrlShort:
        pass

    @abstractmethod
    def add(self, url_shorterner: UrlShorterner) -> None:
        pass

