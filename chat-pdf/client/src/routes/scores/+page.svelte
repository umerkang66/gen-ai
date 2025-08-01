<script lang="ts">
	import type { PageData } from './$types';
	import BarChart from '$c/BarChart.svelte';
	import AuthGuard from '$c/AuthGuard.svelte';

	export let data: PageData;

	$: llmScores = data.scores && data.scores['llm'];
	$: retrieverScores = data.scores && data.scores['retriever'];
	$: memoryScores = data.scores && data.scores['memory'];
</script>

<AuthGuard />

<div class="min-h-screen py-8">
	<!-- Header Section -->
	<div class="text-center mb-12 animate-fade-in">
		<h1 class="text-4xl md:text-6xl font-display font-bold text-neutral-800 dark:text-white mb-4">
			Performance 
			<span class="gradient-text">Analytics</span>
		</h1>
		<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
			Track and analyze the performance of your AI models across different metrics
		</p>
	</div>

	<!-- Stats Overview -->
	<div class="grid md:grid-cols-3 gap-6 mb-12">
		<div class="card p-6 text-center">
			<div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-primary-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">psychology</span>
			</div>
			<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">LLM Performance</h3>
			<p class="text-neutral-600 dark:text-neutral-400">Language model accuracy and response quality</p>
		</div>
		
		<div class="card p-6 text-center">
			<div class="w-16 h-16 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">search</span>
			</div>
			<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">Retriever Performance</h3>
			<p class="text-neutral-600 dark:text-neutral-400">Document retrieval and relevance scoring</p>
		</div>
		
		<div class="card p-6 text-center">
			<div class="w-16 h-16 bg-gradient-to-r from-accent-500 to-accent-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
				<span class="material-icons text-white text-2xl">memory</span>
			</div>
			<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">Memory Performance</h3>
			<p class="text-neutral-600 dark:text-neutral-400">Conversation context and memory retention</p>
		</div>
	</div>

	<!-- Charts Section -->
	<div class="space-y-12">
		<!-- LLM Scores -->
		<div class="card p-8 animate-slide-up">
			<div class="flex items-center mb-6">
				<div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-primary-600 rounded-xl flex items-center justify-center mr-4">
					<span class="material-icons text-white text-xl">psychology</span>
				</div>
				<div>
					<h2 class="text-2xl font-display font-bold text-neutral-800 dark:text-neutral-200">LLM Scores</h2>
					<p class="text-neutral-600 dark:text-neutral-400">Language model performance metrics</p>
				</div>
			</div>
			{#if llmScores}
				<div class="bg-white/50 dark:bg-neutral-800/50 rounded-xl p-6">
					<BarChart startingColor={{ r: 59, g: 130, b: 246 }} data={llmScores} />
				</div>
			{:else}
				<div class="text-center py-12 text-neutral-500 dark:text-neutral-400">
					<span class="material-icons text-4xl mb-4">analytics_off</span>
					<p>No LLM scores available yet</p>
				</div>
			{/if}
		</div>

		<!-- Retriever Scores -->
		<div class="card p-8 animate-slide-up">
			<div class="flex items-center mb-6">
				<div class="w-12 h-12 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-xl flex items-center justify-center mr-4">
					<span class="material-icons text-white text-xl">search</span>
				</div>
				<div>
					<h2 class="text-2xl font-display font-bold text-neutral-800 dark:text-neutral-200">Retriever Scores</h2>
					<p class="text-neutral-600 dark:text-neutral-400">Document retrieval performance metrics</p>
				</div>
			</div>
			{#if retrieverScores}
				<div class="bg-white/50 dark:bg-neutral-800/50 rounded-xl p-6">
					<BarChart startingColor={{ r: 236, g: 72, b: 153 }} data={retrieverScores} />
				</div>
			{:else}
				<div class="text-center py-12 text-neutral-500 dark:text-neutral-400">
					<span class="material-icons text-4xl mb-4">analytics_off</span>
					<p>No retriever scores available yet</p>
				</div>
			{/if}
		</div>

		<!-- Memory Scores -->
		<div class="card p-8 animate-slide-up">
			<div class="flex items-center mb-6">
				<div class="w-12 h-12 bg-gradient-to-r from-accent-500 to-accent-600 rounded-xl flex items-center justify-center mr-4">
					<span class="material-icons text-white text-xl">memory</span>
				</div>
				<div>
					<h2 class="text-2xl font-display font-bold text-neutral-800 dark:text-neutral-200">Memory Scores</h2>
					<p class="text-neutral-600 dark:text-neutral-400">Conversation memory and context retention</p>
				</div>
			</div>
			{#if memoryScores}
				<div class="bg-white/50 dark:bg-neutral-800/50 rounded-xl p-6">
					<BarChart startingColor={{ r: 234, g: 179, b: 8 }} data={memoryScores} />
				</div>
			{:else}
				<div class="text-center py-12 text-neutral-500 dark:text-neutral-400">
					<span class="material-icons text-4xl mb-4">analytics_off</span>
					<p>No memory scores available yet</p>
				</div>
			{/if}
		</div>
	</div>

	<!-- Performance Tips -->
	<div class="mt-12 card p-8">
		<h3 class="text-2xl font-display font-bold text-neutral-800 dark:text-neutral-200 mb-6">Performance Tips</h3>
		<div class="grid md:grid-cols-2 gap-6">
			<div class="space-y-3">
				<div class="flex items-start space-x-3">
					<span class="material-icons text-primary-500 mt-1">lightbulb</span>
					<div>
						<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Improve LLM Performance</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Use more specific prompts and provide better context for more accurate responses.</p>
					</div>
				</div>
				<div class="flex items-start space-x-3">
					<span class="material-icons text-secondary-500 mt-1">search</span>
					<div>
						<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Enhance Retrieval</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Upload more relevant documents and use better chunking strategies.</p>
					</div>
				</div>
			</div>
			<div class="space-y-3">
				<div class="flex items-start space-x-3">
					<span class="material-icons text-accent-500 mt-1">memory</span>
					<div>
						<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Memory Optimization</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Maintain conversation context and use memory-efficient strategies.</p>
					</div>
				</div>
				<div class="flex items-start space-x-3">
					<span class="material-icons text-neutral-500 mt-1">trending_up</span>
					<div>
						<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Monitor Trends</h4>
						<p class="text-sm text-neutral-600 dark:text-neutral-400">Regularly check these metrics to track improvements over time.</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
