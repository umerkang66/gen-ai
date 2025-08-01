<script lang="ts">
	import type { PageData } from './$types';
	import AuthGuard from '$c/AuthGuard.svelte';
	import Button from '$c/Button.svelte';

	export let data: PageData;

	const documents = data.documents || [];
</script>

<AuthGuard />

<div class="min-h-screen py-8">
	<!-- Header Section -->
	<div class="text-center mb-12 animate-fade-in">
		<h1 class="text-4xl md:text-6xl font-display font-bold text-neutral-800 dark:text-white mb-4">
			Your 
			<span class="gradient-text">Documents</span>
		</h1>
		<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
			Manage and interact with your uploaded PDF documents
		</p>
	</div>

	<!-- Action Bar -->
	<div class="flex justify-between items-center mb-8">
		<div class="flex items-center space-x-4">
			<div class="flex items-center space-x-2">
				<div class="w-8 h-8 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center">
					<span class="material-icons text-white text-sm">description</span>
				</div>
				<span class="text-lg font-semibold text-neutral-800 dark:text-neutral-200">
					{documents.length} Document{documents.length !== 1 ? 's' : ''}
				</span>
			</div>
		</div>
		
		<a href="/documents/new">
			<Button variant="primary" size="lg">
				<span class="material-icons mr-2">upload_file</span>
				Upload Document
			</Button>
		</a>
	</div>

	<!-- Documents Grid -->
	{#if documents.length === 0}
		<div class="text-center py-16">
			<div class="w-24 h-24 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-3xl flex items-center justify-center mx-auto mb-6">
				<span class="material-icons text-white text-4xl">upload_file</span>
			</div>
			<h3 class="text-2xl font-semibold text-neutral-800 dark:text-neutral-200 mb-4">
				No Documents Yet
			</h3>
			<p class="text-neutral-600 dark:text-neutral-400 max-w-md mx-auto mb-8">
				Upload your first PDF document to start chatting with your content. 
				Simply drag and drop or click to upload.
			</p>
			<a href="/documents/new">
				<Button variant="primary" size="lg">
					<span class="material-icons mr-2">upload_file</span>
					Upload Your First Document
				</Button>
			</a>
		</div>
	{:else}
		<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each documents as document}
				<div class="card p-6 hover:scale-105 transition-all duration-200 animate-slide-up">
					<div class="flex items-start justify-between mb-4">
						<div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-primary-600 rounded-xl flex items-center justify-center">
							<span class="material-icons text-white text-xl">description</span>
						</div>
						<div class="flex items-center space-x-2">
							<span class="text-xs bg-green-100 dark:bg-green-900/20 text-green-800 dark:text-green-400 px-2 py-1 rounded-full">
								Active
							</span>
						</div>
					</div>
					
					<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-200 mb-2 line-clamp-2">
						{document.name}
					</h3>
					
					<div class="flex items-center justify-between mt-4">
						<div class="flex items-center space-x-2 text-sm text-neutral-500 dark:text-neutral-400">
							<span class="material-icons text-sm">info</span>
							<span>ID: {document.id}</span>
						</div>
						
						<div class="flex items-center space-x-2">
							<a href="/documents/{document.id}" class="group">
								<div class="w-8 h-8 bg-gradient-to-r from-primary-500 to-primary-600 rounded-lg flex items-center justify-center group-hover:scale-110 transition-transform duration-200">
									<span class="material-icons text-white text-sm">visibility</span>
								</div>
							</a>
							<a href="/chat?document={document.id}" class="group">
								<div class="w-8 h-8 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-lg flex items-center justify-center group-hover:scale-110 transition-transform duration-200">
									<span class="material-icons text-white text-sm">chat</span>
								</div>
							</a>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}

	<!-- Quick Actions -->
	{#if documents.length > 0}
		<div class="mt-12 card p-8">
			<h3 class="text-2xl font-display font-bold text-neutral-800 dark:text-neutral-200 mb-6">
				Quick Actions
			</h3>
			<div class="grid md:grid-cols-3 gap-6">
				<div class="text-center space-y-3">
					<div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-primary-600 rounded-2xl flex items-center justify-center mx-auto">
						<span class="material-icons text-white text-2xl">upload_file</span>
					</div>
					<h4 class="text-lg font-semibold text-neutral-800 dark:text-neutral-200">Upload More</h4>
					<p class="text-sm text-neutral-600 dark:text-neutral-400">Add more documents to your collection</p>
					<a href="/documents/new">
						<Button variant="outline" size="sm">Upload</Button>
					</a>
				</div>
				
				<div class="text-center space-y-3">
					<div class="w-16 h-16 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-2xl flex items-center justify-center mx-auto">
						<span class="material-icons text-white text-2xl">chat</span>
					</div>
					<h4 class="text-lg font-semibold text-neutral-800 dark:text-neutral-200">Start Chatting</h4>
					<p class="text-sm text-neutral-600 dark:text-neutral-400">Begin a conversation with your documents</p>
					<a href="/chat">
						<Button variant="outline" size="sm">Chat</Button>
					</a>
				</div>
				
				<div class="text-center space-y-3">
					<div class="w-16 h-16 bg-gradient-to-r from-accent-500 to-accent-600 rounded-2xl flex items-center justify-center mx-auto">
						<span class="material-icons text-white text-2xl">analytics</span>
					</div>
					<h4 class="text-lg font-semibold text-neutral-800 dark:text-neutral-200">View Analytics</h4>
					<p class="text-sm text-neutral-600 dark:text-neutral-400">Check performance and insights</p>
					<a href="/scores">
						<Button variant="outline" size="sm">Analytics</Button>
					</a>
				</div>
			</div>
		</div>
	{/if}
</div>
