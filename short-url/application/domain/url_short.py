from typing import Optional
from uuid import uuid4

from application.resource.validator import is_valid_url


@is_valid_url("long_url")
class UrlShort:
    BIT_SIZE = 64
    ALPHABET_BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self,
                 long_url: str,
                 id: Optional[int] = None,
                 hash: Optional[str] = None) -> None:
        self.id = id or self.generate_id()
        self.long_url = long_url
        self.hash = hash or self.to_base62()

    def generate_id(self) -> int:
        return uuid4().int >> self.BIT_SIZE

    def to_base62(self) -> str:
        if not self.id or self.id == 0:
            return "0"

        number_base10 = self.id
        list_characters = []
        base = len(self.ALPHABET_BASE62)
        while number_base10:
            number_base10, rem = divmod(number_base10, base)
            list_characters.append(self.ALPHABET_BASE62[rem])

        hash_result = "".join(reversed(list_characters))
        return hash_result

