from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config.settings import APP_NAME, VERSION, AUTHOR
from utils.logger import logger


def display_message():
    logger.info("Application Started")
    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print("=" * 60)


if __name__ == "__main__":
    display_message()
