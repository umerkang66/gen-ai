<script lang="ts">
	import type { PageData } from './$types';
	import AuthGuard from '$c/AuthGuard.svelte';

	export let data: PageData;

	const documents = data.documents || [];
</script>

<AuthGuard />

<div class="space-y-8 animate-fade-in">
	<!-- Header Section -->
	<div class="text-center space-y-4">
		<h1 class="text-4xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
			Your Documents
		</h1>
		<p class="text-secondary-600 text-lg max-w-2xl mx-auto">
			Upload and manage your PDF documents to start chatting with AI assistance
		</p>
	</div>

	<!-- Action Bar -->
	<div class="flex justify-center">
		<a
			href="/documents/new"
			class="btn-primary flex items-center space-x-2"
		>
			<span class="material-icons">add</span>
			<span>Upload New Document</span>
		</a>
	</div>

	<!-- Documents Grid -->
	{#if documents.length === 0}
		<div class="text-center py-16">
			<div class="w-24 h-24 bg-gradient-to-br from-secondary-100 to-secondary-200 rounded-full flex items-center justify-center mx-auto mb-6">
				<span class="material-icons text-4xl text-secondary-400">description</span>
			</div>
			<h3 class="text-xl font-semibold text-secondary-700 mb-2">No documents yet</h3>
			<p class="text-secondary-500 mb-6">Upload your first PDF to get started</p>
			<a href="/documents/new" class="btn-primary">
				<span class="material-icons mr-2">upload_file</span>
				Upload Document
			</a>
		</div>
	{:else}
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each documents as document}
				<div class="glass-effect rounded-2xl p-6 card-hover group">
					<div class="flex items-start justify-between mb-4">
						<div class="w-12 h-12 bg-gradient-to-br from-primary-500 to-accent-500 rounded-xl flex items-center justify-center shadow-soft">
							<span class="material-icons text-white">description</span>
						</div>
						<div class="opacity-0 group-hover:opacity-100 transition-opacity duration-200">
							<span class="material-icons text-secondary-400 hover:text-primary-600 cursor-pointer">more_vert</span>
						</div>
					</div>
					
					<h3 class="text-lg font-semibold text-secondary-800 mb-2 line-clamp-2">
						{document.name}
					</h3>
					
					<div class="space-y-2 mb-6">
						<div class="flex items-center text-sm text-secondary-500">
							<span class="material-icons text-xs mr-2">tag</span>
							<span class="font-mono text-xs bg-secondary-100 px-2 py-1 rounded-md">
								{document.id}
							</span>
						</div>
					</div>
					
					<div class="flex justify-end">
						<a 
							href="/documents/{document.id}"
							class="btn-secondary text-sm px-4 py-2 flex items-center space-x-1"
						>
							<span class="material-icons text-sm">visibility</span>
							<span>View</span>
						</a>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
