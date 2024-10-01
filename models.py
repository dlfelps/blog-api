from pydantic import BaseModel

from datetime import datetime


class Post(BaseModel):
    id: int | None = None    
    title: str | None = None 
    content: str | None = None
    category: str| None = None
    tags: list[str] = []
    createdAt: datetime | None = None
    updatedAt: datetime | None = None