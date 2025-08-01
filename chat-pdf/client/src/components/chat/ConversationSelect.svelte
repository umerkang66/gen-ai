<script lang="ts">
	import type { Conversation } from '$s/chat';
	import { onMount } from 'svelte';
	import { setActiveConversationId } from '$s/chat';
	import Button from '$c/Button.svelte';

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
	<div>
		<button
			on:click={() => (isOpen = !isOpen)}
			type="button"
			class="inline-flex items-center justify-center px-3 py-1.5 text-xs font-medium text-neutral-800 dark:text-neutral-200 bg-white/80 dark:bg-neutral-800/80 border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-white dark:hover:bg-neutral-800 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 transition-all duration-200 backdrop-blur-sm"
			id="options-menu"
			aria-haspopup="true"
			aria-expanded="true"
		>
			<span class="material-icons text-sm mr-1">history</span>
			History
			<span class="material-icons ml-1 text-xs transition-transform duration-200 {isOpen ? 'rotate-180' : ''}">
				expand_more
			</span>
		</button>
	</div>

	{#if isOpen}
		<div
			class="origin-top-right absolute right-0 mt-1 w-56 rounded-lg shadow-xl bg-white/95 dark:bg-neutral-800/95 border border-white/20 dark:border-neutral-700/20 backdrop-blur-md ring-1 ring-black/5 dark:ring-white/5 z-50"
			style="max-height: 250px; overflow-y: auto;"
		>
			<div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
				<!-- Header -->
				<div class="px-3 py-2 border-b border-neutral-200 dark:border-neutral-700">
					<h3 class="text-xs font-semibold text-neutral-800 dark:text-neutral-200">
						Conversation History
					</h3>
					<p class="text-xs text-neutral-500 dark:text-neutral-400">
						{conversations.length} conversation{conversations.length !== 1 ? 's' : ''}
					</p>
				</div>

				<!-- Conversations List -->
				<div class="max-h-36 overflow-y-auto">
					{#if conversations.length === 0}
						<div class="px-3 py-2 text-center">
							<div class="w-6 h-6 bg-neutral-200 dark:bg-neutral-700 rounded-lg flex items-center justify-center mx-auto mb-1">
								<span class="material-icons text-neutral-400 text-xs">chat</span>
							</div>
							<p class="text-xs text-neutral-500 dark:text-neutral-400">No conversations yet</p>
						</div>
					{:else}
						{#each conversations as conversation (conversation.id)}
							<button
								class="w-full text-left px-3 py-2 text-xs text-neutral-700 dark:text-neutral-300 hover:bg-neutral-100 dark:hover:bg-neutral-700 hover:text-neutral-900 dark:hover:text-neutral-100 transition-colors duration-200 flex items-center space-x-2"
								on:click={() => handleClick(conversation)}
								on:keypress={() => {}}
							>
								<div class="w-1.5 h-1.5 bg-primary-500 rounded-full flex-shrink-0"></div>
								<div class="flex-1 min-w-0">
									<div class="truncate text-xs">
										Conversation {conversation.id.slice(0, 8)}...
									</div>
									<div class="text-xs text-neutral-500 dark:text-neutral-400">
										{conversation.messages?.length || 0} messages
									</div>
								</div>
							</button>
						{/each}
					{/if}
				</div>

				<!-- Footer -->
				<div class="px-3 py-1 border-t border-neutral-200 dark:border-neutral-700">
					<p class="text-xs text-neutral-500 dark:text-neutral-400 text-center">
						Click to switch conversations
					</p>
				</div>
			</div>
		</div>
	{/if}
</div>
