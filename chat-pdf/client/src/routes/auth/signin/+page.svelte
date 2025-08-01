<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import TextInput from '$c/TextInput.svelte';
	import Button from '$c/Button.svelte';
	import { auth, signin, clearErrors } from '$s/auth';
	import Alert from '$c/Alert.svelte';

	let email = '';
	let password = '';
	let loading = false;

	async function handleSubmit() {
		loading = true;
		await signin(email, password);
		loading = false;
	}

	$: if ($auth.user) {
		goto('/');
	}

	beforeNavigate(clearErrors);
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 via-white to-neutral-100 dark:from-neutral-900 dark:via-neutral-800 dark:to-neutral-900 flex items-center justify-center py-8">
	<div class="w-full max-w-md mx-auto px-4">
		<!-- Header -->
		<div class="text-center mb-8 animate-fade-in">
			<div class="w-20 h-20 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-3xl flex items-center justify-center mx-auto mb-6">
				<span class="material-icons text-white text-3xl">login</span>
			</div>
			<h1 class="text-3xl md:text-4xl font-display font-bold text-neutral-800 dark:text-white mb-2">
				Welcome Back
			</h1>
			<p class="text-lg text-neutral-600 dark:text-neutral-300">
				Sign in to your account to continue
			</p>
		</div>

		<!-- Sign In Form -->
		<div class="card p-8 animate-slide-up">
			<form on:submit|preventDefault={handleSubmit} class="space-y-6">
				<!-- Email Input -->
				<div class="space-y-2">
					<label for="email" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300">
						Email Address
					</label>
					<div class="relative">
						<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
							<span class="material-icons text-neutral-400 text-lg">email</span>
						</div>
						<input
							id="email"
							bind:value={email}
							type="email"
							required
							placeholder="Enter your email"
							class="input-modern pl-10"
						/>
					</div>
				</div>

				<!-- Password Input -->
				<div class="space-y-2">
					<label for="password" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300">
						Password
					</label>
					<div class="relative">
						<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
							<span class="material-icons text-neutral-400 text-lg">lock</span>
						</div>
						<input
							id="password"
							bind:value={password}
							type="password"
							required
							placeholder="Enter your password"
							class="input-modern pl-10"
						/>
					</div>
				</div>

				<!-- Error Display -->
				{#if $auth.error}
					<Alert type="error">
						<div class="flex items-center space-x-2">
							<span class="material-icons">error</span>
							<span>{$auth.error}</span>
						</div>
					</Alert>
				{/if}

				<!-- Submit Button -->
				<Button 
					variant="primary" 
					size="lg" 
					className="w-full"
					disabled={loading}
				>
					{#if loading}
						<span class="material-icons animate-spin mr-2">refresh</span>
						Signing In...
					{:else}
						<span class="material-icons mr-2">login</span>
						Sign In
					{/if}
				</Button>
			</form>

			<!-- Divider -->
			<div class="relative my-8">
				<div class="absolute inset-0 flex items-center">
					<div class="w-full border-t border-neutral-200 dark:border-neutral-700"></div>
				</div>
				<div class="relative flex justify-center text-sm">
					<span class="px-2 bg-white dark:bg-neutral-800 text-neutral-500">or</span>
				</div>
			</div>

			<!-- Sign Up Link -->
			<div class="text-center">
				<p class="text-neutral-600 dark:text-neutral-400">
					Don't have an account? 
					<a href="/auth/signup" class="text-primary-600 hover:text-primary-500 font-medium transition-colors duration-200">
						Sign up here
					</a>
				</p>
			</div>
		</div>

		<!-- Features -->
		<div class="mt-8 grid grid-cols-3 gap-4">
			<div class="text-center space-y-2">
				<div class="w-8 h-8 bg-gradient-to-r from-primary-500 to-primary-600 rounded-lg flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-sm">security</span>
				</div>
				<p class="text-xs text-neutral-600 dark:text-neutral-400">Secure</p>
			</div>
			
			<div class="text-center space-y-2">
				<div class="w-8 h-8 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-lg flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-sm">speed</span>
				</div>
				<p class="text-xs text-neutral-600 dark:text-neutral-400">Fast</p>
			</div>
			
			<div class="text-center space-y-2">
				<div class="w-8 h-8 bg-gradient-to-r from-accent-500 to-accent-600 rounded-lg flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-sm">verified</span>
				</div>
				<p class="text-xs text-neutral-600 dark:text-neutral-400">Reliable</p>
			</div>
		</div>
	</div>
</div>
