# Naming

A name is read far more often than it is written, and almost always at the call site, by someone who doesn't have the definition open. Write for that reader. Doc comments carry the detail; the name only has to be true and recognisable.

Follow the project's conventions: casing, file names, prefixes its framework requires, its domain vocabulary. Within those, apply the rules below.

## The call-site test

Read the call with its import or owner in view, and ask three things:

- Would you say it shorter out loud? Then shorten it.
- Could someone without the file open guess what it does? If not, it is too short.
- Does it read like a sentence? Then the function probably does too much or lives in the wrong place. Fix that rather than growing the name.

The user judges names partly by instinct. A name can pass every rule below and still read badly at the call site, and then it is still wrong.

## Short, with the context in the owner

Aim for one or two words. More than three is rare, and usually means the name is carrying context that belongs to something else.

Leave out what the folder, file or owner already says. Inside `billing/` it is `charge()`, not `chargeBilling()`; on a `Connection` it is `close()`, not `closeConnection()`. When dropping the context makes a bare call unclear, put the context in an owner rather than back in the name.

```ts
// ❌ Every name repeats "cache", because nothing else says it.
import { closeCache, flushCache } from "./cache";

await flushCache();
await closeCache();
```

```ts
// ✅ The owner says it once, and each method says only what it does.
import { cache } from "./cache";

await cache.flush();
await cache.close();
```

Types and classes keep their full name (`PaymentError`), because they travel without their file. In a project that imports plain functions by name, keep that pattern and choose names that stand alone; `flushCache` is fine there. Don't restructure a module just to shorten its names.

## Words that say nothing

- **Abbreviations made by dropping letters:** `cfg`, `ctx`, `err`, `idx`, `msg`, `btn`, `val`, `tmp`. Write the word. Abbreviations that are the thing's normal name (`id`, `url`, `html`, `api`) are fine, and so is a one-letter name in a loop a few lines long.
- **Filler at the end:** `data`, `info`, `list`, `map`, `helper`, `util`, `manager`, `impl`, `base`. `userList` is `users`; `configManager` names nothing.
- **Type or mechanism suffixes:** `searchUrl`, `fetchAsync`, `saveIfNeeded`, `getXFor`. In `href={search(query)}`, the attribute already says it's a link.
- **`handle` at the start:** `handleClick` says when a function runs, not what it does. Name the action: `submit`, `toggle`, `dismiss`. Many React codebases use `handleX` by convention; there, follow the project.

## Name by role, not by type

Name a variable for what it does in this code. Use `sender` and `recipient`, not `user1` and `user2`; `retryAt`, not `timestamp`. When the type is weak (a `string`, a `number`), the name has to carry the meaning: `orderId`, `timeoutMs`.

## Verbs, nouns and questions

- Functions with effects are verbs: `save`, `refresh`, `dismiss`.
- Values and getters without effects are nouns: `orders`, `retryAt`, `invoice.total`.
- When an operation exists in both forms, the names show which one changes things: `sort()` sorts in place, `sorted()` returns a copy.
- Booleans read as a state or an answered question: `ready`, `entitled`, `order.paid`. Add `is` or `has` only when the bare word is ambiguous.
- A function that starts something and returns how to undo it is named for what it starts: `const stop = watcher.start()`.

## Keep names true

Never shorten a name into a word that means something else. `valid` hides what was checked; when several kinds of validity are in play, `credentialsValid` is the right length.

Use one word per concept, and the project's word for it. If the project keeps a glossary, use its terms exactly.

## Renaming public names

Renaming an export changes a contract. Update every reference, including templates and doc-comment links. Keep strings that leave the code unchanged: API schema ids, error codes sent to clients, database tables and columns, serialized keys. A rename that changes a wire format is a migration, not a rename.
