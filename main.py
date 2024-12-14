import sys

from src.find_links import FindLinks
from src.find_links import GetPagesHtml
from setup.config import STORE_MODE
from setup.config import URL
from src.store_links import FileStore

if __name__ == "__main__":
    if sys.argv[1] == "find_links":
        source = GetPagesHtml(URL)
        html_source = source.request_html()
        links = FindLinks(html_source.text)
        links = links.get_links()
        # for link in links:
        #     print(link.get("href"))
        if STORE_MODE == "file":
            store = FileStore(links)
            store.store_links()
