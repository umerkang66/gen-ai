<script lang="ts">
	import classNames from 'classnames';
	export let disabled = false;
	export let className = '';
	export let variant: 'primary' | 'secondary' | 'outline' = 'primary';
	export let size: 'sm' | 'md' | 'lg' = 'md';
</script>

<button
	type="submit"
	class={classNames(
		'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-300 transform hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2',
		{
			// Variants
			'bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white shadow-soft hover:shadow-medium focus:ring-primary-500': variant === 'primary',
			'bg-white/80 backdrop-blur-sm border border-secondary-200 text-secondary-700 hover:bg-white hover:border-primary-300 hover:text-primary-700 shadow-soft hover:shadow-medium focus:ring-primary-500': variant === 'secondary',
			'bg-transparent border-2 border-primary-500 text-primary-600 hover:bg-primary-50 shadow-soft hover:shadow-medium focus:ring-primary-500': variant === 'outline',
			
			// Sizes
			'px-3 py-2 text-sm': size === 'sm',
			'px-6 py-3 text-base': size === 'md',
			'px-8 py-4 text-lg': size === 'lg',
			
			// Disabled state
			'opacity-50 cursor-not-allowed transform-none hover:transform-none': disabled,
		},
		className
	)}
	{disabled}
>
	<slot />
</button>
