<script lang="ts">
	import { onMount } from 'svelte';
	import { goto, beforeNavigate } from '$app/navigation';
	import { signout, clearErrors } from '$s/auth';

	let timeout: number | null = null;

	onMount(async () => {
		await signout();

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

<div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
	<div class="max-w-md w-full space-y-8">
		<!-- Header -->
		<div class="text-center">
			<div class="w-20 h-20 bg-gradient-to-br from-secondary-500 to-secondary-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-large">
				<span class="material-icons text-white text-3xl">logout</span>
			</div>
			<h1 class="text-3xl font-bold bg-gradient-to-r from-secondary-600 to-secondary-700 bg-clip-text text-transparent">
				See You Soon!
			</h1>
			<p class="mt-2 text-secondary-600">
				You have been successfully signed out
			</p>
		</div>

		<!-- Status Card -->
		<div class="glass-effect rounded-2xl p-8 shadow-large text-center">
			<div class="space-y-4">
				<div class="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center mx-auto shadow-soft">
					<span class="material-icons text-white text-2xl">check_circle</span>
				</div>
				<h2 class="text-xl font-semibold text-secondary-800">Successfully Signed Out</h2>
				<p class="text-secondary-500">Thank you for using ChatPDF</p>
			</div>

			<!-- Loading Animation -->
			<div class="mt-8 space-y-3">
				<div class="flex items-center justify-center space-x-2">
					<div class="w-2 h-2 bg-primary-500 rounded-full animate-pulse"></div>
					<div class="w-2 h-2 bg-primary-500 rounded-full animate-pulse" style="animation-delay: 0.2s"></div>
					<div class="w-2 h-2 bg-primary-500 rounded-full animate-pulse" style="animation-delay: 0.4s"></div>
				</div>
				<p class="text-sm text-secondary-500">Redirecting to home page...</p>
			</div>
		</div>

		<!-- Manual Redirect -->
		<div class="text-center">
			<a 
				href="/" 
				class="btn-primary"
			>
				<span class="material-icons mr-2">home</span>
				Go Home Now
			</a>
		</div>
	</div>
</div>
