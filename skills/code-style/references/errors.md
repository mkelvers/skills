# Errors and missing data

Use the project's error model, whether that is exceptions, result types or error values. Inside it, two things are off the table: dropping a failure, and inventing data to cover a gap. Both let the program carry on in a wrong state, and both throw away the information someone will need to find the cause.

## Handle an error or let it travel

A handler that does nothing, only logs, or returns a placeholder is not handling anything. The caller believes the operation worked.

```ts
// ❌ The write failed; the caller thinks it succeeded.
try {
	await orders.save(order);
} catch (error) {
	console.error(error);
}

// ❌ Every failure, including bugs, becomes "no thumbnail".
const thumbnail = await resize(image).catch(() => undefined);
```

```ts
// ✅ Let it propagate to code that can report it.
await orders.save(order);

// ✅ Catch the failure you expect, handle it on purpose, and let the rest through.
try {
	return await resize(image);
} catch (error) {
	if (error instanceof UnsupportedFormatError) {
		return image;
	}

	throw error;
}
```

Catch where the code can do something useful: recover, translate the error for its caller, or report it. That is usually a boundary such as a request handler, a job runner or a UI action, not every function in between. When you translate an error, keep the original as its `cause`.

## Don't fake missing data

A required value that is missing is a bug somewhere upstream. Covering it with placeholder text or a made-up number hides the bug and shows the user something false.

```ts
// ❌ "Unknown" and 0 look like real data.
const title = book.title ?? "Unknown";
const year = book.year || 0;
```

```ts
// ✅ Fail where the gap is found, with enough detail to trace it.
if (!book.title) {
	throw new Error(`Book ${book.id} has no title`);
}
```

A real default for a value that is optional by design is fine (`sort ?? "newest"`); set it once, where input is parsed, rather than at every use. In a UI, show absence honestly by leaving the field out or showing an empty state.

## Asynchronous work

Await every promise the operation depends on. When you start work in the background on purpose, give it its own error handling and mark the choice as intentional (`void task()` in TypeScript). Many runtimes exit on an unhandled rejection.

Remove `console.log`, `debugger` and `alert` before finishing. Diagnostics that should stay go through the project's logger.
