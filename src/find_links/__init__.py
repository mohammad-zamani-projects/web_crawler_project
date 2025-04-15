import requests
from bs4 import BeautifulSoup


class GetPagesHtml:
    def __init__(self, url):
        self.url = url

    def request_html(self):
        try:
            response = requests.get(self.url)
        except Exception:
            raise Exception(f"Cannot get information of the {self.url}")

        if (response_status := response.status_code) != 200:
            print(f"The response of the {self.url} is {response_status}")

        return response


class FindLinks:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    def get_links(self):
        soup = BeautifulSoup(self.html_doc, "html.parser")
        soup_list = soup.find_all("a", attrs={"class": "kt-post-card__action"})  # find link by unique name of class
        return soup_list
