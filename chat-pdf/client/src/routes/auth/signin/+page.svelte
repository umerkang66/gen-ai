<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import TextInput from '$c/TextInput.svelte';
	import Button from '$c/Button.svelte';
	import FormGroup from '$c/FormGroup.svelte';
	import { auth, signin, clearErrors } from '$s/auth';
	import Alert from '$c/Alert.svelte';

	let email = '';
	let password = '';
	let isLoading = false;

	async function handleSubmit() {
		isLoading = true;
		await signin(email, password);
		isLoading = false;
	}

	$: if ($auth.user) {
		goto('/');
	}

	beforeNavigate(clearErrors);
</script>

<div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
	<div class="max-w-md w-full space-y-8">
		<!-- Header -->
		<div class="text-center">
			<div class="w-20 h-20 bg-gradient-to-br from-primary-500 to-accent-500 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-large">
				<span class="material-icons text-white text-3xl">login</span>
			</div>
			<h1 class="text-3xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
				Welcome Back
			</h1>
			<p class="mt-2 text-secondary-600">
				Sign in to your account to continue
			</p>
		</div>

		<!-- Form Card -->
		<div class="glass-effect rounded-2xl p-8 shadow-large">
			<form on:submit|preventDefault={handleSubmit} class="space-y-6">
				<FormGroup label="Email Address" required>
					<TextInput 
						bind:value={email} 
						type="email" 
						placeholder="Enter your email"
						required
					/>
				</FormGroup>

				<FormGroup label="Password" required>
					<TextInput 
						bind:value={password} 
						type="password" 
						placeholder="Enter your password"
						required
					/>
				</FormGroup>

				{#if $auth.error}
					<Alert type="error">{$auth.error}</Alert>
				{/if}

				<Button 
					variant="primary" 
					size="lg" 
					className="w-full"
					disabled={isLoading}
				>
					{#if isLoading}
						<div class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin mr-2"></div>
					{:else}
						<span class="material-icons mr-2">login</span>
					{/if}
					Sign In
				</Button>
			</form>

			<!-- Divider -->
			<div class="relative my-6">
				<div class="absolute inset-0 flex items-center">
					<div class="w-full border-t border-secondary-200"></div>
				</div>
				<div class="relative flex justify-center text-sm">
					<span class="px-2 bg-white text-secondary-500">New to ChatPDF?</span>
				</div>
			</div>

			<!-- Sign Up Link -->
			<div class="text-center">
				<a 
					href="/auth/signup" 
					class="btn-secondary w-full flex items-center justify-center"
				>
					<span class="material-icons mr-2">person_add</span>
					Create Account
				</a>
			</div>
		</div>
	</div>
</div>
