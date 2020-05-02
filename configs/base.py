from collections import UserDict


class BaseConfig:
    def __getitem__(self, key):
        if hasattr(self, key.upper()):
            return getattr(self, key.upper())
        raise KeyError(key)
