import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	// Fix for HMR with tailwind
	server: {
		fs: {
			allow: ['..']
		}
	},
	// Fix for Skeleton UI components during SSR
	ssr: {
		noExternal: ['@skeletonlabs/skeleton']
	}
});
