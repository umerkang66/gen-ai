<script lang="ts">
	import AssistantMessage from '$c/chat/AssistantMessage.svelte';
	import UserMessage from '$c/chat/UserMessage.svelte';
	import PendingMessage from '$c/chat/PendingMessage.svelte';

	interface Message {
		role: 'user' | 'system' | 'assistant' | 'pending' | 'human' | 'ai';
		content: string;
	}
	export let messages: Message[] = [];

	const scrollIntoView = (node: HTMLDivElement, _m: any) => {
		setTimeout(() => {
			node.scrollIntoView({ behavior: 'smooth' });
		}, 0);
		return {
			update: () => node.scrollIntoView({ behavior: 'smooth' })
		};
	};
</script>

<div class="flex flex-col space-y-6">
	{#if messages.length === 0}
		<div class="text-center py-12">
			<div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">chat</span>
			</div>
			<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">
				Start a Conversation
			</h3>
			<p class="text-neutral-600 dark:text-neutral-400 max-w-md mx-auto">
				Ask questions about your documents and get intelligent responses from your AI assistant.
			</p>
		</div>
	{:else}
		<div class="space-y-6">
			{#each messages as message}
				{#if message.role === 'user' || message.role === 'human'}
					<UserMessage content={message.content} />
				{:else if message.role === 'assistant' || message.role === 'ai'}
					<AssistantMessage content={message.content} />
				{:else if message.role === 'pending'}
					<PendingMessage />
				{/if}
			{/each}
		</div>
	{/if}
	<div class="pt-4" use:scrollIntoView={messages} />
</div>
