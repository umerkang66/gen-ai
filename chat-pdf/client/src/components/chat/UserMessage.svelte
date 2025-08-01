<script lang="ts">
	import { marked } from 'marked';

	export let content = '';
</script>

<div class="flex justify-end">
	<div class="max-w-[80%] lg:max-w-[70%]">
		<div class="bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-2xl rounded-br-md px-4 py-3 shadow-lg">
			<div class="prose prose-invert max-w-none">
				{@html marked(content, { breaks: true, gfm: true })}
			</div>
		</div>
		<div class="flex items-center justify-end mt-2 space-x-2">
			<div class="w-6 h-6 bg-gradient-to-r from-primary-500 to-primary-600 rounded-full flex items-center justify-center">
				<span class="material-icons text-white text-xs">person</span>
			</div>
			<span class="text-xs text-neutral-500 dark:text-neutral-400">You</span>
		</div>
	</div>
</div>
