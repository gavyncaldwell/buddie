<script>
	// Remove the Button import as it's not directly exported
	// import { Button } from '@skeletonlabs/skeleton';
	import { browser } from '$app/environment';
</script>

<div class="container mx-auto p-8">
	<h1 class="text-4xl font-bold mb-6">Welcome to Buddie</h1>
	<p class="mb-4">Your personal cannabis concierge app</p>

	{#if browser}
		<a href="/products" class="btn btn-primary mt-4">Explore Products</a>
	{:else}
		<a href="/products" class="mt-4 bg-primary-500 text-white py-2 px-4 rounded">
			Explore Products
		</a>
	{/if}
</div>
