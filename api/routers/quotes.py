# from fastapi import APIRouter, Depends, HTTPException, status
# from typing import List
# from datetime import datetime
# from models.quote import Quote
# from schemas.quote import QuoteCreate, QuoteUpdate, Quote as QuoteSchema
# from auth.utils import get_current_active_user, TokenData
# from odmantic import AIOEngine
# from bson.objectid import ObjectId

# router = APIRouter(prefix="/quotes", tags=["Quotes"])

# @router.get("/", response_model=List[QuoteSchema])
# async def get_quotes(skip: int = 0, limit: int = 100, engine: AIOEngine = Depends(get_db)):
#     quotes = await engine.find(Quote, skip=skip, limit=limit)
#     return quotes

# @router.get("/{quote_id}", response_model=QuoteSchema)
# async def get_quote(quote_id: str, engine: AIOEngine = Depends(get_db)):
#     quote = await engine.find_one(Quote, Quote.id == ObjectId(quote_id))
#     if quote is None:
#         raise HTTPException(status_code=404, detail="Quote not found")
#     return quote

# @router.post("/", response_model=QuoteSchema, status_code=status.HTTP_201_CREATED)
# async def create_quote(
#     quote: QuoteCreate, 
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
#     db_quote = Quote(
#         **quote.model_dump(),
#         created_at=now,
#         updated_at=now
#     )
#     await engine.save(db_quote)
#     return db_quote

# @router.put("/{quote_id}", response_model=QuoteSchema)
# async def update_quote(
#     quote_id: str, 
#     quote: QuoteUpdate, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     db_quote = await engine.find_one(Quote, Quote.id == ObjectId(quote_id))
#     if db_quote is None:
#         raise HTTPException(status_code=404, detail="Quote not found")
    
#     # Update quote fields
#     quote_data = quote.model_dump(exclude_unset=True)
#     for key, value in quote_data.items():
#         setattr(db_quote, key, value)
    
#     db_quote.updated_at = datetime.utcnow()
#     await engine.save(db_quote)
#     return db_quote

# @router.delete("/{quote_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_quote(
#     quote_id: str, 
#     engine: AIOEngine = Depends(get_db),
#     current_user: TokenData = Depends(get_current_active_user)
# ):
#     # Check if user has admin role
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
    
#     db_quote = await engine.find_one(Quote, Quote.id == ObjectId(quote_id))
#     if db_quote is None:
#         raise HTTPException(status_code=404, detail="Quote not found")
    
#     await engine.delete(db_quote)
#     return None