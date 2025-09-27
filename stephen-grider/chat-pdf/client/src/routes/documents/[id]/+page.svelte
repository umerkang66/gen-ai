<script lang="ts">
	import type { PageData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import PdfViewer from '$c/PdfViewer.svelte';
	import ChatPanel from '$c/chat/ChatPanel.svelte';
	import AuthGuard from '$c/AuthGuard.svelte';

	export let data: PageData;

	const document = data.document;
	const documentUrl = data.documentUrl;

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming, documentId: document.id });
	}

	beforeNavigate(resetAll);
</script>

<AuthGuard />

{#if data.error}
	<div class="text-center py-16">
		<div class="w-24 h-24 bg-gradient-to-br from-red-100 to-red-200 rounded-full flex items-center justify-center mx-auto mb-6">
			<span class="material-icons text-4xl text-red-400">error_outline</span>
		</div>
		<h3 class="text-xl font-semibold text-secondary-700 mb-2">Error Loading Document</h3>
		<p class="text-secondary-500 mb-6">{data.error}</p>
		<a href="/documents" class="btn-primary">
			<span class="material-icons mr-2">arrow_back</span>
			Back to Documents
		</a>
	</div>
{:else if document}
	<div class="space-y-6">
		<!-- Document Header -->
		<div class="glass-effect rounded-2xl p-6 shadow-large">
			<div class="flex items-center justify-between">
				<div class="flex items-center space-x-4">
					<div class="w-12 h-12 bg-gradient-to-br from-primary-500 to-accent-500 rounded-xl flex items-center justify-center shadow-soft">
						<span class="material-icons text-white">description</span>
					</div>
					<div>
						<h1 class="text-2xl font-bold text-secondary-800">{document.name}</h1>
						<p class="text-secondary-500">Document ID: {document.id}</p>
					</div>
				</div>
				<a 
					href="/documents" 
					class="btn-secondary flex items-center space-x-2"
				>
					<span class="material-icons text-sm">arrow_back</span>
					<span>Back to Documents</span>
				</a>
			</div>
		</div>

		<!-- Main Content -->
		<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" style="height: calc(100vh - 200px);">
			<!-- Chat Panel -->
			<div class="lg:col-span-1 chat-panel-wrapper h-full overflow-hidden">
				<ChatPanel documentId={document.id} onSubmit={handleSubmit} />
			</div>
			
			<!-- PDF Viewer -->
			<div class="lg:col-span-2">
				<div class="glass-effect rounded-2xl overflow-hidden shadow-large h-full">
					<PdfViewer url={documentUrl} />
				</div>
			</div>
		</div>
	</div>
{/if}
