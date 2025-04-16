from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import sleep
from setup.config import URL, NUMBER_PAGE_SCROLL
import chromedriver_autoinstaller


class GetPageInfo:

    def __init__(self):
        # Autoinstall chrome drive (if necessary)
        chromedriver_autoinstaller.install()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # If you comment this line, chrome opened in runtime
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.collected_ads = []

    def get_page_info(self):
        while True:
            # Running Chrome
            driver = webdriver.Chrome(options=self.options)
            driver.get(URL)
            sleep(3)

            # Scrolling and get page data
            for _ in range(NUMBER_PAGE_SCROLL):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)  # Wait to load ads

                ads = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__body")

                for ad in ads:
                    try:
                        title = ad.find_element(By.TAG_NAME, "h2").text
                        # used_amount = ad.find_element(By.CSS_SELECTOR, "div.kt-post-card__description").text
                        used_amount = ad.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")[0].text
                        price = ad.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")[1].text
                        location = ad.find_element(By.CSS_SELECTOR, "span.kt-post-card__bottom-description").text
                        ad_link = ad.find_element(By.XPATH, "..").get_attribute("href")
                        self.collected_ads.append((title, used_amount, price, location, ad_link))
                    except (StaleElementReferenceException, NoSuchElementException):
                        print("A problem has occurred in convert links.")

            driver.quit()
            if len(self.collected_ads) > 0:
                break
            else:
                print("Failed to get ads, Trying one more time...")

        return self.collected_ads

    def get_ads(self, ads_list):
        for (title, used_amount, price, location, ad_link) in self.collected_ads:
            ads_list.append(
                {
                    "title": title,
                    "used_amount": used_amount,
                    "price": price,
                    "location": location,
                    "ad_link": ad_link
                }
            )
