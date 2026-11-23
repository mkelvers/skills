# Markup and styling

Style rules for HTML, JSX and component templates. Layout and visual design belong to the design skill; framework mechanics come from the framework's docs.

## Elements

- Use the element that means the thing (`nav`, `main`, `section`, `article`, `ul`, `time`, `button`, `a`). `div` and `span` are for layout only.
- A `button` for actions, a link for navigation, never a clickable `div`.
- Don't render empty elements to draw dots, bars or dividers. Use a pseudo-element or a border on an element that already exists.
- Give icon-only controls a name with `aria-label`, not the `title` attribute.
- Informative images get descriptive alt text.
- Elements and components without children self-close.

## Utility classes

For Tailwind and similar:

- Write classes on the element. Don't store class strings in constants or maps.
- Component variants go through a variant helper (the project's, or `class-variance-authority`), not chains of `variant === "x" && "..."`.
- Conditional classes and a caller's `class` are merged with the project's class helper.

❌ **Don't**

```svelte
<script>
	const base = "inline-flex items-center px-3";
</script>

<button class={cn(base, variant === "ghost" && "bg-transparent", variant === "primary" && "bg-accent")}>
```

✅ **Do**

```svelte
<script module>
	export const button = cva("inline-flex items-center px-3", {
		variants: {
			variant: {
				ghost: "bg-transparent",
				primary: "bg-accent",
			},
		},
	});
</script>

<button class={cn(button({ variant }), className)}>
```

## Shared components

Use the project's shared components instead of restyling raw elements. When one misbehaves, fix it in the component rather than at one call site. Don't add a prop to a shared component to serve a single caller; style from the call site with the existing API, or raise it.
