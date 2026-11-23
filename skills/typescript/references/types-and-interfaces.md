# Types, interfaces, schemas, and generics

Types should model real information, not whatever TypeScript happens to permit.

## Interfaces

Use an interface or a type alias for object contracts. Follow local convention and use an interface when intentional declaration merging is part of the design. When one class is the only implementation, use the class (see [api-design.md](api-design.md)).

```ts
export interface Scheduler {
  /** Starts registered jobs. */
  start(): void;

  /** Stops all active jobs. */
  stop(): void;
}
```

## Type aliases

Use aliases for unions and type composition. Prefer discriminated unions over loosely related optional fields, since each state then carries only its own information:

```ts
export type ImportResult =
  | {
      ok: true;
      imported: number;
    }
  | {
      ok: false;
      reason:
        | "unsupported-format"
        | "invalid-data";
    };
```

Avoid this shape, where invalid combinations are representable:

```ts
interface ImportResult {
  ok: boolean;
  imported?: number;
  reason?: string;
}
```

## Runtime schemas

Interfaces and types don't exist at runtime, so they can't validate external data (request bodies, API responses, env vars, webhooks, config files, decoded JSON). For those, the runtime schema is the one source of truth and the type derives from it.

Avoid, because the structure now exists twice and can drift:

```ts
interface CreateAnimeRequest {
  title: string;
  episodes: number;
}

const CreateAnimeRequestSchema = z.object({
  title: z.string().min(1),
  episodes: z.number().int().nonnegative()
});
```

Prefer:

```ts
export const CreateAnimeRequestSchema = z.object({
  title: z.string().min(1),
  episodes: z.number().int().nonnegative()
});

export type CreateAnimeRequest =
  z.infer<typeof CreateAnimeRequestSchema>;
```

This is one of the legitimate uses of `typeof`: TypeScript needs the type of a runtime declaration. Use type-position `typeof` when the runtime declaration owns the type.

After parsing, `request` already has the inferred type. Add no wrapper or annotation.

```ts
const request = CreateAnimeRequestSchema.parse(body);
```

Interfaces still fit contracts that aren't runtime data: service capabilities, class contracts, extensible object APIs.

## Unknown values and assertions

Use `unknown` when an input or caught value really is unknown. A parser may accept `unknown` and return a domain value. Keep its boundary clear and pass the validated type to business logic. Call a schema directly when a separate function would merely forward the call.

❌ **Don't** cast decoded JSON into a trusted type. The cast cannot establish what the sender provided.

✅ **Do** verify the value before using it. Prefer the project validator or a direct check for a small contract. Let inference carry the result of validation.

Prefer inference, checked assignments, and narrowing before reaching for an assertion. Where project policy permits it, limit an assertion to the expression whose invariant was established independently. State the evidence if it is not apparent at the use site. Avoid assertion chains, unjustified non-null assertions, and `any` as an escape from validation. Follow local restrictions on assertions and unknown signatures.

## Generics

A generic should represent a real relationship.

```ts
// Good
export interface Page<TItem> {
  items: readonly TItem[];
  nextCursor: string | null;
}

// Good
export function chunk<T>(
  values: readonly T[],
  size: number
): T[][] {
  // ...
}

// Bad: the wrapper has no semantic purpose
export function wrap<T>(value: T) {
  return {
    value
  };
}
```

Before adding one, ask which types vary, what relationship must stay intact, whether it preserves information or removes real duplication, and whether a concrete domain type would be clearer. Don't turn domain code into a generic framework early.

## Nullability

Use `null` or `undefined` when absence is part of the domain, and model a meaningful absence as an explicit state. Don't make a field nullable to avoid modeling states properly. If a title must exist after creation, make that true at construction or validation time. Defaults are covered in [errors-and-results.md](errors-and-results.md).
