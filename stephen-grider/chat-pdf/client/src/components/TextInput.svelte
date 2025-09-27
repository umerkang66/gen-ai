<script lang="ts">
	export let type: string = 'text';
	export let value = '';
	export let placeholder = '';
	export let label = '';
	export let required = false;

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<div class="space-y-2">
	{#if label}
		<label class="block text-sm font-medium text-secondary-700">
			{label}
			{#if required}
				<span class="text-red-500">*</span>
			{/if}
		</label>
	{/if}
	
	<input
		use:typeAction
		bind:value
		{placeholder}
		{required}
		class="input-modern"
	/>
</div>
