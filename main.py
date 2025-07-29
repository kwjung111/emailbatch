import re
from logger import get_logger
from merge import *
from config import *
from mail import poll_mail,send
from api_client import upload_file

logger = get_logger(__name__)

if __name__ == '__main__':
        batch_info = poll_mail()
        if batch_info:
                file = pattern = os.path.join(OUTPUT_DIR, "merged.xlsx")
                merge_excels_preserve(INPUT_DIR,OUTPUT_DIR)
                delete_all_file(INPUT_DIR)
                if not upload_file(file):
                        batch_info.set_status_to_fail()
                send(f"batch finished",{batch_info.status})
                