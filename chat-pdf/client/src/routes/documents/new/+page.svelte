<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import Alert from '$c/Alert.svelte';
	import Button from '$c/Button.svelte';
	import { documents, upload, clearErrors } from '$s/documents';
	import Progress from '$c/Progress.svelte';

	let files: FileList;
	let loading = false;
	let uploadComplete = false;
	let dragOver = false;
	let fileInput: HTMLInputElement;

	async function handleSubmit() {
		if (!files || files.length === 0) return;
		
		loading = true;
		const result = await upload(files[0]);
		if (result && !$documents.error) {
			uploadComplete = true;

			setTimeout(() => {
				goto('/documents');
				loading = false;
			}, 2000);
		} else {
			loading = false;
		}
	}

	function handleDragOver(event: DragEvent) {
		event.preventDefault();
		dragOver = true;
	}

	function handleDragLeave() {
		dragOver = false;
	}

	function handleDrop(event: DragEvent) {
		event.preventDefault();
		dragOver = false;
		
		if (event.dataTransfer?.files) {
			files = event.dataTransfer.files;
		}
	}

	function handleFileButtonClick() {
		fileInput?.click();
	}

	function handleFileChange() {
		// File selection handled by binding, no automatic upload
	}

	beforeNavigate(clearErrors);
</script>

<div class="min-h-screen py-8">
	<!-- Header Section -->
	<div class="text-center mb-12 animate-fade-in">
		<h1 class="text-4xl md:text-6xl font-display font-bold text-neutral-800 dark:text-white mb-4">
			Upload 
			<span class="gradient-text">Document</span>
		</h1>
		<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
			Upload your PDF documents to start chatting with your content
		</p>
	</div>

	<div class="max-w-2xl mx-auto">
		<div class="card p-8">
			<form on:submit|preventDefault={handleSubmit}>
				<!-- Upload Area -->
				<div 
					class="border-2 border-dashed border-neutral-300 dark:border-neutral-600 rounded-2xl p-8 text-center transition-all duration-200 {dragOver ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20' : 'hover:border-primary-400 dark:hover:border-primary-500'}"
					on:dragover={handleDragOver}
					on:dragleave={handleDragLeave}
					on:drop={handleDrop}
				>
					<div class="w-16 h-16 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
						<span class="material-icons text-white text-2xl">upload_file</span>
					</div>
					
					<h3 class="text-xl font-semibold text-neutral-800 dark:text-neutral-200 mb-2">
						{dragOver ? 'Drop your file here' : 'Upload your PDF document'}
					</h3>
					
					<p class="text-neutral-600 dark:text-neutral-400 mb-6">
						Drag and drop your PDF file here, or click to browse
					</p>
					
					<div class="space-y-4">
						<input
							bind:files
							bind:this={fileInput}
							type="file"
							accept=".pdf"
							id="file-input"
							class="hidden"
							on:change={handleFileChange}
						/>
						<button
							type="button"
							on:click={handleFileButtonClick}
							class="inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed btn-outline px-8 py-4 text-lg"
						>
							<span class="material-icons mr-2">folder_open</span>
							Choose File
						</button>
					</div>
					
					{#if files && files.length > 0}
						<div class="mt-6 p-4 {loading ? 'bg-blue-50 dark:bg-blue-900/20' : uploadComplete ? 'bg-green-50 dark:bg-green-900/20' : 'bg-yellow-50 dark:bg-yellow-900/20'} rounded-xl">
							<div class="flex items-center space-x-3">
								<div class="w-8 h-8 {loading ? 'bg-blue-500' : uploadComplete ? 'bg-green-500' : 'bg-yellow-500'} rounded-lg flex items-center justify-center">
									<span class="material-icons text-white text-sm">
										{loading ? 'upload' : uploadComplete ? 'check' : 'schedule'}
									</span>
								</div>
								<div>
									<p class="font-medium {loading ? 'text-blue-800 dark:text-blue-200' : uploadComplete ? 'text-green-800 dark:text-green-200' : 'text-yellow-800 dark:text-yellow-200'}">
										{files[0].name}
									</p>
									<p class="text-sm {loading ? 'text-blue-600 dark:text-blue-400' : uploadComplete ? 'text-green-600 dark:text-green-400' : 'text-yellow-600 dark:text-yellow-400'}">
										{(files[0].size / 1024 / 1024).toFixed(2)} MB
										{#if loading}
											- Uploading... ({$documents.uploadProgress}%)
										{:else if uploadComplete}
											- Upload Complete!
										{:else}
											- Ready to upload
										{/if}
									</p>
								</div>
							</div>
						</div>
					{/if}
				</div>

				<!-- Upload Progress -->
				{#if loading && !$documents.error}
					<div class="mt-6">
						<Progress progress={$documents.uploadProgress}>
							<Alert type="success">
								<div class="flex items-center space-x-2">
									<span class="material-icons">check_circle</span>
									<span>Upload Complete! Redirecting to documents...</span>
								</div>
							</Alert>
						</Progress>
					</div>
				{/if}

				<!-- Error Display -->
				{#if $documents.error}
					<div class="mt-6">
						<Alert type="error">
							<div class="flex items-center space-x-2">
								<span class="material-icons">error</span>
								<span>Error: {$documents.error}</span>
							</div>
						</Alert>
					</div>
				{/if}

				<!-- Submit Button -->
				{#if !loading}
					<div class="mt-8 flex justify-center">
						<Button 
							variant="primary" 
							size="lg" 
							disabled={!files || files.length === 0 || loading}
							className="w-full md:w-auto"
						>
							<span class="material-icons mr-2">cloud_upload</span>
							Upload Document
						</Button>
					</div>
				{/if}
			</form>
		</div>

		<!-- Features -->
		<div class="mt-12 grid md:grid-cols-3 gap-6">
			<div class="text-center space-y-3">
				<div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-primary-600 rounded-xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-lg">security</span>
				</div>
				<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Secure Upload</h4>
				<p class="text-sm text-neutral-600 dark:text-neutral-400">Your documents are encrypted and secure</p>
			</div>
			
			<div class="text-center space-y-3">
				<div class="w-12 h-12 bg-gradient-to-r from-secondary-500 to-secondary-600 rounded-xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-lg">auto_awesome</span>
				</div>
				<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">AI Processing</h4>
				<p class="text-sm text-neutral-600 dark:text-neutral-400">Advanced AI extracts and processes your content</p>
			</div>
			
			<div class="text-center space-y-3">
				<div class="w-12 h-12 bg-gradient-to-r from-accent-500 to-accent-600 rounded-xl flex items-center justify-center mx-auto">
					<span class="material-icons text-white text-lg">chat</span>
				</div>
				<h4 class="font-semibold text-neutral-800 dark:text-neutral-200">Instant Chat</h4>
				<p class="text-sm text-neutral-600 dark:text-neutral-400">Start chatting with your documents immediately</p>
			</div>
		</div>
	</div>
</div>
