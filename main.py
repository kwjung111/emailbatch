import re
from logger import get_logger
from merge import *
from config import *
from mail import poll_mail,send
from batches.batch_base import AbstractBatch

logger = get_logger(__name__)

if __name__ == '__main__':
        batches = poll_mail()
        for batch in batches:
                batch.run()
                send(f"batch finished",f"{batch.job_name} : {batch.status.value}")
                