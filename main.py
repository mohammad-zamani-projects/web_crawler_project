import sys
import time

from bs4 import BeautifulSoup

from src.find_links import FindLinks
from src.find_links import GetPagesHtml
from setup.config import STORE_MODE
from setup.config import URL
from src.store_links import FileStore

# if __name__ == "__main__":
    # # if sys.argv[1] == "find_links" or sys.argv[1] == "-f":
    # source = GetPagesHtml(URL)
    # html_source = source.request_html()
    # links = FindLinks(html_source.text)
    # links = links.get_links()
    # for link in links:
    #     print(link.get("href"))
    #     # if STORE_MODE == "file":
    #     #     store = FileStore(links)
    #     #     store.store_links()



if __name__ == "__main__":

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
    from time import sleep
    import chromedriver_autoinstaller

    # Autoinstall chrome drive (if necessary)
    chromedriver_autoinstaller.install()

    # Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # If you comment this line, chrome opened in runtime
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    while True:
        # Running Chrome
        driver = webdriver.Chrome(options=options)
        driver.get("https://divar.ir/s/tehran/car")
        sleep(3)

        # Scrolling and get page data
        num_scrolls = 10
        collected_ads = []

        for _ in range(num_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)  # Wait to load ads

            ads = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__body")

            for ad in ads:
                try:
                    title = ad.find_element(By.TAG_NAME, "h2").text
                    # used_amount = ad.find_element(By.CSS_SELECTOR, "div.kt-post-card__description").text
                    used_amount = ad.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")[0].text
                    price = ad.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")[1].text
                    # location = ad.find_element(By.CSS_SELECTOR, "div.kt-post-card__bottom-description").text
                    collected_ads.append((title, used_amount, price))
                except (StaleElementReferenceException, NoSuchElementException):
                    continue
        if len(collected_ads) > 0:
            break
        else:
            print("Failed to get ads, Trying one more time...")

    for (title, used_amount, price) in collected_ads:
        print(f"title: {title}")
        print(f"used_amount: {used_amount}")
        print(f"price: {price}")
        print(60 * "-")

    print(20 * "#")
    print(f"Number of ads: {len(collected_ads)}")
    print(20 * "#")

    driver.quit()



