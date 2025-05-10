<script>
	import { AppBar } from '@skeletonlabs/skeleton';
</script>

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