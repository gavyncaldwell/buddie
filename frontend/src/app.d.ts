// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}

// Fix for deprecated TypeScript settings
export {};

declare module '@sveltejs/kit' {
	interface Config {
		compilerOptions?: {
			verbatimModuleSyntax?: boolean;
		};
	}
}
