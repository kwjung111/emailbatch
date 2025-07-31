from enum import Enum
from typing import Optional
from abc import ABC,abstractmethod

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
        
class AbstractBatch(ABC):
    job_name:str
    status: BatchStatus
    timestamp:str

    def __init__(self,job_name,status,timestamp): 
        self.job_name = job_name
        self.status = status
        self.timestamp = timestamp        
        
    @abstractmethod
    def validate(self) -> bool:
        pass
    
    @abstractmethod
    def run(self,*args,**kwargs):
        pass
    
    def __str__(self) -> str:
        return f"[{self.job_name}],[{self.status.value}],[{self.timestamp}]"
    
    def set_status_to_fail(self):
        self.status = BatchStatus.FAIL
        
        
