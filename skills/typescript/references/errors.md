# Errors and results

Model a failure by how the caller is expected to handle it. The code-style skill covers the rules for every language: never drop an error, never fake missing data. This file covers how to shape errors in TypeScript.

## Throw typed errors for exceptional failure

When an operation can't keep its contract, throw an error class callers can recognise, not a generic `Error` with a code hidden in the message.

```ts
// ❌ Callers have to parse the message to know what happened.
throw new Error("NOT_FOUND");
```

```ts
// ✅ A class callers can catch by type, carrying the detail they need.
export class OrderNotFoundError extends Error {
	constructor(readonly id: string) {
		super(`Order ${id} does not exist`);
		this.name = "OrderNotFoundError";
	}
}
```

When translating a lower-level error, pass the original as `cause` so the chain survives into logs:

```ts
try {
	return await gateway.charge(order);
} catch (error) {
	throw new PaymentFailedError(order.id, {
		cause: error,
	});
}
```

The caught value is `unknown`; that is correct. Narrow it if you need to inspect it, and don't cast it to quiet the compiler.

## Return a result for expected outcomes

When failure is a normal outcome the caller is expected to branch on, such as validation or an import that may be rejected, return a discriminated union instead of throwing. The caller can't forget to handle it, because the type forces the check.

```ts
type ImportResult =
	| {
			ok: true;
			imported: number;
	  }
	| {
			ok: false;
			reason: "unsupported-format" | "invalid-data";
	  };
```

Don't turn every failure into a result. A result type for something the caller can't do anything about only pushes the error-handling to every call site.

## Set defaults once

A default belongs where input is parsed: the schema, configuration loading, or construction. Then the rest of the code reads a value that is always present.

```ts
// ❌ Every reader repeats the default, and they can disagree.
const limit = options.limit ?? 20;
```

```ts
// ✅ The schema decides once.
const Options = z.object({
	limit: z.number().int().positive().default(20),
});
```

A fallback on data that should always exist (`error.message ?? "Something went wrong"`) hides a broken invariant. Establish the invariant earlier instead.
