# from fastapi import APIRouter, Depends, HTTPException, status
# from typing import List
# from datetime import datetime
# from database.database import get_db
# from models.post import Post, PostStatus
# from schemas.post import PostCreate, PostUpdate, Post as PostSchema
# from auth.utils import get_current_active_user, TokenData
# from odmantic import AIOEngine
# from bson.objectid import ObjectId

# router = APIRouter(prefix="/posts", tags=["Blog Posts"])

# @router.get("/", response_model=List[PostSchema])
# async def get_posts(skip: int = 0, limit: int = 100, engine: AIOEngine = Depends(get_db)):
#     posts = await engine.find(Post, skip=skip, limit=limit)
#     return posts

# @router.get("/{post_id}", response_model=PostSchema)
# async def get_post(post_id: str, engine: AIOEngine = Depends(get_db)):
#     post = await engine.find_one(Post, Post.id == ObjectId(post_id))
#     if post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return post

# @router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
# async def create_post(
#     post: PostCreate, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     now = datetime.utcnow()
#     db_post = Post(
#         **post.model_dump(),
#         created_at=now,
#         updated_at=now
#     )
#     await engine.save(db_post)
#     return db_post

# @router.put("/{post_id}", response_model=PostSchema)
# async def update_post(
#     post_id: str, 
#     post: PostUpdate, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     db_post = await engine.find_one(Post, Post.id == ObjectId(post_id))
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     # Update post fields
#     post_data = post.model_dump(exclude_unset=True)
#     for key, value in post_data.items():
#         setattr(db_post, key, value)
    
#     db_post.updated_at = datetime.utcnow()
#     await engine.save(db_post)
#     return db_post

# @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(
#     post_id: str, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     db_post = await engine.find_one(Post, Post.id == ObjectId(post_id))
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     await engine.delete(db_post)
#     return None

# @router.patch("/{post_id}/publish", response_model=PostSchema)
# async def publish_post(
#     post_id: str, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     db_post = await engine.find_one(Post, Post.id == ObjectId(post_id))
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     # Update post status to published
#     db_post.status = PostStatus.PUBLISHED
#     db_post.published_at = datetime.utcnow()
#     db_post.updated_at = datetime.utcnow()
    
#     await engine.save(db_post)
#     return db_post