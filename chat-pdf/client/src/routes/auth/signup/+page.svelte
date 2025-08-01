<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import TextInput from '$c/TextInput.svelte';
	import Button from '$c/Button.svelte';
	import { auth, signup, clearErrors } from '$s/auth';
	import Alert from '$c/Alert.svelte';

	let email = '';
	let password = '';
	let passwordConfirm = '';
	let loading = false;
	let passwordError = '';

	function validatePasswords() {
		if (password && passwordConfirm && password !== passwordConfirm) {
			passwordError = 'Passwords do not match';
			return false;
		}
		passwordError = '';
		return true;
	}

	async function handleSubmit() {
		if (!validatePasswords()) {
			return;
		}
		loading = true;
		await signup(email, password);
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
			<div class="w-20 h-20 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-3xl flex items-center justify-center mx-auto mb-6">
				<span class="material-icons text-white text-3xl">person_add</span>
			</div>
			<h1 class="text-3xl md:text-4xl font-display font-bold text-neutral-800 dark:text-white mb-2">
				Join ChatPDF
			</h1>
			<p class="text-lg text-neutral-600 dark:text-neutral-300">
				Create your account to get started
			</p>
		</div>

		<!-- Sign Up Form -->
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
							placeholder="Create a password"
							class="input-modern pl-10"
							on:input={validatePasswords}
						/>
					</div>
				</div>

				<!-- Confirm Password Input -->
				<div class="space-y-2">
					<label for="passwordConfirm" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300">
						Confirm Password
					</label>
					<div class="relative">
						<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
							<span class="material-icons text-neutral-400 text-lg">lock_reset</span>
						</div>
						<input
							id="passwordConfirm"
							bind:value={passwordConfirm}
							type="password"
							required
							placeholder="Confirm your password"
							class="input-modern pl-10"
							on:input={validatePasswords}
						/>
					</div>
					{#if passwordError}
						<p class="text-sm text-red-600 dark:text-red-400 flex items-center space-x-1">
							<span class="material-icons text-sm">error</span>
							<span>{passwordError}</span>
						</p>
					{/if}
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
					variant="secondary" 
					size="lg" 
					className="w-full"
					disabled={loading || !!passwordError}
				>
					{#if loading}
						<span class="material-icons animate-spin mr-2">refresh</span>
						Creating Account...
					{:else}
						<span class="material-icons mr-2">person_add</span>
						Create Account
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

			<!-- Sign In Link -->
			<div class="text-center">
				<p class="text-neutral-600 dark:text-neutral-400">
					Already have an account? 
					<a href="/auth/signin" class="text-secondary-600 hover:text-secondary-500 font-medium transition-colors duration-200">
						Sign in here
					</a>
				</p>
			</div>
		</div>

		<!-- Benefits -->
		<div class="mt-8 card p-6">
			<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-200 mb-4 text-center">
				Why Join ChatPDF?
			</h3>
			<div class="space-y-4">
				<div class="flex items-start space-x-3">
					<div class="w-6 h-6 bg-gradient-to-r from-primary-500 to-primary-600 rounded-lg flex items-center justify-center flex-shrink-0">
						<span class="material-icons text-white text-sm">upload_file</span>
					</div>
					<div>
						<h4 class="font-medium text-neutral-800 dark:text-neutral-200">Upload PDFs</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Upload and process your documents instantly</p>
					</div>
				</div>
				
				<div class="flex items-start space-x-3">
					<div class="w-6 h-6 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-lg flex items-center justify-center flex-shrink-0">
						<span class="material-icons text-white text-sm">chat</span>
					</div>
					<div>
						<h4 class="font-medium text-neutral-800 dark:text-neutral-200">AI Chat</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Ask questions and get intelligent responses</p>
					</div>
				</div>
				
				<div class="flex items-start space-x-3">
					<div class="w-6 h-6 bg-gradient-to-r from-accent-500 to-accent-600 rounded-lg flex items-center justify-center flex-shrink-0">
						<span class="material-icons text-white text-sm">insights</span>
					</div>
					<div>
						<h4 class="font-medium text-neutral-800 dark:text-neutral-200">Get Insights</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Extract key information from your documents</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
