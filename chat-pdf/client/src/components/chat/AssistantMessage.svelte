<script lang="ts">
	import { marked } from 'marked';

	export let content = '';
</script>

<div class="flex justify-start">
	<div class="max-w-2xl">
		<div class="flex items-start space-x-2">
			<div class="w-6 h-6 bg-gradient-to-br from-accent-500 to-primary-500 rounded-full flex items-center justify-center shadow-soft flex-shrink-0">
				<span class="material-icons text-white text-xs">smart_toy</span>
			</div>
			<div class="glass-effect rounded-xl rounded-bl-md px-4 py-3 shadow-soft">
				<div class="prose prose-secondary max-w-none text-sm">
					{@html marked(content, { breaks: true, gfm: true })}
				</div>
			</div>
		</div>
	</div>
</div>
