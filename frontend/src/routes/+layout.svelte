<script>
	import '../app.postcss';
	import { AppShell } from '@skeletonlabs/skeleton';
	import Header from '../components/Header.svelte';
	import { browser } from '$app/environment';
</script>

{#if browser}
	<!-- App Shell -->
	<AppShell>
		<svelte:fragment slot="header">
			<Header />
		</svelte:fragment>

		<div class="container mx-auto p-4">
			<slot />
		</div>
	</AppShell>
{:else}
	<!-- Fallback for SSR -->
	<div>
		<header>
			<Header />
		</header>

		<div class="container mx-auto p-4">
			<slot />
		</div>
	</div>
{/if}

<style>
	:global(html, body) {
		@apply h-full overflow-hidden;
	}
</style>
