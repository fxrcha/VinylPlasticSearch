from dataclasses import dataclass
from typing import Optional


@dataclass(init=True, repr=True)
class SearchResult:
    typ: Optional[str]
    album_title: Optional[str]
    artist: Optional[str]
    price: Optional[str]
    status: Optional[str]
    sale_rate: Optional[str]


__all__ = ["SearchResult"]
