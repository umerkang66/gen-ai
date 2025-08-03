<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import Alert from '$c/Alert.svelte';
	import Button from '$c/Button.svelte';
	import { documents, upload, clearErrors } from '$s/documents';
	import Progress from '$c/Progress.svelte';

	let files: FileList;
	let loading = false;
	let uploadComplete = false;

	async function handleSubmit() {
		if (!files || files.length === 0) return;
		
		loading = true;
		await upload(files[0]);
		if (!$documents.error) {
			uploadComplete = true;

			setTimeout(() => {
				goto('/documents');
				loading = false;
			}, 2000);
		} else {
			loading = false;
		}
	}

	beforeNavigate(clearErrors);
</script>

<div class="max-w-2xl mx-auto space-y-8">
	<!-- Header -->
	<div class="text-center space-y-4">
		<h1 class="text-4xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
			Upload Document
		</h1>
		<p class="text-secondary-600 text-lg">
			Upload a PDF document to start chatting with AI assistance
		</p>
	</div>

	<!-- Upload Card -->
	<div class="glass-effect rounded-2xl p-8 shadow-large">
		<form on:submit|preventDefault={handleSubmit} class="space-y-6">
			<!-- File Upload Area -->
			<div class="space-y-4">
				<label class="block text-sm font-medium text-secondary-700">
					Select PDF Document
				</label>
				
				<div class="relative">
					<input
						bind:files
						type="file"
						accept=".pdf"
						id="file-input"
						class="sr-only"
					/>
					
					<label 
						for="file-input" 
						class="flex flex-col items-center justify-center w-full h-32 border-2 border-dashed border-secondary-300 rounded-xl cursor-pointer bg-secondary-50 hover:bg-secondary-100 transition-colors duration-200"
					>
						<div class="flex flex-col items-center justify-center pt-5 pb-6">
							<span class="material-icons text-4xl text-secondary-400 mb-2">cloud_upload</span>
							<p class="mb-2 text-sm text-secondary-500">
								<span class="font-semibold">Click to upload</span> or drag and drop
							</p>
							<p class="text-xs text-secondary-400">PDF files only</p>
						</div>
					</label>
				</div>
				
				{#if files && files.length > 0}
					<div class="flex items-center space-x-3 p-4 bg-green-50 border border-green-200 rounded-xl">
						<span class="material-icons text-green-600">check_circle</span>
						<div>
							<p class="text-sm font-medium text-green-800">{files[0].name}</p>
							<p class="text-xs text-green-600">{(files[0].size / 1024 / 1024).toFixed(2)} MB</p>
						</div>
					</div>
				{/if}
			</div>

			<!-- Progress and Status -->
			{#if loading && !$documents.error}
				<div class="space-y-4">
					<Progress progress={$documents.uploadProgress} />
					<Alert type="success">
						<div class="flex items-center space-x-2">
							<span class="material-icons">check_circle</span>
							<span>Upload Complete! Returning to documents...</span>
						</div>
					</Alert>
				</div>
			{/if}

			{#if $documents.error}
				<Alert type="error">{$documents.error}</Alert>
			{/if}

			<!-- Submit Button -->
			{#if !loading}
				<Button 
					variant="primary" 
					size="lg" 
					className="w-full"
					disabled={!files || files.length === 0}
				>
					<span class="material-icons mr-2">upload_file</span>
					Upload Document
				</Button>
			{/if}
		</form>
	</div>

	<!-- Back Link -->
	<div class="text-center">
		<a 
			href="/documents" 
			class="text-secondary-600 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center justify-center space-x-1"
		>
			<span class="material-icons text-sm">arrow_back</span>
			<span>Back to Documents</span>
		</a>
	</div>
</div>
