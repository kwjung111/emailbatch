import os
from batches.batch_base import *
from config import *
from merge import merge_excels_preserve,delete_all_file
from api_client import upload_file

class NavicatBatch(AbstractBatch):
    def __init__(self,status: BatchStatus, timestamp: str):
        super().__init__(job_name="automation",
                         status=status,
                         timestamp=timestamp)
    
    def validate(self) -> bool:
        return True
    
    def run(self,*args,**kwargs):
        file = pattern = os.path.join(OUTPUT_DIR, "navicat_merged.xlsx")
        merge_excels_preserve(INPUT_DIR,OUTPUT_DIR)
        delete_all_file(INPUT_DIR)
        if not upload_file(file):
            self.set_status_to_fail()
  