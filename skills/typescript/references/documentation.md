# Documentation

Doc comments let callers use code without reading its implementation. Write them for what the signature can't say.

## What to document

Add TSDoc to exported functions, classes, methods, types and configuration when they have requirements the types don't show: assumptions about input, guarantees about output, side effects, ownership, lifecycle, and failures callers should handle differently. Follow the project's own documentation rules where it has stricter ones.

```ts
// ❌ Restates the name; tells the caller nothing.
/** Gets the order. */
async function order(id: string): Promise<Order> {}
```

```ts
// ✅ Says what the types can't: which identifier, and what happens when it's missing.
/**
 * Loads an order by its public order number.
 *
 * @throws {@link OrderNotFoundError} When no order has that number.
 */
async function order(number: string): Promise<Order> {}
```

## Interfaces

Say why the contract exists and what every implementation must guarantee. That is the part an implementer can't infer.

```ts
/**
 * Charges customers through an external payment provider.
 *
 * Implementations return a `Receipt` for every successful charge and never
 * retry on their own; the caller decides whether a failure is retried.
 */
export interface PaymentProvider {
	charge(order: Order): Promise<Receipt>;
}
```

## Examples

Add an `@example` where the intended use isn't obvious from the signature: lifecycles, builders, schedulers, overloaded functions, configuration objects, resource ownership. Skip them on trivial functions, where they only add length.

## Describe behaviour, not the algorithm

Documentation should still be true after the implementation changes.

```text
❌ Loops through the array and pushes each value into another array.
✅ Groups orders by customer, keeping their original order within each group.
```
