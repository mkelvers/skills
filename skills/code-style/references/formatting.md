# Formatting and control flow

Run the project's formatter first. These rules cover what it leaves open, and they hold in every codebase unless the formatter or the project's written style says otherwise.

## Objects: one property per line

Give every property of an object literal, object type or interface its own line, with a trailing comma where the language allows one. Do the same for each variant of a union of object types, and for an options object passed beside other arguments, even when it has a single property.

The reader finds a field by scanning one column. On a packed line they have to read across, and a one-field change rewrites the whole line in the diff.

```ts
// ❌ Three fields on one line; adding a fourth rewrites it.
const options = { retries: 2, timeoutMs: 500, signal };

// ❌ The variants run together, so their difference is hard to see.
type Result = { ok: true; value: number } | { ok: false; error: Error };
```

```ts
// ✅ One field per line.
const options = {
	retries: 2,
	timeoutMs: 500,
	signal,
};

// ✅ Each variant is a block; comparing them is comparing two short columns.
type Result =
	| {
			ok: true;
			value: number;
	  }
	| {
			ok: false;
			error: Error;
	  };
```

Leave alone what the formatter owns and keeps collapsing, such as destructuring in a parameter list or `for (const { id } of rows)`. Fighting the formatter only produces churn. Some formatters keep an object expanded once you expand it but never expand one themselves (Prettier and oxfmt with `objectWrap: "preserve"`), so write it expanded the first time.

## Blank lines between steps

A function body is a short sequence of steps: declarations, each guard, the work, the result. Put one blank line between steps, and around any statement that spans several lines. Lines that form one step stay together.

The blank line is the paragraph break. Without it the reader has to read every line to find where a step ends.

```ts
// ❌ Lookup, guard, work and result in one block.
async function publish(id: string) {
	const draft = await drafts.get(id);
	if (!draft) {
		return null;
	}
	const page = render(draft);
	await pages.save(page);
	return page.url;
}
```

```ts
// ✅ Four steps, four paragraphs.
async function publish(id: string) {
	const draft = await drafts.get(id);

	if (!draft) {
		return null;
	}

	const page = render(draft);
	await pages.save(page);

	return page.url;
}
```

## Guards and nesting

Handle the exceptional case first and return, so the main path runs at the left margin. Aim for at most two levels of nesting in a function. A third level usually means a guard is missing or the inner block is a separate idea.

```ts
// ❌ Three conditions, three levels; the work is buried at the bottom right.
for (const order of orders) {
	if (order.paid) {
		if (order.address) {
			if (!shipped.has(order.id)) {
				queue.push(order);
			}
		}
	}
}
```

```ts
// ✅ Skip what doesn't qualify, then do the work at the top level.
for (const order of orders) {
	const ready = order.paid && order.address;

	if (!ready || shipped.has(order.id)) {
		continue;
	}

	queue.push(order);
}
```

Don't reach the target by moving three lines into a function called once; that trades depth for a jump elsewhere in the file. A nested loop that *is* the algorithm, such as comparing every pair, can stay nested.

## Branches and ternaries

Use `if`/`else` or an early return for anything that does work, and for choices between more than two values. Keep ternaries for picking one of two plain values on one readable line. If the project bans ternaries entirely, follow the project.

A ternary puts two ideas on one line. That works for `"on" : "off"`. It stops working once either side is a call, a nested ternary or a side effect.

```ts
// ❌ Nested, with calls on both sides.
const client = override ? override.connect() : cached ? cached : pool.acquire();

// ❌ A ternary used as a statement.
playing ? player.pause() : player.play();
```

```ts
// ✅ Two plain values.
const label = active ? "Active" : "Inactive";

// ✅ Work goes in branches.
if (playing) {
	player.pause();
} else {
	player.play();
}
```

Where ternaries are banned, assign a typed variable in an `if`, or return from a small block. Don't declare an untyped `let value;`; it widens to `any`.

Handle every case of a closed union or enum explicitly, with a `switch` or a chain of guards that ends in an exhaustiveness check, so adding a case later fails to compile instead of falling through.

## Name compound conditions

When an `if` or `while` joins more than two operands with `&&` or `||`, give the condition a name. The name says what the checks mean together, which is what the reader actually wants to know. (`??` picks a value and doesn't count.)

```ts
// ❌ The reader has to work out what four checks add up to.
if (user && user.verified && !user.banned && plan !== "free") {
	unlock();
}
```

```ts
// ✅ The name states the decision.
const entitled = user?.verified && !user.banned && plan !== "free";

if (entitled) {
	unlock();
}
```

## Name meaningful intermediate values

Introduce a variable when its name explains a domain concept, makes a non-obvious value clear, or ties together uses that must agree. Repetition alone is a reason to look closer, not a reason to extract.

```ts
// ❌ The same calculated time decides whether to retry and when; nothing says so.
if (now + delayMs >= expiresAt) {
	return;
}

await schedule(now + delayMs);
```

```ts
// ✅ `retryAt` also tells the reader the scheduler takes an absolute time, not a delay.
const retryAt = now + delayMs;

if (retryAt >= expiresAt) {
	return;
}

await schedule(retryAt);
```

Leave `return price + tax;` or `if (now >= expiresAt)` as they are; the expression already says what it means. Remember that extracting an expression can change how often it runs, which matters when it has side effects or reads changing state.

## One step per line

Don't nest calls so deeply that the reader evaluates inside out. Name the middle step when it means something on its own.

```ts
// ❌ Read from the inside out.
return sortByDate(dedupe(rows.map(toOrder))).slice(0, limit);
```

```ts
// ✅ What the orders are, then what is returned.
const orders = dedupe(rows.map(toOrder));

return sortByDate(orders).slice(0, limit);
```

## Ordinary syntax

- `const` by default, `let` when the value is reassigned, never `var`.
- `for...of` when the index doesn't matter; an array method when its name states the operation (`some`, `find`, `flatMap`).
- Don't copy a growing accumulator on every pass (`[...acc, item]` inside `reduce`); the work grows quadratically. Push into a local array or use a loop.
- Use template literals for interpolation. Use optional chaining and `??` only where absence is expected, never to paper over data that should be there (see [errors.md](errors.md)).
