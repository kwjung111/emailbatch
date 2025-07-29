import os
import requests
from config import *
from logger import get_logger

logger = get_logger(__name__)

def upload_file(filepath):
    url = UPLOAD_URL

    with open(filepath, 'rb') as f:
        files = {'file_dict_vendor': f}
        response = requests.post(url,files=files)
        
    logger.log(f"Response Code : {response.status_code}, Text : {response.text}")