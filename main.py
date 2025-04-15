import sys

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
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import time

    # 🛠️ تنظیمات Chrome
    options = Options()
    options.add_argument("--headless")  # برای اجرا بدون باز شدن مرورگر
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--lang=fa-IR")

    # راه‌اندازی درایور
    driver = webdriver.Chrome(options=options)

    # رفتن به صفحه‌ی آگهی خودروها
    url = "https://divar.ir/s/tehran/car"
    driver.get(url)
    time.sleep(3)  # صبر برای لود اولیه

    # 🔁 اسکرول تا زمانی که محتوای جدید اضافه می‌شود
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(10):  # تعداد دفعات اسکرول، قابل تنظیم
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # اگر محتوای جدیدی لود نشد، خروج
        last_height = new_height

    # استخراج آگهی‌ها پس از اسکرول
    # ads = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__body")
    ads = driver.find_elements(By.CLASS_NAME, "kt-post-card__body")

    print(f"✅ تعداد آگهی‌های استخراج‌شده: {len(ads)}")

    for ad in ads:
        try:
            # title = ad.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div[1]/div/div/div[4]/div[1]/article/a/div/div[1]/h2").text
            # price = ad.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div[1]/div/div/div[5]/div[1]/article/a/div/div[1]/div[2]").text
            # used_amount = ad.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div[1]/div/div/div[6]/div[2]/article/a/div/div[1]/div[1]").text
            # print("🔹title:", title)
            # print("💵 price:", price)
            # print("📍 used_amount:", used_amount)
            # print("-" * 40)
            print(ad.text)
            print(40*"-")

        except Exception as e:
            continue

    driver.quit()



