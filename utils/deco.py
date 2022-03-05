from functools import wraps
from bs4 import BeautifulSoup


def soup_instance(func):
    @wraps(func)
    async def real(self, *args, **kwargs):
        raw = await func(self, *args, **kwargs)
        return BeautifulSoup(raw, "html.parser")

    return real


def soup_instance_sync(func):
    @wraps(func)
    def real(self, *args, **kwargs):
        raw = func(self, *args, **kwargs)
        return BeautifulSoup(raw, "html.parser")

    return real
