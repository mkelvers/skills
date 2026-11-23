# Markup and styling

Style rules for HTML, JSX and component templates. Visual design belongs to the design skill, and framework mechanics to the framework's docs.

## Use the element that means the thing

Native elements bring behaviour for free: keyboard support, focus, roles for assistive technology, and meaning for search engines. A `div` brings none of it.

- Use `nav`, `main`, `section`, `article`, lists, `time`, `button` and `a` for what they mean. Keep `div` and `span` for layout.
- Use a `button` for an action and a link for navigation, never a clickable `div`.
- Give icon-only controls a name with `aria-label`. The `title` attribute's hover tooltip is unreliable and most assistive technology ignores it.
- Give informative images descriptive alt text.
- Don't render empty elements to draw a dot, bar or divider. Use a pseudo-element or a border on an element that already exists.
- Self-close elements and components that have no children.

## Utility classes

With Tailwind and similar, the classes on an element are its style sheet. Keep them where the element is.

- Write classes on the element. Class strings stored in constants or maps send the reader elsewhere to find out what an element looks like.
- Express a component's variants with a variant helper, either the project's or `class-variance-authority`, instead of chains of `variant === "x" && "..."`.
- Merge conditional classes and a caller's `class` with the project's class helper.

```svelte
<!-- ❌ The base style lives in a constant, and the variants in a chain of conditions. -->
<script>
	const base = "inline-flex items-center px-3";
</script>

<button class={cn(base, variant === "ghost" && "bg-transparent", variant === "primary" && "bg-accent")}>
```

```svelte
<!-- ✅ One declaration lists every variant; the element asks for one. -->
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

Use the project's shared components instead of restyling raw elements on one page. When a shared component misbehaves, fix it in the component, so every use gets the fix. Don't add a prop to a shared component to serve a single caller; style from the call site with the existing API, or raise the need.
