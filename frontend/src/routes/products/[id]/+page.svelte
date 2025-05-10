<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	
	// Get the product ID from the URL params
	const productId = $page.params.id;
	
	let product = null;
	let loading = true;
	let error = null;
	
	// Placeholder function for submitting a review
	function submitReview() {
		alert('This feature would submit a review in the real app');
	}
	
	// Placeholder function for adding to favorites
	function toggleFavorite() {
		alert('This feature would add/remove from favorites in the real app');
	}
	
	onMount(async () => {
		try {
			loading = true;
			
			// This would be replaced with an actual API call
			// const response = await fetch(`/api/products/${productId}`);
			// product = await response.json();
			
			// Simulate API call with mock data
			setTimeout(() => {
				product = {
					id: productId,
					name: 'Blue Dream',
					strain_type: 'Hybrid',
					thc_percentage: 18.5,
					cbd_percentage: 0.2,
					terpenes: 'Myrcene, Pinene, Caryophyllene',
					description: 'A sweet berry aroma with effects that balance full-body relaxation with gentle cerebral invigoration. Blue Dream is a popular daytime medicine for treating pain, depression, and nausea.',
					price: 45.99,
					image_url: 'https://via.placeholder.com/400',
					brand: 'Canopy Growth',
					dispensary: 'Herbology',
					reviews: [
						{
							id: 1,
							user: 'JaneDoe',
							rating: 5,
							review_text: 'This is my go-to strain for creativity and relaxation without feeling too sleepy.',
							created_at: '2023-05-15'
						},
						{
							id: 2,
							user: 'CannabisConnoisseur',
							rating: 4,
							review_text: 'Great flavor profile and smooth smoke. Effects are balanced and not too overwhelming.',
							created_at: '2023-06-20'
						}
					]
				};
				loading = false;
			}, 500);
			
		} catch (err) {
			error = 'Failed to load product details';
			console.error('Error loading product:', err);
			loading = false;
		}
	});
</script>

<div class="container mx-auto p-4">
	{#if loading}
		<div class="flex justify-center p-12">
			<p>Loading product details...</p>
		</div>
	{:else if error}
		<div class="alert variant-filled-error">
			{error}
		</div>
	{:else if product}
		<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
			<!-- Product Image -->
			<div>
				<img 
					src={product.image_url} 
					alt={product.name} 
					class="w-full rounded-lg shadow-lg object-cover"
				/>
			</div>
			
			<!-- Product Details -->
			<div>
				<div class="flex justify-between items-start">
					<h1 class="text-3xl font-bold">{product.name}</h1>
					<button 
						class="btn-icon variant-ghost-tertiary" 
						on:click={toggleFavorite}
					>
						❤
					</button>
				</div>
				
				<div class="badge variant-filled-primary my-2">{product.strain_type}</div>
				
				<p class="text-xl font-bold mt-2">${product.price}</p>
				
				<div class="grid grid-cols-2 gap-4 my-4">
					<div class="card p-3">
						<span class="text-sm">THC</span>
						<p class="font-bold">{product.thc_percentage}%</p>
					</div>
					<div class="card p-3">
						<span class="text-sm">CBD</span>
						<p class="font-bold">{product.cbd_percentage}%</p>
					</div>
				</div>
				
				{#if product.terpenes}
					<div class="my-4">
						<h3 class="font-semibold">Terpenes</h3>
						<p>{product.terpenes}</p>
					</div>
				{/if}
				
				<div class="my-4">
					<h3 class="font-semibold">Description</h3>
					<p>{product.description}</p>
				</div>
				
				<div class="my-4">
					<p class="text-sm">Brand: {product.brand}</p>
					{#if product.dispensary}
						<p class="text-sm">Available at: {product.dispensary}</p>
					{/if}
				</div>
				
				<button class="btn variant-filled-secondary w-full my-4">
					Add to Cart
				</button>
			</div>
		</div>
		
		<!-- Reviews Section -->
		<div class="mt-12">
			<h2 class="text-2xl font-bold mb-4">Reviews</h2>
			
			{#if product.reviews && product.reviews.length > 0}
				<div class="grid grid-cols-1 gap-4">
					{#each product.reviews as review}
						<div class="card p-4">
							<div class="flex justify-between items-center">
								<span class="font-semibold">{review.user}</span>
								<span class="text-sm">{review.created_at}</span>
							</div>
							<div class="flex my-2">
								{#each Array(review.rating) as _, i}
									<span class="text-yellow-500">★</span>
								{/each}
								{#each Array(5 - review.rating) as _, i}
									<span class="text-gray-300">★</span>
								{/each}
							</div>
							<p>{review.review_text}</p>
						</div>
					{/each}
				</div>
			{:else}
				<p>No reviews yet. Be the first to review this product!</p>
			{/if}
			
			<!-- Add Review Form -->
			<div class="card p-4 mt-8">
				<h3 class="text-xl font-semibold mb-4">Write a Review</h3>
				
				<form on:submit|preventDefault={submitReview}>
					<label class="label">
						<span>Rating</span>
						<select class="select">
							<option value="5">5 Stars - Excellent</option>
							<option value="4">4 Stars - Very Good</option>
							<option value="3">3 Stars - Good</option>
							<option value="2">2 Stars - Fair</option>
							<option value="1">1 Star - Poor</option>
						</select>
					</label>
					
					<label class="label mt-4">
						<span>Your Review</span>
						<textarea
							class="textarea"
							rows="4"
							placeholder="Share your experience with this product..."
						></textarea>
					</label>
					
					<button type="submit" class="btn variant-filled-primary mt-4">
						Submit Review
					</button>
				</form>
			</div>
		</div>
	{:else}
		<p>Product not found</p>
	{/if}
</div> 