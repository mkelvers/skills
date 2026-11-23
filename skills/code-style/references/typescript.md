# TypeScript

What is particular to TypeScript. Layout, naming, helpers, classes and the general error rules are in the other references and apply here unchanged. The project's own choices come first: its validator, its error model, its rules on assertions.

Contents: [Boundaries](#check-data-at-the-boundary) · [Assertions](#let-the-compiler-see-the-evidence) · [Unions](#make-invalid-states-unrepresentable) · [Generics](#generics) · [Absence](#absence) · [Errors](#errors) · [TSDoc](#tsdoc) · [Reviewing](#reviewing-typescript)

## Check data at the boundary

Types don't exist at runtime, so they can't check a request body, an API response, an environment variable, a queue message or decoded JSON. That data is `unknown` until a schema proves its shape. Parse it once, where it enters, and let the type come from the schema. After that, business logic works with real types and never checks again.

```ts
// ❌ The same shape declared twice; nothing keeps them in step.
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

The result of `NewOrderSchema.parse(body)` already has the right type. Don't wrap the call in a function that only forwards to it, and don't annotate the result again. Use the project's validator; Zod is only the example.

A parse often uncovers bugs a cast was hiding: a field that arrives as `null`, a number that arrives as a string. Fix where the data comes from, for example by filtering the query or modelling the `null`, rather than loosening the schema until it passes.

Interfaces still fit contracts that aren't data from outside: service capabilities, class contracts, plugin APIs. Use an interface or a type alias for object contracts as the project does; use an alias for unions and composition.

## Let the compiler see the evidence

`unknown` is the honest type for a value nobody has checked yet: parsed JSON, a caught error, a message from another process. A parser may take `unknown` and return a domain type. Keep that boundary visible, and hand the checked type to the rest of the code.

An assertion does no checking at runtime; it only stops the compiler from telling you that you're wrong. Prefer, in order: a parse, a narrowing check, inference from a better-typed source, an annotated assignment (`const checked: Order = value`).

```ts
// ❌ The cast claims a shape nobody checked; the sender decides what arrives.
const order = JSON.parse(text) as NewOrder;
```

```ts
// ✅ The schema checks it, and inference carries the result.
const order = NewOrderSchema.parse(JSON.parse(text));
```

Where the project allows assertions, limit one to the single expression whose invariant was established somewhere the compiler can't follow, and make that evidence clear. Avoid chains like `as unknown as T`, unexplained non-null `!`, and `any` used to skip validation. `as const` and `satisfies` are fine: they check rather than override.

## Make invalid states unrepresentable

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

Switch over the discriminant and end with an exhaustiveness check (`const unreachable: never = result`), so adding a state later fails to compile everywhere it isn't handled.

## Generics

A type parameter should carry a real relationship: what goes in determines what comes out.

```ts
// ✅ The item type flows from input to output.
export function chunk<T>(values: readonly T[], size: number): T[][] {
  // ...
}
```

```ts
// ❌ The parameter adds nothing a plain type wouldn't.
export function wrap<T>(value: T) {
  return {
    value,
  };
}
```

Start concrete. Add a type parameter when a second real use needs it, and stop before domain code turns into a framework.

## Absence

Use `null` or `undefined` when absence is a real state in the domain, and model it explicitly. Don't make a field optional to avoid deciding when it exists. If a value must exist once an object is created, make the constructor or the schema require it. Defaults belong in the schema too (`z.number().default(20)`), set once rather than at every read.

## Errors

The general rules are in [errors.md](errors.md). In TypeScript:

- **Throw error classes callers can recognise,** not a generic `Error` with a code hidden in the message. Set `name` to the class name.
- **Keep the cause** when translating a lower-level error: `new PaymentFailedError(order.id, { cause: error })`.
- **A caught value is `unknown`.** Narrow it with `instanceof` before reading it; don't cast it.
- **Return a discriminated union for expected outcomes** the caller is meant to branch on, such as validation or an import that can be rejected. The type forces the check. Don't do this for failures the caller can't act on; that only spreads error handling across every call site.

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

## TSDoc

Write TSDoc on exported functions, classes, methods, types and configuration when they have requirements the types don't show: assumptions about input, guarantees about output, side effects, ownership, lifecycle, and failures callers should handle differently. Follow the project's own documentation rules where they are stricter.

```ts
// ❌ Restates the name; tells the caller nothing.
/** Gets the order. */
export async function order(id: string): Promise<Order> {}
```

```ts
// ✅ Says what the types can't: which identifier, and what happens when it's missing.
/**
 * Loads an order by its public order number.
 *
 * @throws {@link OrderNotFoundError} When no order has that number.
 */
export async function order(number: string): Promise<Order> {}
```

On an interface, say why the contract exists and what every implementation must guarantee; that is what an implementer can't infer. Add an `@example` where the intended use isn't obvious from the signature: lifecycles, builders, overloads, configuration objects. Describe behaviour, not the algorithm, so the comment stays true when the implementation changes.

## Reviewing TypeScript

On top of the general rules, look for:

- casts from parsed or external data, and interfaces duplicating a schema;
- an interface with a single implementation, a factory where `new` would do, a generic with one use;
- `as unknown as`, unexplained `!`, `any` standing in for validation;
- optional fields modelling what should be a union of states;
- thrown strings, lost `cause`, and caught errors read without narrowing;
- exported contracts whose obligations aren't documented.

Before finishing, ask: could someone reading only the public types and docs use this correctly?
