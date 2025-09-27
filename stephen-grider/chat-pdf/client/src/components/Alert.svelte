<script lang="ts">
	import classNames from 'classnames';

	export let onDismiss: (() => void) | null = null;
	export let type: 'error' | 'success' | 'info' | 'warning' = 'error';

	const klasses = {
		error: 'bg-red-50 border border-red-200 text-red-700',
		success: 'bg-green-50 border border-green-200 text-green-700',
		info: 'bg-blue-50 border border-blue-200 text-blue-700',
		warning: 'bg-yellow-50 border border-yellow-200 text-yellow-700'
	};
	
	const icons = {
		error: 'error_outline',
		success: 'check_circle_outline',
		info: 'info_outline',
		warning: 'warning_amber'
	};
	
	const klass = classNames(klasses[type], 'rounded-xl p-4 shadow-soft');

	function handleDismiss() {
		if (onDismiss) {
			onDismiss();
		}
	}
</script>

<div class={klass} role="alert">
	<div class="flex items-start space-x-3">
		<span class="material-icons text-lg flex-shrink-0">{icons[type]}</span>
		<div class="flex-1 text-sm">
			<slot />
		</div>
		{#if onDismiss}
			<button
				on:click={handleDismiss}
				class="flex-shrink-0 w-6 h-6 rounded-full hover:bg-black/10 flex items-center justify-center transition-colors duration-200"
			>
				<span class="material-icons text-sm">close</span>
			</button>
		{/if}
	</div>
</div>
