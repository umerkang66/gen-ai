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

	export let onSubmit: (text: string, useStreaming: boolean) => void;
	export let documentId: number | undefined = undefined;

	let useStreaming = !!localStorage.getItem('streaming');

	$: localStorage.setItem('streaming', useStreaming ? 'true' : '');
	$: activeConversation = $store.activeConversationId ? getActiveConversation() : null;
	$: isDocumentChat = documentId !== undefined;

	function handleSubmit(event: CustomEvent<string>) {
		if (onSubmit) {
			onSubmit(event.detail, useStreaming);
		}
	}

	function handleNewChat() {
		if (isDocumentChat) {
			createConversation(documentId);
		} else {
			createConversation();
		}
	}

	onMount(() => {
		if (isDocumentChat) {
			fetchConversations(documentId);
		} else {
			fetchConversations();
		}
	});
</script>

<div class="flex flex-col glass-effect rounded-xl shadow-medium overflow-hidden h-full">
	<!-- Compact Header -->
	<div class="glass-effect border-b border-white/20 px-4 py-3 flex items-center justify-between flex-shrink-0">
	
		
		<div class="flex items-center space-x-2">
			<!-- Streaming Toggle -->
			<label class="flex items-center space-x-2 cursor-pointer">
				<div class="relative">
					<input 
						id="chat-type" 
						type="checkbox" 
						bind:checked={useStreaming}
						class="sr-only"
					/>
					<div class="w-8 h-4 bg-secondary-200 rounded-full transition-colors duration-200 {useStreaming ? 'bg-primary-500' : ''}">
						<div class="w-3 h-3 bg-white rounded-full shadow-sm transform transition-transform duration-200 translate-x-0.5 translate-y-0.5 {useStreaming ? 'translate-x-4' : ''}"></div>
					</div>
				</div>
				<span class="text-xs text-secondary-600">Stream</span>
			</label>
			
			<!-- Conversation Controls -->
			<div class="flex items-center space-x-1">
				<ConversationSelect conversations={$store.conversations} />
				<button 
					class="btn-secondary text-xs px-2 py-1 flex items-center space-x-1"
					on:click={handleNewChat}
				>
					<span class="material-icons text-xs">add</span>
					<span>New</span>
				</button>
			</div>
		</div>
	</div>

	<!-- Chat Messages -->
	<div class="chat-messages-scroll flex-1 overflow-y-auto px-4 py-3 space-y-3 min-h-0">
		<ChatList messages={activeConversation?.messages || []} {isDocumentChat} />
		
		<!-- Error Display -->
		{#if $store.error && $store.error.length < 200}
			<div class="animate-slide-up">
				<Alert type="error" onDismiss={resetError}>
					{$store.error}
				</Alert>
			</div>
		{/if}
	</div>

	<!-- Chat Input -->
	<div class="border-t border-white/20 p-4 flex-shrink-0">
		<ChatInput on:submit={handleSubmit} />
	</div>
</div>

<style>
	/* Ensure the chat panel takes full height and enables proper scrolling */
	:global(.chat-panel-wrapper) {
		height: 100%;
		max-height: 100%;
		overflow: hidden;
	}
	
	/* Ensure smooth scrolling for the chat messages area only */
	.chat-messages-scroll {
		scrollbar-width: thin;
		scrollbar-color: rgba(156, 163, 175, 0.5) transparent;
		max-height: calc(100vh - 300px);
	}
	
	.chat-messages-scroll::-webkit-scrollbar {
		width: 8px;
	}
	
	.chat-messages-scroll::-webkit-scrollbar-track {
		background: rgba(156, 163, 175, 0.1);
		border-radius: 4px;
	}
	
	.chat-messages-scroll::-webkit-scrollbar-thumb {
		background-color: rgba(156, 163, 175, 0.6);
		border-radius: 4px;
	}
	
	.chat-messages-scroll::-webkit-scrollbar-thumb:hover {
		background-color: rgba(156, 163, 175, 0.8);
	}
</style>
