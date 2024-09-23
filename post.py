from typing import Optional, List
from datetime import datetime

from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel


class Post(BaseModel):
    # id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    tags: Optional[List[str]] = []
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None