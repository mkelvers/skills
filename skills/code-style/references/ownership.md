# Modules and state

Place the rule with the domain that owns it. Group cohesive functionality in a module and keep private helpers out of its exports. Keep closely related internal declarations together when splitting them would turn one operation into a tour through several files.

❌ **Don't** expose a helper just to make it callable from the same module. Avoid a static-only class whose sole job is to group two stateless functions.

✅ **Do** keep the transformation private and export the actual contract.

```ts
function normalize(title: string): string {
	return title.trim().toLowerCase();
}

export function matches(title: string, query: string): boolean {
	const normalizedTitle = normalize(title);
	const normalizedQuery = normalize(query);

	return normalizedTitle.includes(normalizedQuery);
}
```

❌ **Don't** keep an instance-specific value in a shared mutable binding. It makes otherwise independent users of the module affect each other.

```ts
let value = 0;

export function next(): number {
	value += 1;

	return value;
}
```

✅ **Do** put instance-specific state and the operations that maintain it on its owner. This counter gives each owner an independent sequence.

```ts
class Sequence {
	#value = 0;

	next(): number {
		this.#value += 1;

		return this.#value;
	}
}
```

Module-owned process state can be appropriate when the module explicitly owns its initialization and cleanup. Choose classes for state, identity, invariants, or lifecycle, and for framework contracts that call for them. Keep constructors synchronous. Use a named async creation method when initialization must finish before use.

Keep import-time side effects deliberate. Avoid cycles and keep imports pointed toward the public entry point of the owner. A layer should own policy, change semantics, protect an invariant, implement a meaningful protocol, or perform work callers actually need. Inline pure forwarding wrappers unless the boundary itself is part of a contract.
