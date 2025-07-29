import os
import requests
from config import *
from logger import get_logger

logger = get_logger(__name__)

def upload_file(filepath):
    url = UPLOAD_URL

    try:
        with open(filepath, 'rb') as f:
            files = {'file_dict_vendor': f}
            logger.info(f"Upload Start")
            response = requests.post(url,files=files)
            

        if response.status_code == 200:
            logger.info(f"Upload Success. Response Code : {response.status_code}, Text : {response.text}")
            return True
        else:
            logger.info(f"Upload Failed. Response Code : {response.status_code}, Text : {response.text}")
            return False
    
    except requests.exceptions.RequestException as e:
        logger.exception(f"Error occured : {e}")
        return False