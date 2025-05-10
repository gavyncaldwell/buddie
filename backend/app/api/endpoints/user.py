from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from ...models.database import get_session
from ...models.user import User
from ...models.product import Review, Favorite
from ...schemas.user import UserResponse
from ...schemas.product import ReviewCreate, ReviewResponse
from ...auth.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """
    Get information about the currently authenticated user.
    """
    return current_user

@router.post("/reviews", response_model=ReviewResponse)
async def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Create a product review.
    """
    # Create new review
    db_review = Review(
        rating=review.rating,
        review_text=review.review_text,
        user_id=current_user.id,
        product_id=review.product_id
    )
    
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

@router.get("/reviews", response_model=List[ReviewResponse])
async def get_my_reviews(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Get all reviews for the current user.
    """
    return session.exec(
        select(Review).where(Review.user_id == current_user.id)
    ).all()

@router.post("/favorites/{product_id}")
async def add_favorite(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Add a product to favorites.
    """
    # Check if already favorited
    existing = session.exec(
        select(Favorite).where(
            Favorite.user_id == current_user.id,
            Favorite.product_id == product_id
        )
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already in favorites"
        )
    
    # Add favorite
    favorite = Favorite(user_id=current_user.id, product_id=product_id)
    session.add(favorite)
    session.commit()
    
    return {"message": "Product added to favorites"}

@router.delete("/favorites/{product_id}")
async def remove_favorite(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Remove a product from favorites.
    """
    favorite = session.exec(
        select(Favorite).where(
            Favorite.user_id == current_user.id,
            Favorite.product_id == product_id
        )
    ).first()
    
    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found in favorites"
        )
    
    session.delete(favorite)
    session.commit()
    
    return {"message": "Product removed from favorites"} 