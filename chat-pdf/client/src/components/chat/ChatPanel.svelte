<script lang="ts">
	import { onMount } from 'svelte';
	import {
		store,
		resetError,
		fetchConversations,
		createConversation,
		getActiveConversation
	} from '$s/chat';
	import Alert from '$c/Alert.svelte';
	import ChatInput from '$c/chat/ChatInput.svelte';
	import ChatList from '$c/chat/ChatList.svelte';
	import ConversationSelect from '$c/chat/ConversationSelect.svelte';
	import Button from '$c/Button.svelte';

	export let onSubmit: (text: string, useStreaming: boolean) => void;
	export let documentId: number;

	let useStreaming = !!localStorage.getItem('streaming');

	$: localStorage.setItem('streaming', useStreaming ? 'true' : '');
	$: activeConversation = $store.activeConversationId ? getActiveConversation() : null;

	function handleSubmit(event: CustomEvent<string>) {
		if (onSubmit) {
			onSubmit(event.detail, useStreaming);
		}
	}

	function handleNewChat() {
		createConversation(documentId);
	}

	onMount(() => {
		fetchConversations(documentId);
	});
</script>

<div class="h-full flex flex-col card overflow-hidden">
	<!-- Header -->
	<div class="glass-effect border-b border-white/20 dark:border-neutral-700/20 p-2.5">
		<div class="flex items-center justify-between">
			<div class="flex items-center space-x-2.5">
				<div class="flex items-center space-x-1.5">
					<div class="w-6 h-6 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center">
						<span class="material-icons text-white text-xs">chat</span>
					</div>
					<h2 class="text-sm font-display font-semibold text-neutral-800 dark:text-neutral-200">
						AI Assistant
					</h2>
				</div>
				
				<div class="flex items-center space-x-1.5">
					<input 
						id="streaming-toggle" 
						type="checkbox" 
						bind:checked={useStreaming}
						class="w-3 h-3 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-primary-500 focus:ring-2"
					/>
					<label for="streaming-toggle" class="text-xs text-neutral-600 dark:text-neutral-400">
						Streaming
					</label>
				</div>
			</div>
			
			<div class="flex items-center space-x-1.5">
				<div class="relative">
					<ConversationSelect conversations={$store.conversations} />
				</div>
				<Button variant="primary" size="sm" on:click={handleNewChat} className="text-xs px-2 py-1 h-7">
					<span class="material-icons text-xs mr-0.5">add</span>
					New
				</Button>
			</div>
		</div>
	</div>

	<!-- Chat Messages -->
	<div class="flex-1 overflow-hidden">
		<div class="h-full flex flex-col">
			<div class="flex-1 overflow-y-auto p-4">
				<ChatList messages={activeConversation?.messages || []} />
			</div>
			
			<!-- Error Display -->
			{#if $store.error && $store.error.length < 200}
				<div class="px-4 pb-4">
					<Alert type="error" onDismiss={resetError}>
						{$store.error}
					</Alert>
				</div>
			{/if}
			
			<!-- Input Area -->
			<div class="p-4 border-t border-white/20 dark:border-neutral-700/20 bg-white/50 dark:bg-neutral-800/50">
				<ChatInput on:submit={handleSubmit} />
			</div>
		</div>
	</div>
</div>
