from typing import Any, Optional

from aiohttp import ClientSession


DEFAULT_HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


class HTTPException(Exception):
    """
    Exception which happens when HTTP status code is not 200 (OK).
    """

    def __init__(self, code, url) -> None:
        self.error = f"While requesting to {url}, request returned status {code}."

    def __str__(self) -> str:
        return self.error


class Base:
    def __init__(self) -> None:
        self.session: Optional[ClientSession] = None

    async def request(
        self,
        url: str,
        method: str,
        return_type: str,
        **kwargs: Any,
    ):
        if not self.session or self.session.closed:
            self.session = ClientSession()

        resp = await self.session.request(method, url, **kwargs)

        if resp.status == 200:
            return await getattr(resp, return_type)()

        else:
            raise HTTPException(resp.status, url)

    async def post(self, url: str, **kwargs: Any):
        return await self.request(url, "POST", **kwargs)

    async def get(self, url: str, **kwargs: Any):
        return await self.request(url, "GET", **kwargs)


class Requester(Base):
    pass
