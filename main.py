import re
from logger import get_logger
from merge import *
from config import *
from mail import poll_mail,send
from api_client import upload_file

logger = get_logger(__name__)

if __name__ == '__main__':
        poll_result = poll_mail()
        if poll_result:
                file = pattern = os.path.join(OUTPUT_DIR, "merged.xlsx")
                merge_excels_preserve(INPUT_DIR,OUTPUT_DIR)
                if upload_file(file):
                        send(f"batch finished",{poll_result.status})