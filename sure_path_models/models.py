from datetime import datetime
from pydantic import BaseModel



class ChangeRequest(BaseModel):
    request_number: str = None
    start_time: datetime = None
    end_time: datetime = None
    status: str = "Unknown"
