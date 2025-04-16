import datetime
from abc import ABC, abstractmethod

from setup.config import LINKS_FILE_PATH
from src.advertisement_database_model import AdvertisementModel


class StoreBase(ABC):
    @abstractmethod
    def store_ads(self):
        pass


class FileStore(StoreBase):

    def __init__(self, ads_list):
        self.ads_list = ads_list

    def store_ads(self):
        file_path = LINKS_FILE_PATH + "/advertisements_info.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            for link in self.ads_list:
                f.write(f"title: {link['title']}\nused_amount: {link['used_amount']}\nprice: {link['price']}\n"
                        f"location: {link['location']}\nad_link: {link['ad_link']}\n{80 * '-'}\n")


class DataBaseStore(StoreBase):

    def __init__(self, ads_list):
        self.ads_list = ads_list

    def store_ads(self):
        for ad in self.ads_list:
            AdvertisementModel.create(
                title=ad['title'],
                used_amount=ad['used_amount'],
                price=ad['price'],
                location=ad['location'],
                ad_link=ad['ad_link'],
                crawled_time=datetime.datetime.now()
            ).save()






