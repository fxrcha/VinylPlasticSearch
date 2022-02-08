from cli.header import header
from utils.config import load_config
from importlib import import_module


if __name__ == "__main__":
    header()
    config = load_config()

    for key in config["search_sites"].keys():
        if config["search_sites"][key]:
            import_module(f"crawl.{key.lower()}")
