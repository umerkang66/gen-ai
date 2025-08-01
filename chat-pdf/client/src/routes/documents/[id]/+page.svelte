<script lang="ts">
	import type { PageData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import PdfViewer from '$c/PdfViewer.svelte';
	import ChatPanel from '$c/chat/ChatPanel.svelte';
	import Button from '$c/Button.svelte';

	export let data: PageData;

	const document = data.document;
	const documentUrl = data.documentUrl;

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming, documentId: document.id });
	}

	beforeNavigate(resetAll);
</script>

{#if data.error}
	<div class="min-h-screen flex items-center justify-center">
		<div class="text-center">
			<div class="w-16 h-16 bg-red-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">error</span>
			</div>
			<h2 class="text-2xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">
				Error Loading Document
			</h2>
			<p class="text-neutral-600 dark:text-neutral-400 mb-6">
				{data.error}
			</p>
			<a href="/documents">
				<Button variant="primary">
					<span class="material-icons mr-2">arrow_back</span>
					Back to Documents
				</Button>
			</a>
		</div>
	</div>
{:else if document}
	<div class="min-h-screen bg-gradient-to-br from-neutral-50 via-white to-neutral-100 dark:from-neutral-900 dark:via-neutral-800 dark:to-neutral-900">
		<!-- Header -->
		<div class="sticky top-0 z-40 glass-effect border-b border-white/20 dark:border-neutral-700/20">
			<div class="container mx-auto px-4 py-4">
				<div class="flex items-center justify-between">
					<div class="flex items-center space-x-4">
						<a href="/documents" class="group">
							<div class="w-8 h-8 bg-gradient-to-r from-neutral-500 to-neutral-600 rounded-lg flex items-center justify-center group-hover:scale-110 transition-transform duration-200">
								<span class="material-icons text-white text-sm">arrow_back</span>
							</div>
						</a>
						<div class="flex items-center space-x-3">
							<div class="w-10 h-10 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center">
								<span class="material-icons text-white text-lg">description</span>
							</div>
							<div>
								<h1 class="text-xl font-display font-bold text-neutral-800 dark:text-neutral-200">
									{document.name}
								</h1>
								<p class="text-sm text-neutral-600 dark:text-neutral-400">
									Document ID: {document.id}
								</p>
							</div>
						</div>
					</div>
					
					<div class="flex items-center space-x-3">
						<a href="/chat?document={document.id}">
							<Button variant="secondary" size="sm">
								<span class="material-icons text-sm mr-1">chat</span>
								Chat
							</Button>
						</a>
					</div>
				</div>
			</div>
		</div>

		<!-- Main Content -->
		<div class="container mx-auto px-4 py-6">
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[calc(100vh-140px)]">
				<!-- Chat Panel -->
				<div class="lg:col-span-1">
					<ChatPanel documentId={document.id} onSubmit={handleSubmit} />
				</div>
				
				<!-- PDF Viewer -->
				<div class="lg:col-span-2">
					<div class="card h-full overflow-hidden">
						<div class="p-4 border-b border-white/20 dark:border-neutral-700/20">
							<div class="flex items-center space-x-2">
								<div class="w-6 h-6 bg-gradient-to-r from-accent-500 to-accent-600 rounded-lg flex items-center justify-center">
									<span class="material-icons text-white text-sm">picture_as_pdf</span>
								</div>
								<h3 class="font-semibold text-neutral-800 dark:text-neutral-200">
									PDF Viewer
								</h3>
							</div>
						</div>
						<div class="flex-1 h-full">
							<PdfViewer url={documentUrl} />
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{:else}
	<div class="min-h-screen flex items-center justify-center">
		<div class="text-center">
			<div class="w-16 h-16 bg-neutral-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">search</span>
			</div>
			<h2 class="text-2xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">
				Document Not Found
			</h2>
			<p class="text-neutral-600 dark:text-neutral-400 mb-6">
				The document you're looking for doesn't exist or has been removed.
			</p>
			<a href="/documents">
				<Button variant="primary">
					<span class="material-icons mr-2">arrow_back</span>
					Back to Documents
				</Button>
			</a>
		</div>
	</div>
{/if}
