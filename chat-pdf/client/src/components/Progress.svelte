<script>
	import { tweened } from 'svelte/motion';

	export let progress = 0;

	const width = tweened(1, {
		duration: 1000
	});

	$: width.set(progress);
</script>

{#if $$slots.default && $width === 100}
	<slot />
{:else}
	<div class="space-y-2">
		<div class="flex justify-between text-sm text-secondary-600">
			<span>Uploading...</span>
			<span>{Math.round($width)}%</span>
		</div>
		<div class="w-full h-2 bg-secondary-200 rounded-full overflow-hidden">
			<div
				class="h-full bg-gradient-to-r from-primary-500 to-accent-500 rounded-full transition-all duration-300 ease-out"
				role="progressbar"
				style="width: {$width}%"
			/>
		</div>
	</div>
{/if}
