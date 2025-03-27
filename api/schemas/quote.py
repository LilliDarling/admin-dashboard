from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QuoteBase(BaseModel):
    text: str
    author: str
    category: str

class QuoteCreate(QuoteBase):
    pass

class QuoteUpdate(BaseModel):
    text: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None

class Quote(QuoteBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True