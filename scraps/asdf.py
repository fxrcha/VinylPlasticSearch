from bs4 import BeautifulSoup
from requests import get


def asdf() -> BeautifulSoup:
    a = get("http://www.yes24.com/Product/Search?domain=MUSIC&query=donda").text
    return BeautifulSoup(a, "html.parser")


def test(s: BeautifulSoup):
    for i in s.find("ul", {"id": "yesSchList"}).find_all("div", {"class": "itemUnit"}):
        item_info = i.find("div", {"class": "item_info"})


if __name__ == "__main__":
    soup = asdf()
    test(soup)
