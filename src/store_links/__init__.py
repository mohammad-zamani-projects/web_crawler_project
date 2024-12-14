from abc import ABC, abstractmethod

from setup.config import LINKS_FILE_PATH


class StoreBase(ABC):
    @abstractmethod
    def store_links(self):
        pass


class FileStore(StoreBase):
    def __init__(self, links):
        self.links = links

    def store_links(self):
        file_path = LINKS_FILE_PATH + "/links.txt"
        with open(file_path, "w") as f:
            for link in self.links:
                f.write(link.get("href") + "\n")


class DataBaseStore(StoreBase):
    def store_links(self):
        raise NotImplementedError
