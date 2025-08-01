<script lang="ts">
	export let type: string = 'text';
	export let value = '';
	export let placeholder = '';
	export let label = '';

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<div class="space-y-2">
	{#if label}
		<label for="input-{label}" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300">
			{label}
		</label>
	{/if}
	<input
		use:typeAction
		bind:value
		{placeholder}
		id="input-{label}"
		class="input-modern"
		required
	/>
</div>
