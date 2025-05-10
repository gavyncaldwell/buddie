<script>
	import { AppBar } from '@skeletonlabs/skeleton';
	import { browser } from '$app/environment';
</script>

{#if browser}
	<AppBar>
		<svelte:fragment slot="lead">
			<strong class="text-xl uppercase">Buddie</strong>
		</svelte:fragment>
		<svelte:fragment slot="trail">
			<a class="btn btn-sm variant-ghost-surface" href="/products">Products</a>
			<a class="btn btn-sm variant-ghost-surface" href="/profile">Profile</a>
			<a class="btn btn-sm variant-ghost-surface" href="/login">Login</a>
		</svelte:fragment>
	</AppBar>
{:else}
	<header class="bg-surface-900 p-4 flex justify-between items-center">
		<div>
			<strong class="text-xl uppercase">Buddie</strong>
		</div>
		<div class="flex gap-4">
			<a class="text-sm" href="/products">Products</a>
			<a class="text-sm" href="/profile">Profile</a>
			<a class="text-sm" href="/login">Login</a>
		</div>
	</header>
{/if}
