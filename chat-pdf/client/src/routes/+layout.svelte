<script lang="ts">
	import '../app.css';
	import 'material-icons/iconfont/material-icons.css';
	import { onMount } from 'svelte';
	import Navbar from '$c/Navbar.svelte';
	import ErrorModal from '$c/ErrorModal.svelte';
	import { getUser, auth } from '$s/auth';

	$: user = $auth.user;

	onMount(() => {
		if (user === null) {
			getUser();
		}
	});
</script>

<ErrorModal />
<div class="min-h-screen bg-gradient-to-br from-neutral-50 via-white to-neutral-100 dark:from-neutral-900 dark:via-neutral-800 dark:to-neutral-900">
	<Navbar />
	<main class="container mx-auto px-4 py-8 max-w-7xl">
		<slot />
	</main>
</div>
