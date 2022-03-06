from bs4 import BeautifulSoup
from requests import get


def asdf() -> BeautifulSoup:
    a = get("http://www.yes24.com/Product/Search?domain=MUSIC&query=donda").text
    return BeautifulSoup(a, "html.parser")


def shitpost(asset) -> str:
    asdf = asset.find("span", {"class": "authPub info_auth"})
    if asdf.find("span", {"class": "moreAuthArea"}):
        asdf.find("span", {"class": "moreAuthArea"}).decompose()

    asdf = asset.find("span", {"class": "authPub info_auth"}).text
    return asdf


def second_shitpost(asset) -> str:
    if asset.find("span", {"class": "btn_row soldOut"}):
        return "품절"

    return "구매 가능"


def test(s: BeautifulSoup):
    for i in s.find("ul", {"id": "yesSchList"}).find_all("div", {"class": "itemUnit"}):
        print("start")
        item_info = i.find("div", {"class": "item_info"})
        btns = i.find("div", {"class": "item_btnCol"})

        print(item_info.find("span", {"class": "gd_res"}).text)
        print("b")
        print(item_info.find("a", {"class": "gd_name"}).text)
        print("asdf")
        print(shitpost(item_info).strip())
        print("asdfasdf")
        print(item_info.find("strong", {"class": "txt_num"}).text)
        print("asdfasdfasdfasdf")
        if item_info.find("span", {"class": "txt_sale"}):
            print(item_info.find("span", {"class": "txt_sale"}).text)

        print("asfdasdgtj")
        print(second_shitpost(btns))
        print("end")


if __name__ == "__main__":
    soup = asdf()
    test(soup)
