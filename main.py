import re
from logger import get_logger
from merge import *
from config import *
from mail import *

logger = get_logger(__name__)

if __name__ == '__main__':
        poll_mail()