<script lang="ts">
	import { auth } from '$s/auth';
	import Button from '$c/Button.svelte';
	
	$: user = $auth.user;
</script>

<div class="min-h-[80vh] flex items-center justify-center">
	<div class="text-center space-y-8 max-w-4xl mx-auto px-4">
		<!-- Hero Section -->
		<div class="space-y-6 animate-fade-in">
			<div class="relative">
				<div class="absolute inset-0 bg-gradient-to-r from-primary-500/20 to-secondary-500/20 blur-3xl"></div>
				<h1 class="relative text-5xl md:text-7xl font-display font-bold text-neutral-800 dark:text-white">
					Chat with Your 
					<span class="gradient-text">PDFs</span>
				</h1>
			</div>
			
			<p class="text-xl md:text-2xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto leading-relaxed">
				Upload your documents and have intelligent conversations with your content. 
				Get instant answers, summaries, and insights from your PDFs.
			</p>
		</div>

		<!-- CTA Buttons -->
		<div class="flex flex-col sm:flex-row gap-4 justify-center items-center animate-slide-up">
			{#if user}
				<a href="/documents">
					<Button variant="primary" size="lg">
						<span class="material-icons mr-2">upload_file</span>
						Upload Documents
					</Button>
				</a>
				<a href="/chat">
					<Button variant="secondary" size="lg">
						<span class="material-icons mr-2">chat</span>
						Start Chatting
					</Button>
				</a>
			{:else}
				<a href="/auth/signup">
					<Button variant="primary" size="lg">
						<span class="material-icons mr-2">person_add</span>
						Get Started
					</Button>
				</a>
				<a href="/auth/signin">
					<Button variant="outline" size="lg">
						<span class="material-icons mr-2">login</span>
						Sign In
					</Button>
				</a>
			{/if}
		</div>

		<!-- Features Grid -->
		<div class="grid md:grid-cols-3 gap-8 mt-16">
			<div class="card p-6 text-center space-y-4">
				<div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-primary-600 rounded-2xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-2xl">upload_file</span>
				</div>
				<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200">Upload PDFs</h3>
				<p class="text-neutral-600 dark:text-neutral-400">Simply upload your PDF documents and let our AI process them for you.</p>
			</div>
			
			<div class="card p-6 text-center space-y-4">
				<div class="w-16 h-16 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-2xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-2xl">chat</span>
				</div>
				<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200">Chat Naturally</h3>
				<p class="text-neutral-600 dark:text-neutral-400">Ask questions in natural language and get intelligent responses from your documents.</p>
			</div>
			
			<div class="card p-6 text-center space-y-4">
				<div class="w-16 h-16 bg-gradient-to-r from-accent-500 to-accent-600 rounded-2xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-2xl">insights</span>
				</div>
				<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200">Get Insights</h3>
				<p class="text-neutral-600 dark:text-neutral-400">Extract key information, summaries, and insights from your documents instantly.</p>
			</div>
		</div>
	</div>
</div>
