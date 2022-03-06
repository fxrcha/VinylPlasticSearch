from typing import List, Optional

from utils.deco import soup_instance
from utils.request import Requester

from bs4 import BeautifulSoup

from model import SearchResult


class YES24(Requester):
    def __init__(self) -> None:
        self.url = "http://www.yes24.com/Product/Search?domain=MUSIC&query="
        self.soup: Optional[BeautifulSoup] = None
        super().__init__()

    @soup_instance
    async def search_album(self, album, artist) -> BeautifulSoup:
        query = f"{artist} - {album}"

        return await self.get(self.url + query, return_type="text")

    def __grab_title(self, asset) -> str:
        res = asset.find("a", {"class": "gd_name"}).text

        if asset.find("span", {"class": "gd_feature"}):
            res += f" ({asset.find('span', {'class': 'gd_feature'}).text})"

        return res

    def __grab_artist(self, asset) -> str:
        if asset.find("span", {"class": "authPub info_auth"}).find(
            "span", {"class": "moreAuthArea"}
        ):
            asset.find("span", {"class": "authPub info_auth"}).find(
                "span", {"class": "moreAuthArea"}
            ).decompose()

        return asset.find("span", {"class": "authPub info_auth"}).text

    def __get_status(self, asset) -> str:
        if asset.find("span", {"class": "btn_row soldOut"}):
            return "품절"

        return "구매 가능"

    async def crawl(self, album, artist) -> List[SearchResult]:
        self.soup = await self.search_album(album, artist)

        result = []

        for i in self.soup.find("ul", {"id": "yesSchList"}).find_all(
            "div", {"class": "itemUnit"}
        ):
            item_info = i.find("div", {"class": "item_info"})
            btns = i.find("div", {"class": "item_btnCol"})

            if item_info.find("span", {"class": "txt_sale"}):
                sale_rate = item_info.find("span", {"class": "txt_sale"}).text

            result.append(
                SearchResult(
                    typ=item_info.find("span", {"class": "gd_res"}).text,
                    album_title=self.__grab_title(asset=item_info),
                    artist=self.__grab_artist(asset=item_info).strip(),
                    price=item_info.find("strong", {"class": "txt_num"}).text,
                    status=self.__get_status(asset=btns),
                    sale_rate=sale_rate,
                )
            )

        return result
