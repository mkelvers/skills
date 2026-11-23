# Formatting and control flow

These rules decide how code looks on the page. They apply in every project, whatever its architecture. Run the project's formatter first; apply these rules to everything the formatter leaves open. Give way only where the project's formatter or written style rules enforce something different.

Contents: [Objects](#objects-one-property-per-line) · [Blank lines](#blank-lines-between-groups) · [Guards and nesting](#guards-and-nesting) · [Branches and ternaries](#branches-and-ternaries) · [Compound conditions](#name-compound-conditions) · [Intermediate values](#name-meaningful-intermediate-values) · [One step per line](#one-step-per-line) · [Ordinary syntax](#ordinary-syntax)

## Objects: one property per line

**Always.** Every object literal, object type, interface, struct literal and object-shaped union variant with more than one member puts each member on its own line, with a trailing comma where the language allows it. Write single-property literals expanded too when they are assigned or passed as options.

Why: a field is found by scanning down one column. A packed line hides fields, and a one-field edit shows up as a whole-line change in the diff.

❌ **Don't**

```ts
// Three ideas on one line; adding a field rewrites the line.
const options = { retries: 2, timeoutMs: 500, signal };

// Union variants run together and are hard to compare.
type Result = { ok: true; value: number } | { ok: false; error: Error };

// An options object squeezed in beside other arguments.
rmSync(directory, { force: true, recursive: true });
```

✅ **Do**

```ts
const options = {
	retries: 2,
	timeoutMs: 500,
	signal,
};

// Each variant is its own block, so the difference between them is visible.
type Result =
	| {
			ok: true;
			value: number;
	  }
	| {
			ok: false;
			error: Error;
	  };

rmSync(directory, {
	force: true,
	recursive: true,
});
```

Leave alone what the formatter owns and keeps collapsing, such as destructuring in a parameter list (`({ params }) =>`), an inline parameter type, or `for (const { id } of rows)`. Fighting the formatter only produces churn.

Some formatters keep an expanded object expanded but never expand a new one (Prettier-style `objectWrap: "preserve"`). Write it expanded the first time.

## Blank lines between groups

**Always.** A function body reads as groups separated by one blank line: declarations, each guard, the work, the result. A multi-line statement gets a blank line on both sides.

Why: the blank line is the paragraph break. Without it the reader has to parse every line to find where one step ends.

❌ **Don't**

```ts
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

✅ **Do**

```ts
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

Consecutive single-line declarations or calls that form one step stay together.

## Guards and nesting

**Always.** Handle the exceptional case first and return, so the main path runs at the left margin. Aim for two levels of nesting inside a function. A third level usually means a guard is missing or the inner block is a separate idea.

❌ **Don't**

```ts
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

✅ **Do**

```ts
for (const order of orders) {
	const ready = order.paid && order.address;

	if (!ready || shipped.has(order.id)) {
		continue;
	}

	queue.push(order);
}
```

Don't meet the depth target by pulling three lines into a tiny function called once. That trades nesting for a jump elsewhere in the file. A nested loop that is the algorithm (comparing every pair, walking a grid) can stay nested.

## Branches and ternaries

**Always.** Use `if`/`else` or an early return for anything that does work or chooses between more than two plain values. A ternary is acceptable only when it picks one of two simple values and fits on one readable line. A project that bans ternaries completely wins.

Why: a ternary holds two ideas on one line. That works for `"on" : "off"` and fails the moment either side is a call, a nested ternary or a side effect.

❌ **Don't**

```ts
// Two calls and a nested ternary in one expression.
const client = override ? override.connect() : cached ? cached : pool.acquire();

// A ternary used for side effects.
playing ? player.pause() : player.play();
```

✅ **Do**

```ts
const label = active ? "Active" : "Inactive";

if (playing) {
	player.pause();
} else {
	player.play();
}
```

Where ternaries are banned, a value that depends on a condition becomes an early return inside a small block, or a typed variable assigned in an `if`. Never leave the variable untyped (`let x;`), which widens its type.

```ts
let label: string = "Off";

if (active) {
	label = "On";
}
```

Handle every case of a closed union or enum explicitly: a `switch` or a chain of guards that ends in an exhaustiveness check.

## Name compound conditions

**Always.** When an `if` or `while` joins more than two operands with `&&` or `||`, give the condition a name. `??` picks a value and doesn't count.

❌ **Don't**

```ts
if (user && user.verified && !user.banned && plan !== "free") {
	unlock();
}
```

✅ **Do**

```ts
// The name says what the four checks mean together.
const entitled = user?.verified && !user.banned && plan !== "free";

if (entitled) {
	unlock();
}
```

## Name meaningful intermediate values

Introduce a variable when it names a domain concept, makes a non-obvious value or decision clear, or keeps uses that must agree tied to the same calculation. Repetition by itself is a reason to look at the expression, and the surrounding logic determines whether extraction helps.

❌ **Don't** leave a shared scheduling decision implicit. Here the same calculated time determines whether the retry fits within the window and when it should run.

```ts
if (now + delayMs >= expiresAt) {
	return;
}

await schedule(now + delayMs);
```

✅ **Do** name the value the branches share. `retryAt` also makes it clear that the scheduler receives an absolute time rather than a delay.

```ts
const retryAt = now + delayMs;

if (retryAt >= expiresAt) {
	return;
}

await schedule(retryAt);
```

Keep `return price + tax;` or `if (now >= expiresAt)` direct when the expression already communicates its purpose. A local earns its place when its name helps the reader understand the code.

Extracting an expression can change when or how often it runs. Check that the change preserves behavior when the expression has side effects or reads mutable state.

## One step per line

**Always.** Don't nest calls three deep so the reader has to evaluate inside out. Name the middle step when it has a meaning of its own.

❌ **Don't**

```ts
return sortByDate(dedupe(rows.map(toOrder))).slice(0, limit);
```

✅ **Do**

```ts
const orders = dedupe(rows.map(toOrder));

return sortByDate(orders).slice(0, limit);
```

## Ordinary syntax

- `const` by default, `let` only for reassignment, never `var`.
- `for...of` when the index doesn't matter. An array method when its name states the operation (`some`, `find`, `flatMap`).
- Never copy a growing accumulator on each pass (`[...acc, x]` or `{ ...acc, [k]: v }` inside `reduce`). That is quadratic. Mutate a local accumulator or use a loop.
- Template literals for interpolation. Optional chaining and `??` only where absence is valid, never to paper over required data (see [errors](errors.md)).
