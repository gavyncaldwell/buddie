import { join } from 'path';
import { skeleton } from '@skeletonlabs/tw-plugin';
import { fileURLToPath } from 'url';

/** @type {import('tailwindcss').Config} */
export default {
	darkMode: 'class',
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		// Add the skeleton paths for components
		join(
			fileURLToPath(import.meta.url),
			'..',
			'node_modules',
			'@skeletonlabs',
			'skeleton',
			'**',
			'*.{html,js,svelte,ts}'
		)
	],
	theme: {
		extend: {}
	},
	plugins: [
		skeleton({
			themes: { preset: ['skeleton'] }
		})
	]
};
