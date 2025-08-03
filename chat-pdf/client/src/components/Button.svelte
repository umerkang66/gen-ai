<script lang="ts">
	import classNames from 'classnames';
	import { createEventDispatcher } from 'svelte';
	
	export let disabled = false;
	export let className = '';
	export let variant: 'primary' | 'secondary' | 'outline' | 'ghost' = 'primary';
	export let size: 'sm' | 'md' | 'lg' = 'md';
	
	const dispatch = createEventDispatcher();
	
	function handleClick(event: MouseEvent) {
		if (!disabled) {
			dispatch('click', event);
		}
	}
</script>

<button
	type="button"
	class={classNames(
		'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed',
		{
			// Variants
			'btn-primary': variant === 'primary',
			'btn-secondary': variant === 'secondary',
			'btn-outline': variant === 'outline',
			'text-neutral-600 hover:text-primary-600 hover:bg-neutral-100 dark:text-neutral-300 dark:hover:text-primary-400 dark:hover:bg-neutral-800': variant === 'ghost',
			
			// Sizes
			'px-3 py-1.5 text-sm': size === 'sm',
			'px-6 py-3 text-base': size === 'md',
			'px-8 py-4 text-lg': size === 'lg',
		},
		className
	)}
	{disabled}
	on:click={handleClick}
>
	<slot />
</button>
