<script lang="ts">
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import ChatPanel from '$c/chat/ChatPanel.svelte';

	beforeNavigate(resetAll);

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming });
	}
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 via-white to-neutral-100 dark:from-neutral-900 dark:via-neutral-800 dark:to-neutral-900">
	<div class="container mx-auto px-4 py-8 max-w-6xl">
		<div class="text-center mb-8 animate-fade-in">
			<h1 class="text-4xl md:text-5xl font-display font-bold text-neutral-800 dark:text-white mb-4">
				Chat with Your 
				<span class="gradient-text">Documents</span>
			</h1>
			<p class="text-lg text-neutral-600 dark:text-neutral-300">
				Ask questions and get intelligent responses from your uploaded PDFs
			</p>
		</div>
		
		<div class="h-[calc(100vh-200px)]">
			<ChatPanel onSubmit={handleSubmit} />
		</div>
	</div>
</div>
