<script lang="ts">
	import type { Conversation } from '$s/chat';
	import { onMount } from 'svelte';
	import { setActiveConversationId } from '$s/chat';

	export let conversations: Conversation[] = [];
	let isOpen = false;

	async function handleClick(conversation: Conversation) {
		isOpen = false;
		setActiveConversationId(conversation.id);
	}

	onMount(() => {
		window.addEventListener('click', (e: any) => {
			if (e.target && !e.target.closest('.relative')) {
				isOpen = false;
			}
		});
	});
</script>

<div class="relative inline-block text-left">
	<button
		on:click={() => (isOpen = !isOpen)}
		type="button"
		class="btn-secondary text-xs px-2 py-1 flex items-center space-x-1"
		id="options-menu"
		aria-haspopup="true"
		aria-expanded={isOpen}
	>
		<span class="material-icons text-xs">history</span>
		<span class="hidden sm:inline">History</span>
		<span class="material-icons text-xs transition-transform duration-200 {isOpen ? 'rotate-180' : ''}">expand_more</span>
	</button>

	{#if isOpen}
		<div
			class="absolute right-0 mt-1 w-48 rounded-xl shadow-medium glass-effect border border-white/20 overflow-hidden z-50"
			style="max-height: 200px;"
		>
			<div class="p-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
				{#if conversations.length === 0}
					<div class="px-3 py-2 text-xs text-secondary-500 text-center">
						No history
					</div>
				{:else}
					{#each conversations as conversation (conversation.id)}
						<button
							class="w-full text-left px-3 py-2 text-xs text-secondary-700 hover:bg-white/50 hover:text-primary-600 rounded-lg transition-all duration-200 flex items-center space-x-2"
							on:click={() => handleClick(conversation)}
						>
							<span class="material-icons text-secondary-400 text-xs">chat_bubble_outline</span>
							<span class="font-mono text-xs bg-secondary-100 px-1 py-0.5 rounded text-xs">
								{conversation.id}
							</span>
						</button>
					{/each}
				{/if}
			</div>
		</div>
	{/if}
</div>
