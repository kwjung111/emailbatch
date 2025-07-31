from batches.batch_base import AbstractBatch, BatchStatus
from batches.navicat_batch import NavicatBatch
from typing import Optional

#static class
class BatchFactory:
    def __new__(cls, *args, **kwargs):
        raise TypeError("This class cannot be instantiated.")
        
    @staticmethod
    def create_batch(job_name: str, status: str, timestamp : str) -> Optional[AbstractBatch]:
        batch_status = BatchStatus.from_str(status)
        if not batch_status:
            return None
        
        if job_name.upper() == "AUTOMATION":
            return NavicatBatch(batch_status,timestamp)
        
        return None