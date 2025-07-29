import re
from logger import get_logger
from merge import *
from config import *
from mail import *
from api_client import upload_file

logger = get_logger(__name__)

if __name__ == '__main__':
        if poll_mail():
                file = pattern = os.path.join(OUTPUT_DIR, "merged.xlsx")
                upload_file(file)