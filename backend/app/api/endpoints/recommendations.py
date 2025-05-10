from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from ...models.database import get_session
from ...models.user import User
from ...models.product import Product, Review, Favorite
from ...schemas.product import ProductResponse
from ...auth.auth import get_current_user
from ...services.recommendation import get_recommendations

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
async def get_user_recommendations(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Get personalized product recommendations for the current user.
    """
    # Get user's reviews and favorites
    user_reviews = session.exec(
        select(Review).where(Review.user_id == current_user.id)
    ).all()
    
    user_favorites = session.exec(
        select(Favorite).where(Favorite.user_id == current_user.id)
    ).all()
    
    # If user has no reviews or favorites, return popular products
    if not user_reviews and not user_favorites:
        # Return top-rated products
        top_products = session.exec(
            select(Product)
            .join(Review)
            .group_by(Product.id)
            .order_by(Review.rating.desc())
            .limit(10)
        ).all()
        return top_products
    
    # Otherwise, get personalized recommendations
    # This would call the recommendation service
    recommended_product_ids = get_recommendations(
        user_id=current_user.id,
        user_reviews=user_reviews,
        user_favorites=user_favorites
    )
    
    # Fetch the recommended products
    recommended_products = session.exec(
        select(Product).where(Product.id.in_(recommended_product_ids))
    ).all()
    
    return recommended_products

@router.get("/similar/{product_id}", response_model=List[ProductResponse])
async def get_similar_products(
    product_id: int,
    session: Session = Depends(get_session)
):
    """
    Get products similar to the specified product.
    """
    # Get the product
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Find similar products based on strain type and THC/CBD content
    similar_products = session.exec(
        select(Product)
        .where(
            (Product.id != product_id) &
            (Product.strain_type == product.strain_type) &
            (Product.thc_percentage.between(
                product.thc_percentage * 0.8,
                product.thc_percentage * 1.2
            ))
        )
        .limit(10)
    ).all()
    
    return similar_products 