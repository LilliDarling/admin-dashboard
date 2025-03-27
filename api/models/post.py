from odmantic import Model, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class PostStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

class Post(Model):
    title: str
    excerpt: str
    content: str
    author: str
    status: PostStatus = PostStatus.DRAFT
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    
    model_config = {
        "collection": "posts"
    }