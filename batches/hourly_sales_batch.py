import os
from batches.batch_base import *
from config import *
from api_client import upload_file

class HourlySalesBatch(AbstractBatch):
    def __init__(self,status: BatchStatus, timestamp: str):
        super().__init__(job_name="hourlysales",
                         status=status,
                         timestamp=timestamp)
    
    def validate(self) -> bool:
        return True
    
    def run(self,*args,**kwargs):
        file = pattern = os.path.join(OUTPUT_DIR, "hourly_sales_merged.xlsx")
        #if not upload_file(file):
        #    self.set_status_to_fail()
  