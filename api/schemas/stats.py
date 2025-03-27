from pydantic import BaseModel

class DashboardStats(BaseModel):
    quote_api_requests: int
    blog_posts: int
    blog_views: int
    uptime: str

    class Config:
        from_attributes = True