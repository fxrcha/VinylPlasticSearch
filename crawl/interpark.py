from typing import Optional
from utils.deco import soup_instance
from utils.request import Requester
from bs4 import BeautifulSoup


class INTERPARK(Requester):
    def __init__(self) -> None:
        self.url = "http://www.yes24.com/Product/Search?domain=MUSIC&query="
        self.soup: Optional[BeautifulSoup] = None
        super().__init__()

    @soup_instance
    async def search_album(self, album, artist) -> BeautifulSoup:
        query = f"{artist} - {album}"

        return await self.get(self.url + query, return_type="text")

    async def crawl(self, album, artist):
        self.soup = await self.search_album(album, artist)

        self.soup.find_all()

        # yesSchList > li > div > div.item_info > div.info_row.info_name > span.gd_res
