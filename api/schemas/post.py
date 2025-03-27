from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class PostStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

class PostBase(BaseModel):
    title: str
    excerpt: str
    content: str
    author: str

class PostCreate(PostBase):
    status: PostStatus = PostStatus.DRAFT

class PostUpdate(BaseModel):
    title: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    status: Optional[PostStatus] = None

class Post(PostBase):
    id: str
    status: PostStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None

    class Config:
        from_attributes = True