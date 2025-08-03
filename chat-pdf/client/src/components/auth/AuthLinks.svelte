<script lang="ts">
	import { auth } from '$s/auth';
</script>

{#if $auth.user}
	<div class="flex items-center space-x-3">
		<div class="flex items-center space-x-2 text-secondary-600">
			<span class="material-icons text-lg">account_circle</span>
			<span class="font-medium">{$auth.user.email}</span>
		</div>
		<a
			href="/auth/signout"
			class="btn-secondary text-sm px-4 py-2"
		>
			<span class="material-icons text-sm mr-1">logout</span>
			Sign Out
		</a>
	</div>
{:else}
	<div class="flex items-center space-x-3">
		<a
			href="/auth/signin"
			class="text-secondary-600 hover:text-primary-600 font-medium transition-colors duration-200 flex items-center space-x-1"
		>
			<span class="material-icons text-lg">login</span>
			<span>Login</span>
		</a>
		<a
			href="/auth/signup"
			class="btn-primary text-sm px-4 py-2"
		>
			<span class="material-icons text-sm mr-1">person_add</span>
			Sign Up
		</a>
	</div>
{/if}
