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

<div class="space-y-12 animate-fade-in">
	<!-- Header -->
	<div class="text-center space-y-4">
		<h1 class="text-4xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
			Performance Analytics
		</h1>
		<p class="text-secondary-600 text-lg max-w-2xl mx-auto">
			Track and analyze the performance of your AI chat interactions
		</p>
	</div>

	<!-- LLM Scores -->
	<div class="glass-effect rounded-2xl p-8 shadow-large">
		<div class="flex items-center space-x-3 mb-6">
			<div class="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center shadow-soft">
				<span class="material-icons text-white">psychology</span>
			</div>
			<div>
				<h2 class="text-2xl font-bold text-secondary-800">LLM Performance</h2>
				<p class="text-secondary-500">Language Model Response Quality</p>
			</div>
		</div>
		
		{#if llmScores}
			<BarChart startingColor={{ r: 59, g: 130, b: 246 }} data={llmScores} />
		{:else}
			<div class="text-center py-12">
				<div class="w-16 h-16 bg-gradient-to-br from-secondary-100 to-secondary-200 rounded-full flex items-center justify-center mx-auto mb-4">
					<span class="material-icons text-2xl text-secondary-400">analytics</span>
				</div>
				<p class="text-secondary-500">No LLM scores available yet</p>
			</div>
		{/if}
	</div>

	<!-- Retriever Scores -->
	<div class="glass-effect rounded-2xl p-8 shadow-large">
		<div class="flex items-center space-x-3 mb-6">
			<div class="w-12 h-12 bg-gradient-to-br from-accent-500 to-accent-600 rounded-xl flex items-center justify-center shadow-soft">
				<span class="material-icons text-white">search</span>
			</div>
			<div>
				<h2 class="text-2xl font-bold text-secondary-800">Retriever Performance</h2>
				<p class="text-secondary-500">Document Retrieval Accuracy</p>
			</div>
		</div>
		
		{#if retrieverScores}
			<BarChart startingColor={{ r: 217, g: 70, b: 239 }} data={retrieverScores} />
		{:else}
			<div class="text-center py-12">
				<div class="w-16 h-16 bg-gradient-to-br from-secondary-100 to-secondary-200 rounded-full flex items-center justify-center mx-auto mb-4">
					<span class="material-icons text-2xl text-secondary-400">analytics</span>
				</div>
				<p class="text-secondary-500">No retriever scores available yet</p>
			</div>
		{/if}
	</div>

	<!-- Memory Scores -->
	<div class="glass-effect rounded-2xl p-8 shadow-large">
		<div class="flex items-center space-x-3 mb-6">
			<div class="w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center shadow-soft">
				<span class="material-icons text-white">memory</span>
			</div>
			<div>
				<h2 class="text-2xl font-bold text-secondary-800">Memory Performance</h2>
				<p class="text-secondary-500">Conversation Context Retention</p>
			</div>
		</div>
		
		{#if memoryScores}
			<BarChart startingColor={{ r: 34, g: 197, b: 94 }} data={memoryScores} />
		{:else}
			<div class="text-center py-12">
				<div class="w-16 h-16 bg-gradient-to-br from-secondary-100 to-secondary-200 rounded-full flex items-center justify-center mx-auto mb-4">
					<span class="material-icons text-2xl text-secondary-400">analytics</span>
				</div>
				<p class="text-secondary-500">No memory scores available yet</p>
			</div>
		{/if}
	</div>
</div>
