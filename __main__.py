from cli.header import header
from utils.config import load_config
from importlib import import_module

from crawl.yes24 import YES24

import asyncio


def importer(module_name: str) -> str:
    import_module(f"crawl.{module_name.lower()}")
    return module_name


if __name__ == "__main__":
    header()
    config = load_config()

    import_list = [
        importer(key)
        for key in config["search_sites"].keys()
        if config["search_sites"][key]
    ]
