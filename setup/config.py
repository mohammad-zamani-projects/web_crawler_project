import os
from pathlib import Path

# Wanted url
URL = "https://divar.ir/s/tehran/car"

# Number of scrolls
NUMBER_PAGE_SCROLL = 5

# How to store links
STORE_MODE = "database"  # choices: ["file", "database"]

# Set path of stored link file
PROJECT_DIR = str(Path(os.path.abspath(__file__)).parent.parent)
LINKS_FILE_PATH = os.path.join(PROJECT_DIR, "files")
