# API design

A good API makes correct use obvious and incorrect use hard. Callers should learn little and get a lot.

## Design the contract first

For any API other code will depend on, settle these before writing the implementation: what the caller provides, what it gets back, what can fail, what state exists and who owns it, what lifecycle it has, and which invariants must hold. Then build the smallest surface that satisfies them.

Don't expose something just because the implementation already has it. Every exported member is a promise you'll have to keep.

## One implementation needs no interface

Interfaces earn their place when several real implementations share a contract, or when callers must depend on the contract independently of any implementation.

```ts
// ❌ A contract with one implementation: two names to maintain, nothing gained.
interface PaymentService {
	charge(order: Order): Promise<Receipt>;
}

class PaymentServiceImpl implements PaymentService {
	// ...
}
```

```ts
// ✅ One implementation: just the class.
class PaymentService {
	// ...
}

// ✅ Several real implementations: the interface names the capability they share.
interface PaymentProvider {
	charge(order: Order): Promise<Receipt>;
}

class StripeProvider implements PaymentProvider {
	// ...
}

class AdyenProvider implements PaymentProvider {
	// ...
}
```

## Constructors

A constructor establishes a valid object: it validates its inputs, normalises configuration and initialises owned state. It does no asynchronous work, because a half-built object can't be awaited safely.

When setup must be asynchronous, make the constructor private and add a static creation method that finishes the work before returning the object.

```ts
export class Manifest {
	private constructor(private readonly entries: readonly Entry[]) {}

	/** Reads and validates the manifest at `path`. */
	static async load(path: string): Promise<Manifest> {
		const entries = await readEntries(path);

		return new Manifest(entries);
	}
}
```

Don't add a factory when `new Manifest(entries)` already says it clearly.

## Inheritance

Inherit when the subclass truly is a specialised version of the base, the shared behaviour belongs to the abstraction, and a subclass can stand in anywhere the base is used. Extending `Error` qualifies.

Don't inherit to share a few helper methods. Composition, an object holding the helper it needs, keeps unrelated capabilities apart.
