# Functions, classes and state

Contents: [Whose decision](#whose-decision) · [Classes or functions](#classes-or-functions) · [Helpers](#helpers) · [Writing a class](#writing-a-class) · [State](#state) · [Constants](#constants) · [No thin wrappers](#no-thin-wrappers) · [Abstractions](#abstractions)

## Whose decision

How a codebase is structured belongs to the codebase. If it is built from service classes, write service classes. If it is built from modules of functions, hooks or a functional core, write that. Don't introduce a second paradigm beside the existing one, and don't restructure code you aren't asked to change.

The preferences below apply where the project hasn't decided: a new project, a new area with no precedent, or a project the user owns.

## Classes or functions

**The user's preference:** organise non-trivial logic around classes that own one concept, with plain functions for small, stateless work. JavaScript and TypeScript support both styles fully; neither is the "correct" one. Published guidance splits on this, and the sources are in [sources.md](sources.md).

Use a **class** when:

- several operations share state, an invariant or a lifecycle (a cache, a connection, a parser, a session);
- several operations take the same value and only make sense together (`new Identifier(text).words`, `.last`, `.startsWith(...)`);
- the concept will grow, and keeping its operations in one place keeps them discoverable. A class with a small public surface hiding a lot of work is the goal ("deep", in Ousterhout's terms).

Use **plain functions** when:

- the work is a stateless transformation or calculation;
- the function stands alone and nothing else operates on the same data;
- the framework expects functions (React components and hooks, route handlers, loaders).

Avoid both failure modes:

- **Function sprawl:** dozens of small module functions passing the same value around, with no name for the concept they serve. This is the clutter the class preference exists to prevent.
- **Classitis:** many tiny classes that each hide almost nothing, and classes with only static members (a namespace pretending to be an object; use a module).

❌ **Don't**

```ts
// Helpers threading the same string through, with no name for what it is.
function words(name: string) {
	return name.split(/(?=[A-Z])/u).map((word) => word.toLowerCase());
}

function lastWord(name: string) {
	return words(name).at(-1);
}

function startsWith(name: string, prefix: string) {
	return words(name)[0] === prefix;
}
```

✅ **Do**

```ts
// One concept, one place: everything you can ask of an identifier.
class Identifier {
	readonly #text: string;

	constructor(text: string) {
		this.#text = text;
	}

	get words(): string[] {
		return this.#text.split(/(?=[A-Z])/u).map((word) => word.toLowerCase());
	}

	get last(): string | undefined {
		return this.words.at(-1);
	}

	startsWith(prefix: string): boolean {
		return this.words[0] === prefix;
	}
}
```

✅ **Also right:** a single stateless function stays a function.

```ts
export function cents(amount: number): string {
	return `${(amount / 100).toFixed(2)} €`;
}
```

## Helpers

**Default.** A helper is separate only when the separation pays for itself.

- **Used once:** write it inside the function or method that uses it.
- **Used a few times and short:** usually inline. Keep it separate when the repeated logic must stay identical everywhere.
- **Used widely, or real logic with its own meaning:** a named function, or a method on the class that owns the data.
- **Don't create a file, class or module just to hold one or two small functions.**

A long algorithm can still read better as named steps, even when each runs once. Name a step when the name tells the reader *what* happens and saves them reading *how*. Don't extract three obvious lines.

❌ **Don't**

```ts
// A one-line helper, called once, in a place of its own.
function slug(title: string): string {
	return title.trim().toLowerCase().replaceAll(/\s+/gu, "-");
}

export function articlePath(article: Article): string {
	return `/articles/${slug(article.title)}`;
}
```

✅ **Do**

```ts
export function articlePath(article: Article): string {
	const slug = article.title.trim().toLowerCase().replaceAll(/\s+/gu, "-");

	return `/articles/${slug}`;
}
```

## Writing a class

- Every method uses the instance. Logic that doesn't need it belongs outside the class, or inline.
- No class with only static members.
- State is private (`#field`, or the project's convention). Expose methods and getters, not fields to mutate.
- Constructors only assign. Async setup goes in a named creation method (`await Index.open(path)`).
- Keep the public surface small. Many public methods that each do a little is a shallow class.
- Prefer composition. Inherit only for a true is-a, or when a framework requires it (custom errors, framework base classes).
- One main class per file. A small private class only that file uses may sit beside it.

## State

**Default.** Mutable state has an owner: an instance, a closure, or a store the framework provides. Don't keep it in a module-level variable that several functions reassign; independent users then affect each other and tests share it.

❌ **Don't**

```ts
let current: Session | undefined;

export function signIn(session: Session) {
	current = session;
}
```

✅ **Do**

```ts
export class Sessions {
	#current: Session | undefined;

	signIn(session: Session) {
		this.#current = session;
	}
}
```

One deliberate process-wide instance (a connection pool, a logger) is fine. Where a framework gives module-level variables per-instance meaning (component scripts), the framework's meaning applies.

## Constants

**Default.** A constant used in one place is written in that place, as a named local when the name explains a magic value.

Anything that must be created once stays created once: compiled regular expressions and schemas on a hot path, formatters, caches, registries, pools. Moving them into a function body rebuilds them on every call. Keep them at module level or as a static field of the class that uses them.

## No thin wrappers

**Default.** Don't write a function whose whole body forwards its arguments to another call. Call the target directly.

❌ **Don't**

```ts
export function getOrder(id: string) {
	return fetchOrder(http, id);
}
```

A function earns its place when it holds real logic, owns a contract callers depend on (validation, retries, translating errors), or is a boundary the architecture defines (a repository, a port, an adapter). A designed layer is not a wrapper, even when one method happens to forward.

## Abstractions

- Don't generalise from one case. Wait until the third similar use before extracting a shared abstraction; duplication is cheaper than the wrong abstraction.
- An abstraction must hide more than it costs to learn. If callers still need to know how it works, it isn't helping.
- Options and parameters for hypothetical callers are clutter. Add them when a real caller needs them.
