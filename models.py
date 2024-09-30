from pydantic import BaseModel

from datetime import datetime


class Post(BaseModel):
    id: int | None = None    
    title: str 
    content: str 
    category: str
    tags: list[str] = []
    createdAt: datetime | None = None
    updatedAt: datetime | None = None