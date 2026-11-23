# Types, schemas and generics

A type should describe real information, not whatever TypeScript happens to allow.

## Interfaces and type aliases

Use either for an object contract and follow the project's habit. Use an interface when declaration merging is part of the design. Use a type alias for unions and composition.

## Discriminated unions

When a value can be in several states, give each state its own shape and a field that tells them apart. Each state then carries only the fields that make sense for it, and the compiler stops you reading a field that isn't there.

```ts
// ❌ Every combination is representable, including ok: true with a reason.
interface ImportResult {
	ok: boolean;
	imported?: number;
	reason?: string;
}
```

```ts
// ✅ Two states, each with exactly its own data.
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

## Schemas for data from outside

Types don't exist at runtime, so they can't check a request body, an API response, an environment variable or decoded JSON. For that data, the runtime schema is the source of truth, and the type comes from it. Declaring both by hand gives you two definitions that drift apart.

```ts
// ❌ The same shape twice; nothing keeps them in step.
interface NewOrder {
	sku: string;
	quantity: number;
}

const NewOrderSchema = z.object({
	sku: z.string().min(1),
	quantity: z.number().int().positive(),
});
```

```ts
// ✅ One schema; the type follows it.
export const NewOrderSchema = z.object({
	sku: z.string().min(1),
	quantity: z.number().int().positive(),
});

export type NewOrder = z.infer<typeof NewOrderSchema>;
```

After `NewOrderSchema.parse(body)`, the result already has the right type. Don't wrap the call in a function that only forwards to it, or annotate the result again. Use the project's validator; Zod is only the example here.

Interfaces still fit contracts that aren't data from outside: service capabilities, class contracts, plugin APIs.

## `unknown` and assertions

`unknown` is the honest type for a value you haven't checked yet: parsed JSON, a caught error, a message from another process. A parser may take `unknown` and return a domain type. Keep that boundary visible and hand the checked type to the rest of the code.

```ts
// ❌ The cast claims a shape that nobody checked.
const order = JSON.parse(text) as NewOrder;
```

```ts
// ✅ The schema checks it, and inference carries the result.
const order = NewOrderSchema.parse(JSON.parse(text));
```

Prefer inference, narrowing and annotated assignments to assertions. Where the project allows them, use an assertion only on the one expression whose invariant was established elsewhere, and make that evidence clear. Avoid chains like `as unknown as T`, unexplained non-null `!`, and `any` used to skip validation. Follow the project's stricter rules where it has them.

## Generics

A generic should preserve a real relationship between types: what goes in determines what comes out.

```ts
// ✅ The item type flows from input to output.
export function chunk<T>(values: readonly T[], size: number): T[][] {
	// ...
}

// ❌ The type parameter adds nothing a plain type wouldn't.
export function wrap<T>(value: T) {
	return {
		value,
	};
}
```

Start concrete. Add a type parameter when a second real use needs it, and stop before domain code turns into a framework.

## Absence

Use `null` or `undefined` when absence is a real state in the domain, and model it explicitly. Don't make a field optional to avoid deciding when it exists. If a value must exist after creation, make the constructor or the schema require it.
