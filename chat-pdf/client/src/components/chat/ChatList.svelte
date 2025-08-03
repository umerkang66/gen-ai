<script lang="ts">
	import AssistantMessage from '$c/chat/AssistantMessage.svelte';
	import UserMessage from '$c/chat/UserMessage.svelte';
	import PendingMessage from '$c/chat/PendingMessage.svelte';

	interface Message {
		role: 'user' | 'system' | 'assistant' | 'pending' | 'human' | 'ai';
		content: string;
	}
	export let messages: Message[] = [];
	export let isDocumentChat: boolean = true;

	const scrollIntoView = (node: HTMLDivElement, _m: any) => {
		setTimeout(() => {
			node.scrollIntoView({ behavior: 'smooth', block: 'end' });
		}, 0);
		return {
			update: () => node.scrollIntoView({ behavior: 'smooth', block: 'end' })
		};
	};
</script>

<div class="flex flex-col space-y-3">
	{#if messages.length === 0}
		<div class="text-center py-8">
			<div class="w-12 h-12 bg-gradient-to-br from-secondary-100 to-secondary-200 rounded-full flex items-center justify-center mx-auto mb-3">
				<span class="material-icons text-xl text-secondary-400">chat_bubble_outline</span>
			</div>
			<h3 class="text-sm font-semibold text-secondary-700 mb-1">
				{isDocumentChat ? 'Start a conversation' : 'Welcome to ChatPDF!'}
			</h3>
			<p class="text-xs text-secondary-500">
				{isDocumentChat 
					? 'Ask questions about your document to get started'
					: 'I\'m here to help! Ask me anything and I\'ll do my best to assist you.'
				}
			</p>
		</div>
	{:else}
		{#each messages as message, index}
			<div class="animate-fade-in" style="animation-delay: {index * 0.1}s">
				{#if message.role === 'user' || message.role === 'human'}
					<UserMessage content={message.content} />
				{:else if message.role === 'assistant' || message.role === 'ai'}
					<AssistantMessage content={message.content} />
				{:else if message.role === 'pending'}
					<PendingMessage />
				{/if}
			</div>
		{/each}
	{/if}
	
	<div class="pt-2" use:scrollIntoView={messages} />
</div>
