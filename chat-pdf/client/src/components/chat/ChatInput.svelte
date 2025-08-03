<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import Button from '$c/Button.svelte';

	let value = '';
	let textarea: HTMLTextAreaElement;

	const dispatch = createEventDispatcher();
	
	function handleKeyDown(event: KeyboardEvent) {
		const isCombo = event.shiftKey || event.ctrlKey || event.altKey || event.metaKey;
		if (event.key !== 'Enter' || isCombo) {
			return;
		}

		if (event.key === 'Enter' && !isCombo && value === '') {
			event.preventDefault();
			return;
		}

		event.preventDefault();
		submitMessage();
	}

	function submitMessage() {
		console.log('submitMessage called, value:', value);
		if (value.trim()) {
			console.log('Dispatching submit event with value:', value);
			dispatch('submit', value);
			value = '';
			// Reset textarea height
			if (textarea) {
				textarea.style.height = 'auto';
			}
		} else {
			console.log('Value is empty, not submitting');
		}
	}

	function adjustHeight() {
		if (textarea) {
			textarea.style.height = 'auto';
			textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px';
		}
	}

	$: if (value !== undefined) {
		setTimeout(adjustHeight, 0);
	}
</script>

<div class="flex items-end space-x-3">
	<div class="flex-1 relative">
		<textarea
			bind:this={textarea}
			bind:value
			on:keydown={handleKeyDown}
			placeholder="Ask from document..."
			class="w-full px-4 py-3 pr-12 bg-white/70 dark:bg-neutral-800/70 border border-neutral-200 dark:border-neutral-700 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200 resize-none min-h-[48px] max-h-[200px] text-neutral-800 dark:text-neutral-200 placeholder-neutral-500 dark:placeholder-neutral-400"
			rows="1"
		/>
	</div>
	
	<Button 
		variant="primary" 
		size="md" 
		on:click={() => {
			console.log('Button clicked!');
			submitMessage();
		}}
		disabled={!value.trim()}
		class="flex-shrink-0"
	>
		<span class="material-icons">send</span>
	</Button>
</div>
