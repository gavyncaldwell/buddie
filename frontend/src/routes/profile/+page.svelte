<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	
	let user = null;
	let favorites = [];
	let reviews = [];
	let loading = true;
	
	onMount(async () => {
		// Check if user is logged in
		const token = localStorage.getItem('token');
		if (!token) {
			goto('/login');
			return;
		}
		
		try {
			loading = true;
			
			// This would be replaced with actual API calls
			// const userResponse = await fetch('/api/users/me');
			// user = await userResponse.json();
			
			// const favoritesResponse = await fetch('/api/users/me/favorites');
			// favorites = await favoritesResponse.json();
			
			// const reviewsResponse = await fetch('/api/users/me/reviews');
			// reviews = await reviewsResponse.json();
			
			// Mock data for development
			setTimeout(() => {
				user = {
					id: 1,
					name: 'John Doe',
					email: 'john@example.com',
					created_at: '2023-01-15'
				};
				
				favorites = [
					{
						id: 1,
						name: 'Blue Dream',
						strain_type: 'Hybrid',
						thc_percentage: 18.5,
						image_url: 'https://via.placeholder.com/100'
					},
					{
						id: 2,
						name: 'OG Kush',
						strain_type: 'Indica',
						thc_percentage: 23.0,
						image_url: 'https://via.placeholder.com/100'
					}
				];
				
				reviews = [
					{
						id: 1,
						product: {
							id: 1,
							name: 'Blue Dream',
							image_url: 'https://via.placeholder.com/100'
						},
						rating: 5,
						review_text: 'This is my go-to strain for creativity and relaxation without feeling too sleepy.',
						created_at: '2023-05-15'
					},
					{
						id: 2,
						product: {
							id: 3,
							name: 'Sour Diesel',
							image_url: 'https://via.placeholder.com/100'
						},
						rating: 4,
						review_text: 'Great for daytime use. Helps with focus and productivity.',
						created_at: '2023-06-20'
					}
				];
				
				loading = false;
			}, 800);
			
		} catch (error) {
			console.error('Error loading profile:', error);
			loading = false;
		}
	});
	
	function logout() {
		localStorage.removeItem('token');
		goto('/login');
	}
</script>

<div class="container mx-auto p-4">
	<h1 class="text-3xl font-bold mb-6">Your Profile</h1>
	
	{#if loading}
		<div class="flex justify-center p-12">
			<p>Loading profile...</p>
		</div>
	{:else if user}
		<!-- User Info -->
		<div class="card p-6 mb-8">
			<div class="flex flex-col md:flex-row justify-between">
				<div>
					<h2 class="text-2xl font-semibold">{user.name}</h2>
					<p class="text-sm mt-1">{user.email}</p>
					<p class="text-xs mt-1">Member since {new Date(user.created_at).toLocaleDateString()}</p>
				</div>
				
				<div class="mt-4 md:mt-0">
					<button class="btn variant-ghost-error" on:click={logout}>
						Logout
					</button>
				</div>
			</div>
		</div>
		
		<!-- Tabs for different sections -->
		<div class="tab-container">
			<ul class="tabs">
				<li class="tab tab-active" data-active="true">Favorites</li>
				<li class="tab">Reviews</li>
				<li class="tab">Order History</li>
			</ul>
			
			<!-- Favorites Section -->
			<div class="tab-panel">
				<h2 class="text-xl font-semibold mb-4">Your Favorites</h2>
				
				{#if favorites.length === 0}
					<p>You haven't added any favorites yet.</p>
				{:else}
					<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
						{#each favorites as product}
							<a href={`/products/${product.id}`} class="card p-4 flex gap-4 hover:bg-surface-hover-token">
								<img 
									src={product.image_url} 
									alt={product.name} 
									class="w-16 h-16 object-cover rounded"
								/>
								<div>
									<h3 class="font-semibold">{product.name}</h3>
									<div class="badge variant-filled-primary my-1">{product.strain_type}</div>
									<p class="text-sm">THC: {product.thc_percentage}%</p>
								</div>
							</a>
						{/each}
					</div>
				{/if}
			</div>
			
			<!-- Reviews Section -->
			<div class="tab-panel hidden">
				<h2 class="text-xl font-semibold mb-4">Your Reviews</h2>
				
				{#if reviews.length === 0}
					<p>You haven't written any reviews yet.</p>
				{:else}
					<div class="space-y-4">
						{#each reviews as review}
							<div class="card p-4">
								<div class="flex items-start gap-4">
									<img 
										src={review.product.image_url} 
										alt={review.product.name} 
										class="w-16 h-16 object-cover rounded"
									/>
									<div class="flex-1">
										<div class="flex justify-between items-start">
											<a href={`/products/${review.product.id}`} class="font-semibold hover:underline">
												{review.product.name}
											</a>
											<span class="text-xs">{new Date(review.created_at).toLocaleDateString()}</span>
										</div>
										
										<div class="flex my-1">
											{#each Array(review.rating) as _, i}
												<span class="text-yellow-500">★</span>
											{/each}
											{#each Array(5 - review.rating) as _, i}
												<span class="text-gray-300">★</span>
											{/each}
										</div>
										
										<p class="text-sm mt-2">{review.review_text}</p>
									</div>
								</div>
							</div>
						{/each}
					</div>
				{/if}
			</div>
			
			<!-- Order History Section -->
			<div class="tab-panel hidden">
				<h2 class="text-xl font-semibold mb-4">Order History</h2>
				<p>Your order history will appear here.</p>
			</div>
		</div>
	{:else}
		<div class="card p-6">
			<p>Please log in to view your profile</p>
			<a href="/login" class="btn variant-filled-primary mt-4">Login</a>
		</div>
	{/if}
</div> 