<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	let value = '';
	let isSubmitting = false;

	const dispatch = createEventDispatcher();
	
	function handleKeyDown(event: KeyboardEvent) {
		const isCombo = event.shiftKey || event.ctrlKey || event.altKey || event.metaKey;
		if (event.key !== 'Enter' || isCombo) {
			return;
		}

		if (event.key === 'Enter' && !isCombo && value.trim() === '') {
			event.preventDefault();
			return;
		}

		event.preventDefault();
		submitMessage();
	}

	function submitMessage() {
		if (value.trim() === '' || isSubmitting) return;
		
		isSubmitting = true;
		dispatch('submit', value.trim());
		value = '';
		
		setTimeout(() => {
			isSubmitting = false;
		}, 100);
	}

	$: height = Math.min((value.match(/\n/g)?.length || 0) * 16 + 40, 80);
</script>

<div class="relative">
	<div class="flex items-end space-x-2">
		<div class="flex-1 relative">
			<textarea
				class="input-modern resize-none w-full pr-10 focus:ring-2 focus:ring-primary-500 focus:border-transparent text-sm"
				style:height={height + 'px'}
				bind:value
				on:keydown={handleKeyDown}
				placeholder="Type your message..."
				disabled={isSubmitting}
			/>
		</div>
		
		<button
			class="w-8 h-8 bg-gradient-to-r from-primary-600 to-accent-600 hover:from-primary-700 hover:to-accent-700 text-white rounded-lg flex items-center justify-center shadow-soft hover:shadow-medium transition-all duration-300 transform hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
			on:click={submitMessage}
			disabled={value.trim() === '' || isSubmitting}
		>
			{#if isSubmitting}
				<div class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
			{:else}
				<span class="material-icons text-sm">send</span>
			{/if}
		</button>
	</div>
</div>
