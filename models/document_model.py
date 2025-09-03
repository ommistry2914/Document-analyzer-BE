from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    filename: str
    filepath: str
    indexpath: str
    user_id: str
