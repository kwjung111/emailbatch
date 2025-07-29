from dataclasses import dataclass
from enum import Enum
from typing import Optional
from config import *

class BatchStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    NA = "N/A"

    @classmethod
    def from_str(cls, value: str) -> Optional["BatchStatus"]:
        normalized = value.strip().upper()
        return _alias_map.get(normalized)

_alias_map = {
    "SUCCESSFULLY": BatchStatus.SUCCESS,
    "UNSUCCESSFULLY": BatchStatus.FAIL
}
    
    
@dataclass(frozen=True)
class BatchInfo:
    job_name: str
    status: BatchStatus
    timestamp : str
    
    def check(self) -> bool:
        if self.job_name != JOB_NAME:
            return False
        if self.status != BatchStatus.SUCCESS:
            return False
        
        return True
    
    def __str__(self):
        return f"[{self.job_name}],[{self.status.value}],[{self.timestamp}]"