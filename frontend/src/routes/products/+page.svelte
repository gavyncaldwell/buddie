<script>
	import { onMount } from 'svelte';
	
	let products = [];
	let loading = true;
	
	onMount(async () => {
		try {
			// This would be replaced with an actual API call
			loading = true;
			// const response = await fetch('/api/products');
			// products = await response.json();
			
			// Placeholder data
			products = [
				{
					id: 1,
					name: 'Blue Dream',
					strain_type: 'Hybrid',
					thc_percentage: 18.5,
					cbd_percentage: 0.2,
					description: 'A sweet berry aroma with effects that balance full-body relaxation with gentle cerebral invigoration.',
					price: 45.99,
					image_url: 'https://via.placeholder.com/200'
				},
				{
					id: 2,
					name: 'OG Kush',
					strain_type: 'Indica',
					thc_percentage: 23.0,
					cbd_percentage: 0.3,
					description: 'An American marijuana classic with complex aroma and strong effects.',
					price: 52.99,
					image_url: 'https://via.placeholder.com/200'
				}
			];
		} catch (error) {
			console.error('Error fetching products:', error);
		} finally {
			loading = false;
		}
	});
</script>

<div class="container mx-auto p-4">
	<h1 class="text-3xl font-bold mb-6">Products</h1>
	
	{#if loading}
		<div class="flex justify-center">
			<p>Loading products...</p>
		</div>
	{:else if products.length === 0}
		<p>No products found.</p>
	{:else}
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each products as product}
				<div class="card p-4">
					<img src={product.image_url} alt={product.name} class="w-full h-48 object-cover mb-4 rounded" />
					<h2 class="text-xl font-semibold">{product.name}</h2>
					<div class="badge variant-filled-primary my-2">{product.strain_type}</div>
					<p class="text-sm mb-2">THC: {product.thc_percentage}% | CBD: {product.cbd_percentage}%</p>
					<p class="line-clamp-3 text-sm mb-4">{product.description}</p>
					<div class="flex justify-between items-center">
						<span class="text-lg font-bold">${product.price}</span>
						<button class="btn btn-sm variant-filled-secondary">Add to Cart</button>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div> 