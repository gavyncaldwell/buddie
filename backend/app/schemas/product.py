from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    brand: str
    strain_type: str
    thc_percentage: float
    cbd_percentage: float
    terpenes: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    dispensary: Optional[str] = None
    is_available: bool = True

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rating: int
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    product_id: int

class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime
    user_id: int
    product_id: int
    
    class Config:
        orm_mode = True 