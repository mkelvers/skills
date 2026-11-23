# Classes, functions and state

The codebase decides its overall structure. If it is built from service classes, write service classes. If it is built from modules of functions, hooks or a functional core, write that. Never introduce a second paradigm beside the existing one, and never restructure code you weren't asked to change.

The rest of this file is for choices the project leaves open: a new project, a new area with no precedent, or the inside of a single file.

## Classes for concepts, functions for small work

JavaScript and TypeScript support both styles fully, and experienced engineers disagree about which to favour. The user's preference is to organise any non-trivial concept as a class that owns it, and keep small stateless work as plain functions. The aim is that each concept lives in one place, with a small public surface and the detail hidden inside.

Make it a **class** when:

- several operations share state, an invariant or a lifecycle: a cache, a connection, a parser, a session;
- several operations take the same value and only make sense together;
- the concept will grow, and keeping its operations together keeps them discoverable.

Keep it a **function** when:

- it is a stateless transformation or calculation;
- nothing else operates on the same data;
- the framework expects functions: components, hooks, route handlers, loaders.

The signal is the same value being passed around, not the number of functions.

```ts
// ❌ Three loose functions threading the same string; nothing names what it is.
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

```ts
// ✅ One concept, one place: everything you can ask of an identifier.
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

```ts
// ✅ Equally right: one stateless operation stays a function.
export function cents(amount: number): string {
	return `${(amount / 100).toFixed(2)} €`;
}
```

Two failure modes sit on either side. **Function sprawl** is dozens of small module functions passing the same data around with no name for the concept they serve; it is the clutter this preference exists to prevent. **Classitis** is many tiny classes that each hide almost nothing, or classes with only static members, which are namespaces pretending to be objects. Avoid both.

## Writing a class

- Every method uses the instance. Logic that doesn't belongs outside the class or inline.
- Keep state private (`#field`, or the project's convention) and expose methods, not fields to mutate.
- Keep the public surface small. A class whose many public methods each do a little is shallow: callers learn a lot and gain little.
- Constructors validate their input and assign. Async setup goes in a named creation method, with the constructor made private, so a half-built object is never in use:

  ```ts
  export class Manifest {
      private constructor(private readonly entries: readonly Entry[]) {}

      static async load(path: string): Promise<Manifest> {
          return new Manifest(await readEntries(path));
      }
  }
  ```

- Prefer composition. Inherit for a true is-a, or when a framework requires it (custom errors, framework base classes).
- One main class per file. A small private class that only that file uses can sit beside it.

## Helpers

A separate helper costs the reader a jump away and back. It has to pay for that.

- **Used once:** write it inside the function that uses it.
- **Used a few times and short:** usually inline too. Keep it separate when the logic must stay identical in every place.
- **Used widely, or real logic with a meaning of its own:** a named function, or a method on the class that owns the data.
- **Don't create a file, class or module just to hold one or two small functions.**

```ts
// ❌ A one-line helper with one caller, in a place of its own.
function slug(title: string): string {
	return title.trim().toLowerCase().replaceAll(/\s+/gu, "-");
}

export function articlePath(article: Article): string {
	return `/articles/${slug(article.title)}`;
}
```

```ts
// ✅ The step is named where it happens.
export function articlePath(article: Article): string {
	const slug = article.title.trim().toLowerCase().replaceAll(/\s+/gu, "-");

	return `/articles/${slug}`;
}
```

When a long algorithm reads better as named steps, name them even if each runs once. A name earns its place when it tells the reader *what* happens and spares them reading *how*. Don't extract three obvious lines.

## State

Give mutable state an owner: an instance, a closure, or a store the framework provides. A module-level variable that several functions reassign makes independent users of the module affect each other, and tests share it.

```ts
// ❌ Every importer shares this one session.
let current: Session | undefined;

export function signIn(session: Session) {
	current = session;
}
```

```ts
// ✅ Each owner has its own.
export class Sessions {
	#current: Session | undefined;

	signIn(session: Session) {
		this.#current = session;
	}
}
```

One deliberate process-wide instance, such as a connection pool or a logger, is fine. Where a framework gives module-level variables per-instance meaning, as component scripts do, the framework's meaning applies.

## Constants

Write a constant used in one place where it is used, as a named local when the name explains a magic value.

Keep anything that must be created once at module level or as a static field: compiled regular expressions and schemas on hot paths, formatters, caches, registries, pools. Moving those into a function body rebuilds them on every call.

## No thin wrappers

Don't write a function whose whole body forwards its arguments to another call. It adds a name to learn and a hop to follow, and does nothing.

```ts
// ❌ Callers could call fetchOrder directly.
export function getOrder(id: string) {
	return fetchOrder(http, id);
}
```

A function earns its place when it holds real logic, owns a contract callers depend on (validation, retries, translating errors), or is a boundary the architecture defines, such as a repository, port or adapter. A designed layer is not a wrapper, even when one method happens to forward.

## Abstractions

Before writing an API other code will depend on, settle what the caller provides, what it gets back, what can fail, what state exists and who owns it. Then build the smallest surface that covers that. Every exported member is a promise you'll have to keep, so don't export something just because the implementation already has it.

An interface needs more than one real implementation, or callers that must depend on the contract on its own. A lone `PaymentServiceImpl` behind a `PaymentService` interface is two names to maintain for nothing; write the class. When several providers really share a contract, the interface names the capability they share.

- Wait for the third similar case before extracting a shared abstraction. Duplication is cheaper to undo than the wrong abstraction, which every later change has to fight.
- An abstraction must hide more than it costs to learn. If callers still need to know how it works inside, it isn't helping.
- Don't add options or parameters for callers that don't exist yet.
