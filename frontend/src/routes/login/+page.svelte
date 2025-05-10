<script>
	import { goto } from '$app/navigation';

	let email = '';
	let password = '';
	let error = '';
	let loading = false;

	async function handleSubmit() {
		if (!email || !password) {
			error = 'Please enter both email and password.';
			return;
		}

		try {
			loading = true;
			error = '';
			
			// This would be replaced with an actual API call
			// const response = await fetch('/api/auth/login', {
			//     method: 'POST',
			//     headers: { 'Content-Type': 'application/json' },
			//     body: JSON.stringify({ email, password })
			// });
			
			// if (response.ok) {
			//     const data = await response.json();
			//     localStorage.setItem('token', data.token);
			//     goto('/');
			// } else {
			//     const data = await response.json();
			//     error = data.detail || 'Login failed. Please try again.';
			// }
			
			// Simulating successful login for now
			setTimeout(() => {
				localStorage.setItem('token', 'fake-jwt-token');
				goto('/');
			}, 1000);
			
		} catch (err) {
			error = 'An error occurred. Please try again.';
			console.error('Login error:', err);
		} finally {
			loading = false;
		}
	}
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="card p-6 w-full max-w-md">
		<h1 class="text-2xl font-bold mb-6 text-center">Login to Buddie</h1>
		
		{#if error}
			<div class="alert variant-filled-error mb-4">
				{error}
			</div>
		{/if}
		
		<form on:submit|preventDefault={handleSubmit}>
			<label class="label">
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
			
			<div class="flex justify-between items-center mt-2">
				<a href="/forgot-password" class="text-sm">Forgot password?</a>
				<a href="/register" class="text-sm">Create account</a>
			</div>
			
			<button
				type="submit"
				class="btn variant-filled-primary w-full mt-6"
				disabled={loading}
			>
				{loading ? 'Logging in...' : 'Login'}
			</button>
		</form>
	</div>
</div> 