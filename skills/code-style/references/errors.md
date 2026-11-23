# Errors and missing data

Use the project's error model (exceptions, result types, error values). Within it, two things are never acceptable: dropping a failure, and pretending missing data is present. For TypeScript error and result design, see the TypeScript skill.

## Don't swallow errors

**Always.** A handler that does nothing, only logs, or returns a placeholder lets the program carry on in a wrong state and throws away the cause.

❌ **Don't**

```ts
try {
	await orders.save(order);
} catch (error) {
	// The write failed; the caller thinks it worked.
	console.error(error);
}

const thumbnail = await resize(image).catch(() => undefined);
```

✅ **Do**

```ts
// Let it propagate to code that can report it.
await orders.save(order);

// Or catch the failure you expect, and handle it on purpose.
try {
	return await resize(image);
} catch (error) {
	if (error instanceof UnsupportedFormatError) {
		return image;
	}

	throw error;
}
```

Catch where the code can recover, translate or report: a request handler, a job runner, a UI action. Not in every function on the way. When translating, keep the original error as the cause.

## Don't fake missing data

**Always.** Don't cover a missing required value with placeholder text or a made-up value.

❌ **Don't**

```ts
const title = book.title ?? "Unknown";
const year = book.year || 0;
```

✅ **Do**

```ts
// Required: its absence is a bug upstream, so fail where it is found.
if (!book.title) {
	throw new Error(`Book ${book.id} has no title`);
}
```

A real default for an optional value is fine (`sort ?? "newest"`), ideally set once where input is parsed. In a UI, show the absence honestly: leave the field out or show an empty state.

## Async

Await what the operation depends on. Work started deliberately in the background handles its own failure and is marked as intentional (`void task()` in TypeScript).

Remove `console.log`, `debugger` and `alert` before finishing; use the project's logger for diagnostics that should stay.
