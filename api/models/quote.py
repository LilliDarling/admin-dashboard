from odmantic import Model, Field
from datetime import datetime
from typing import Optional

class Quote(Model):
    text: str
    author: str
    category: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
    # New style for odmantic 1.0.2
    model_config = {
        "collection": "quotes"
    }