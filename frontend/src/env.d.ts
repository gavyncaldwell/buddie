import 'svelte';
import 'vite/client';

// This is a workaround for SvelteKit's TypeScript configuration issues
// with importsNotUsedAsValues and preserveValueImports
declare module '*.svelte' {
	import type { ComponentType } from 'svelte';
	const component: ComponentType;
	export default component;
}
