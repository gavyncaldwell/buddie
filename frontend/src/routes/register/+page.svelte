<script>
	import { goto } from '$app/navigation';
	import { authStore } from '../../stores/authStore';

	let name = '';
	let email = '';
	let password = '';
	let confirmPassword = '';
	let error = '';
	let loading = false;

	async function handleSubmit() {
		// Validate inputs
		if (!name || !email || !password || !confirmPassword) {
			error = 'All fields are required.';
			return;
		}

		if (password !== confirmPassword) {
			error = 'Passwords do not match.';
			return;
		}

		try {
			loading = true;
			error = '';
			
			// This would be connected to the auth store in a real implementation
			// For now, just simulate registration
			
			// const result = await authStore.register({
			//     name,
			//     email,
			//     password
			// });
			
			// if (result.success) {
			//     goto('/');
			// } else {
			//     error = result.error;
			// }
			
			// Simulating successful registration
			setTimeout(() => {
				localStorage.setItem('token', 'fake-jwt-token');
				goto('/');
			}, 1000);
			
		} catch (err) {
			error = 'An error occurred. Please try again.';
			console.error('Registration error:', err);
		} finally {
			loading = false;
		}
	}
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="card p-6 w-full max-w-md">
		<h1 class="text-2xl font-bold mb-6 text-center">Create an Account</h1>
		
		{#if error}
			<div class="alert variant-filled-error mb-4">
				{error}
			</div>
		{/if}
		
		<form on:submit|preventDefault={handleSubmit}>
			<label class="label">
				<span>Name</span>
				<input
					class="input"
					type="text"
					bind:value={name}
					placeholder="Your Name"
					required
				/>
			</label>
			
			<label class="label mt-4">
				<span>Email</span>
				<input
					class="input"
					type="email"
					bind:value={email}
					placeholder="your@email.com"
					required
				/>
			</label>
			
			<label class="label mt-4">
				<span>Password</span>
				<input
					class="input"
					type="password"
					bind:value={password}
					placeholder="********"
					required
				/>
			</label>
			
			<label class="label mt-4">
				<span>Confirm Password</span>
				<input
					class="input"
					type="password"
					bind:value={confirmPassword}
					placeholder="********"
					required
				/>
			</label>
			
			<div class="flex justify-end mt-2">
				<a href="/login" class="text-sm">Already have an account? Login</a>
			</div>
			
			<button
				type="submit"
				class="btn variant-filled-primary w-full mt-6"
				disabled={loading}
			>
				{loading ? 'Creating Account...' : 'Register'}
			</button>
		</form>
	</div>
</div> 