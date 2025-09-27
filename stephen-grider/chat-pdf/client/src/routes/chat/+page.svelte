<script lang="ts">
	import { beforeNavigate } from '$app/navigation';
	import { resetAll, sendMessage } from '$s/chat/index';
	import ChatPanel from '$c/chat/ChatPanel.svelte';
	import AuthGuard from '$c/AuthGuard.svelte';

	beforeNavigate(resetAll);

	function handleSubmit(content: string, useStreaming: boolean) {
		sendMessage({ role: 'user', content }, { useStreaming });
	}
</script>

<AuthGuard />

<div class="space-y-4">
	<!-- Compact Header -->
	<div class="glass-effect rounded-xl p-4 shadow-medium">
		<div class="flex items-center space-x-3">
			<div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-accent-500 rounded-xl flex items-center justify-center shadow-soft">
				<span class="material-icons text-white">chat</span>
			</div>
			<div>
				<h1 class="text-lg font-bold text-secondary-800">General Chat</h1>
				<p class="text-sm text-secondary-500">Chat with AI without a specific document context</p>
			</div>
		</div>
	</div>

	<!-- Chat Panel -->
	<div class="h-[calc(100vh-180px)] chat-panel-wrapper">
		<ChatPanel onSubmit={handleSubmit} />
	</div>
</div>

<style>
	.chat-panel-wrapper {
		height: 80%;
	}
</style>
