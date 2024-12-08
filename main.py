import sys

from src.find_links import FindLinks

if __name__ == "__main__":
    if sys.argv[1] == "find_links":
        url = "https://paris.craigslist.org/search/hhh?cc=gb&lang=en#search=1~gallery~0~0"
        links = FindLinks(url)
        links.get_links()
