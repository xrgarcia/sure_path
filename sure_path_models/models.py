from datetime import datetime
from pydantic import BaseModel



class ChangeRequest(BaseModel):
    request_number: str = None
    description: str = None
    backout_plan: str = None
    test_plan: str = None
    title: str = None
    start_time: datetime = None
    end_time: datetime = None
    requestor: str = None
    status: str = "Unknown"
