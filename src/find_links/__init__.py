import requests
from bs4 import BeautifulSoup

class FindLinks:
    def __init__(self, url):
        self.url = url

    def get_links(self):
        try:
            response = requests.get(self.url)
        except Exception:
            raise Exception(f"Cannot get information of the {self.url}")

        print(response.status_code)

