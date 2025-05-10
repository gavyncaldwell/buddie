from typing import List, Dict, Any
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from collections import defaultdict

# This is a simplified recommendation system
# In a real production environment, this would be more sophisticated

def get_recommendations(user_id: int, user_reviews: List, user_favorites: List) -> List[int]:
    """
    Generate product recommendations for a user based on their reviews and favorites.
    This is a placeholder for a more sophisticated recommendation engine.
    
    Args:
        user_id: The ID of the user
        user_reviews: List of user reviews
        user_favorites: List of user favorites
        
    Returns:
        List of recommended product IDs
    """
    # In a real implementation, we would:
    # 1. Extract features from products (strain, THC/CBD levels, terpenes)
    # 2. Build user preference profile based on highly-rated products
    # 3. Find products similar to ones the user likes
    # 4. Recommend new products based on similarity
    
    # This is a dummy implementation that would be replaced with a real one
    product_ids_from_reviews = [review.product_id for review in user_reviews]
    product_ids_from_favorites = [fav.product_id for fav in user_favorites]
    
    # Combine and deduplicate
    liked_product_ids = list(set(product_ids_from_reviews + product_ids_from_favorites))
    
    # In a real implementation, we'd return similar products to these
    # For now, we'll return a dummy list
    return liked_product_ids[:10]

def calculate_product_similarity(products):
    """
    Calculate similarity between products based on their features.
    This would be part of a more sophisticated recommendation system.
    """
    # Extract features for each product
    features = []
    for product in products:
        # Example features - in a real system, we'd have more
        thc = product.thc_percentage / 100.0
        cbd = product.cbd_percentage / 100.0
        
        # One-hot encode strain type
        is_indica = 1 if product.strain_type.lower() == 'indica' else 0
        is_sativa = 1 if product.strain_type.lower() == 'sativa' else 0
        is_hybrid = 1 if product.strain_type.lower() == 'hybrid' else 0
        
        features.append([thc, cbd, is_indica, is_sativa, is_hybrid])
    
    # Convert to numpy array
    features_array = np.array(features)
    
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(features_array)
    
    return similarity_matrix 