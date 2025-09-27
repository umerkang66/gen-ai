<script lang="ts">
	import { onMount } from 'svelte';
	import { errorStore, reset } from '$s/errors';
	import ErrorMessage from '$c/ErrorMessage.svelte';

	const listener = (event: KeyboardEvent) => {
		if (event.key === 'Escape') {
			reset();
		}
	};

	onMount(() => {
		window.addEventListener('keydown', listener);
		return () => window.removeEventListener('keydown', listener);
	});
</script>

{#if $errorStore.errors.length}
	<!-- Backdrop -->
	<div 
		on:click={reset} 
		class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
	>
		<!-- Modal -->
		<div 
			class="glass-effect rounded-2xl shadow-large max-w-2xl w-full max-h-[80vh] overflow-hidden"
			on:click|stopPropagation
		>
			<!-- Header -->
			<div class="flex items-center justify-between p-6 border-b border-white/20">
				<div class="flex items-center space-x-3">
					<div class="w-10 h-10 bg-gradient-to-br from-red-500 to-red-600 rounded-xl flex items-center justify-center shadow-soft">
						<span class="material-icons text-white">error_outline</span>
					</div>
					<div>
						<h2 class="text-xl font-bold text-secondary-800">Error Occurred</h2>
						<p class="text-sm text-secondary-500">Please review the details below</p>
					</div>
				</div>
				<button 
					on:click={reset}
					class="w-8 h-8 rounded-full hover:bg-black/10 flex items-center justify-center transition-colors duration-200"
				>
					<span class="material-icons text-secondary-500">close</span>
				</button>
			</div>

			<!-- Content -->
			<div class="p-6 overflow-y-auto max-h-96">
				<div class="space-y-4">
					{#each $errorStore.errors as error, index}
						<div class="bg-red-50 border border-red-200 rounded-xl p-4">
							<div class="flex items-start space-x-3">
								<span class="material-icons text-red-500 text-sm mt-0.5">error</span>
								<div class="flex-1">
									{#if error.contentType?.includes('text/html')}
										<ErrorMessage message={error.message} />
									{:else}
										<p class="text-red-700 text-sm">{error.message}</p>
									{/if}
								</div>
							</div>
						</div>
					{/each}
				</div>
			</div>

			<!-- Footer -->
			<div class="flex justify-end p-6 border-t border-white/20">
				<button 
					on:click={reset}
					class="btn-secondary"
				>
					<span class="material-icons mr-2">close</span>
					Close
				</button>
			</div>
		</div>
	</div>
{/if}
