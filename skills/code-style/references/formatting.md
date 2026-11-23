# Formatting and control flow

Follow the local formatter for punctuation, indentation, and destructuring. Where it leaves room, give each property of a multi-property literal or object type its own line, with trailing commas where supported. Expand object-shaped union variants into separate blocks. Give an options object beside other arguments its own lines, even for one property. Keep a standalone one-property object compact.

## Named steps

❌ **Don't** compress multiple domain steps into one return. It hides which comparison the caller actually needs.

```ts
return normalize(title).includes(normalize(query));
```

✅ **Do** name the normalized inputs when the steps matter to the reader. Separate the work from the result.

```ts
const normalizedTitle = normalize(title);
const normalizedQuery = normalize(query);

return normalizedTitle.includes(normalizedQuery);
```

## Branches

Use guards when they clear the main path. Name a compound test when the name expresses a meaningful decision. Group guards, work, and results with blank lines. A return immediately completing a guard can follow it directly. Keep a concise arrow body for one plain call or value.

❌ **Don't** put multiple operations or nested ternaries into value selection. Avoid extracting tiny functions solely to meet a depth target.

✅ **Do** use explicit `if` or `else` for branching work and handle every case of a closed union. Keep a nested loop when keeping it together makes the algorithm clearer. Use a simple ternary for two readable values where local policy permits it.

```ts
const status = active ? "active" : "inactive";
```

## Object layout

❌ **Don't** pack unrelated fields into one line. It makes a field harder to spot and edits harder to scan.

```ts
const options = { retries: 2, timeoutMs: 500 };
```

✅ **Do** give each field its own line. Keep the same layout for multi-property type declarations.

```ts
const options = {
	retries: 2,
	timeoutMs: 500,
};
```
