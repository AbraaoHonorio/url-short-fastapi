from validator_collection import checkers


class CheckUrl:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not checkers.is_url(value):
            raise ValueError("Name cannot empty.")
        self.value = value


def is_valid_url(attr):
    def decorator(cls):
        setattr(cls, attr, CheckUrl())
        return cls

    return decorator
