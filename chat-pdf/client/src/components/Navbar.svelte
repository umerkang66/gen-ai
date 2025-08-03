<script lang="ts">
	import AuthLinks from '$c/auth/AuthLinks.svelte';
	import { auth } from '$s/auth';

	$: user = $auth.user;
</script>

<header class="sticky top-0 z-50 backdrop-blur-md bg-white/80 border-b border-white/20 shadow-soft">
	<nav class="container mx-auto px-4 py-4 max-w-7xl">
		<div class="flex items-center justify-between">
			<!-- Logo/Brand -->
			<a href="/" class="flex items-center space-x-3 group">
				<div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-accent-500 rounded-xl flex items-center justify-center shadow-soft group-hover:shadow-medium transition-all duration-300">
					<span class="material-icons text-white text-xl">chat</span>
				</div>
				<div>
					<h1 class="text-xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
						ChatPDF
					</h1>
					<p class="text-xs text-secondary-500 -mt-1">AI Document Assistant</p>
				</div>
			</a>

			<!-- Navigation Links -->
			<div class="hidden md:flex items-center space-x-8">
				{#if user}
					<a
						href="/documents"
						class="text-secondary-600 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-2 group"
					>
						<span class="material-icons text-lg group-hover:scale-110 transition-transform duration-200">description</span>
						<span>Documents</span>
					</a>
					<a
						href="/scores"
						class="text-secondary-600 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-2 group"
					>
						<span class="material-icons text-lg group-hover:scale-110 transition-transform duration-200">analytics</span>
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
