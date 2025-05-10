from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    brand: str
    strain_type: str  # Indica, Sativa, Hybrid
    thc_percentage: float
    cbd_percentage: float
    terpenes: Optional[str] = Field(default=None)
    price: float
    image_url: Optional[str] = Field(default=None)
    dispensary: Optional[str] = Field(default=None)
    is_available: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    reviews: List["Review"] = Relationship(back_populates="product")

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rating: int  # 1-5 stars
    review_text: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Foreign keys
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")
    
    # Relationships
    user: "User" = Relationship(back_populates="reviews")
    product: Product = Relationship(back_populates="reviews")

class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Foreign keys
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")
    
    # Relationships
    user: "User" = Relationship(back_populates="favorites")
    product: Product = Relationship() 