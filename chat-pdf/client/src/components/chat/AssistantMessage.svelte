<script lang="ts">
	import { marked } from 'marked';
	import classnames from 'classnames';
	import { scoreConversation } from '$s/chat';
	import Icon from '$c/Icon.svelte';

	export let content = '';
	let score = 0;

	const klass = 'w-8 h-8 rounded-full flex items-center justify-center cursor-pointer transition-all duration-200 hover:scale-110';
	$: upKlass = classnames(klass, {
		'bg-green-500 text-white': score === 1,
		'bg-neutral-200 dark:bg-neutral-700 text-neutral-600 dark:text-neutral-400 hover:bg-green-100 dark:hover:bg-green-900/20': score === 0
	});
	$: downKlass = classnames(klass, {
		'bg-red-500 text-white': score === -1,
		'bg-neutral-200 dark:bg-neutral-700 text-neutral-600 dark:text-neutral-400 hover:bg-red-100 dark:hover:bg-red-900/20': score === 0
	});

	async function applyScore(_score: number) {
		if (score !== 0) {
			return;
		}
		score = _score;
		return scoreConversation(_score);
	}
</script>

<div class="flex justify-start">
	<div class="max-w-[80%] lg:max-w-[70%]">
		<div class="bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-2xl rounded-bl-md px-4 py-3 shadow-lg">
			<div class="prose prose-neutral dark:prose-invert max-w-none">
				{@html marked(content, { breaks: true, gfm: true })}
			</div>
		</div>
		
		<div class="flex items-center mt-2 space-x-2">
			<div class="w-6 h-6 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-full flex items-center justify-center">
				<span class="material-icons text-white text-xs">smart_toy</span>
			</div>
			<span class="text-xs text-neutral-500 dark:text-neutral-400">AI Assistant</span>
			
			<div class="flex items-center space-x-1 ml-auto">
				{#if score >= 0}
					<button class={upKlass} on:click={() => applyScore(1)} title="Good response">
						<Icon name="thumb_up" outlined />
					</button>
				{/if}
				{#if score <= 0}
					<button class={downKlass} on:click={() => applyScore(-1)} title="Bad response">
						<Icon name="thumb_down" outlined />
					</button>
				{/if}
			</div>
		</div>
	</div>
</div>
