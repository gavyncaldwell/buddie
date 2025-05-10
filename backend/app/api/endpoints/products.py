from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from ...models.database import get_session
from ...models.product import Product
from ...schemas.product import ProductCreate, ProductResponse
from ...auth.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
async def get_products(
    skip: int = 0,
    limit: int = 100,
    strain_type: Optional[str] = None,
    min_thc: Optional[float] = None,
    max_thc: Optional[float] = None,
    session: Session = Depends(get_session)
):
    """
    Get all products with optional filtering.
    """
    query = select(Product)
    
    # Apply filters if provided
    if strain_type:
        query = query.where(Product.strain_type == strain_type)
    if min_thc is not None:
        query = query.where(Product.thc_percentage >= min_thc)
    if max_thc is not None:
        query = query.where(Product.thc_percentage <= max_thc)
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    # Execute query
    products = session.exec(query).all()
    return products

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    """
    Get a specific product by ID.
    """
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return product

@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    """
    Create a new product (admin only).
    """
    # Check if user has admin privileges (to be implemented)
    
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/search/{query}")
async def search_products(
    query: str,
    session: Session = Depends(get_session)
):
    """
    Search for products by name or description.
    """
    products = session.exec(
        select(Product).where(
            (Product.name.contains(query)) | 
            (Product.description.contains(query))
        )
    ).all()
    return products 