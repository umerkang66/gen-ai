<script lang="ts">
	import AuthLinks from '$c/auth/AuthLinks.svelte';
	import { auth } from '$s/auth';

	$: user = $auth.user;
</script>

<header class="sticky top-0 z-50 glass-effect border-b border-white/20 dark:border-neutral-700/20">
	<nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
		<div class="flex justify-between items-center h-16">
			<!-- Logo/Brand -->
			<a href="/" class="flex items-center space-x-3 group">
				<div class="w-10 h-10 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center shadow-lg">
					<span class="text-white font-bold text-lg">CP</span>
				</div>
				<span class="text-2xl font-display font-bold text-neutral-800 dark:text-white">
					Chat<span class="gradient-text">PDF</span>
				</span>
			</a>

			<!-- Navigation Links -->
			<div class="hidden md:flex items-center space-x-8">
				{#if user}
					<a
						href="/documents"
						class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-primary-400 font-medium transition-all duration-200 flex items-center space-x-2 px-4 py-2 rounded-lg hover:bg-white/50 dark:hover:bg-neutral-800/50"
					>
						<span class="material-icons text-lg">description</span>
						<span>Documents</span>
					</a>
					<a
						href="/scores"
						class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-primary-400 font-medium transition-all duration-200 flex items-center space-x-2 px-4 py-2 rounded-lg hover:bg-white/50 dark:hover:bg-neutral-800/50"
					>
						<span class="material-icons text-lg">analytics</span>
						<span>Scores</span>
					</a>
				{/if}
			</div>

			<!-- Auth Links -->
			<div class="flex items-center space-x-4">
				<AuthLinks />
			</div>
		</div>
	</nav>
</header>
