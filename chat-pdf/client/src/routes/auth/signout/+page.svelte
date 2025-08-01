<script lang="ts">
	import { onMount } from 'svelte';
	import { goto, beforeNavigate } from '$app/navigation';
	import { signout, clearErrors } from '$s/auth';
	import Button from '$c/Button.svelte';

	let timeout: number | null = null;
	let progress = 0;

	onMount(async () => {
		await signout();

		// Animate progress bar
		const interval = setInterval(() => {
			progress += 2;
			if (progress >= 100) {
				clearInterval(interval);
				goto('/');
			}
		}, 50);

		timeout = setTimeout(() => {
			goto('/');
		}, 2500);
	});

	beforeNavigate(() => {
		clearErrors();
		if (timeout) {
			clearTimeout(timeout);
		}
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 via-white to-neutral-100 dark:from-neutral-900 dark:via-neutral-800 dark:to-neutral-900 flex items-center justify-center py-8">
	<div class="w-full max-w-md mx-auto px-4">
		<!-- Header -->
		<div class="text-center mb-8 animate-fade-in">
			<div class="w-20 h-20 bg-gradient-to-r from-neutral-500 to-neutral-600 rounded-3xl flex items-center justify-center mx-auto mb-6">
				<span class="material-icons text-white text-3xl">logout</span>
			</div>
			<h1 class="text-3xl md:text-4xl font-display font-bold text-neutral-800 dark:text-white mb-2">
				See You Soon!
			</h1>
			<p class="text-lg text-neutral-600 dark:text-neutral-300">
				You've been successfully signed out
			</p>
		</div>

		<!-- Sign Out Card -->
		<div class="card p-8 animate-slide-up">
			<div class="text-center space-y-6">
				<div class="w-16 h-16 bg-gradient-to-r from-green-500 to-green-600 rounded-2xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-2xl">check_circle</span>
				</div>
				
				<div>
					<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">
						Successfully Signed Out
					</h3>
					<p class="text-neutral-600 dark:text-neutral-400">
						Thank you for using ChatPDF. We hope to see you again soon!
					</p>
				</div>

				<!-- Progress Bar -->
				<div class="space-y-2">
					<div class="flex justify-between text-sm text-neutral-600 dark:text-neutral-400">
						<span>Redirecting...</span>
						<span>{Math.round(progress)}%</span>
					</div>
					<div class="w-full bg-neutral-200 dark:bg-neutral-700 rounded-full h-2">
						<div 
							class="bg-gradient-to-r from-primary-500 to-secondary-500 h-2 rounded-full transition-all duration-300"
							style="width: {progress}%"
						></div>
					</div>
				</div>

				<!-- Action Buttons -->
				<div class="flex space-x-3">
					<a href="/auth/signin" class="flex-1">
						<Button variant="primary" size="md" className="w-full">
							<span class="material-icons mr-2">login</span>
							Sign In Again
						</Button>
					</a>
					<a href="/" class="flex-1">
						<Button variant="outline" size="md" className="w-full">
							<span class="material-icons mr-2">home</span>
							Go Home
						</Button>
					</a>
				</div>
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
