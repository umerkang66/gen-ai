<script lang="ts">
	export let label: string = '';
	export let required = false;
	export let error = '';
</script>

<div class="space-y-2">
	{#if label}
		<div class="flex justify-between items-center">
			<label class="block text-sm font-medium text-secondary-700">
				{label}
				{#if required}
					<span class="text-red-500">*</span>
				{/if}
			</label>
		</div>
	{/if}
	
	<div class="relative">
		<slot />
	</div>
	
	{#if error}
		<p class="text-sm text-red-600 mt-1 flex items-center space-x-1">
			<span class="material-icons text-sm">error_outline</span>
			<span>{error}</span>
		</p>
	{/if}
</div>
