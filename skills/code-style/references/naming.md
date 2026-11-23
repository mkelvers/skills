# Naming

A name has one job: let a reader who doesn't have the file open recognise what the thing is at the call site. A doc comment carries the detail. The name only has to be true and recognisable.

Follow the project's naming *conventions* (casing, file names, prefixes its framework requires, its domain vocabulary). Apply the quality rules below to every name you write inside those conventions.

The user judges names by instinct ("this ticks wrong"). The rules below capture what that instinct rejects and accepts. When a name passes every rule and still reads badly at the call site, it is still wrong.

## The test

Read the call site with its import or owner in view.

- If you would say it shorter out loud, shorten it.
- If someone without the file open couldn't guess what it does, it is too short.
- If it reads as a sentence, the function does too much or lives in the wrong place. Fix that instead of growing the name.

## Length

**Default.** Aim for one or two words; more than three is rare. There is no hard limit, but a name that needs four or more words is describing a responsibility that belongs to an owner (a module, a class, an object), or a function doing two jobs.

❌ **Don't**

```ts
calculateShippingCostForOrder(order);
maximumRetryDelayInMilliseconds;
getUserNotificationPreferences(userId);
```

✅ **Do**

```ts
// The owner carries "shipping", so the method only names the calculation.
shipping.cost(order);
maxDelayMs;
preferences.notifications(userId);
```

Names an external contract fixes are exempt: framework-required exports, protocol fields, database columns, third-party interface members.

## Don't repeat the context

**Default.** A value or function doesn't repeat a word its folder, file or owner already says. Inside `billing/`, it is `charge()`, not `chargeBilling()`. On a `Connection` class it is `close()`, not `closeConnection()`.

Types and classes keep their full name, because they travel without their file: `PaymentError` stays `PaymentError` wherever it is imported.

## Put the context in an owner

When dropping the context makes a bare call unclear, give the call an owner instead of a longer name: a class instance, a module namespace import, or an exported object of related functions, whichever the project already uses. The call site reads `owner.verb()`.

❌ **Don't**

```ts
import { closeCache, flushCache } from "./cache";

await flushCache();
await closeCache();
```

✅ **Do**

```ts
import { cache } from "./cache";

// Short names stay clear because "cache." is part of every call.
await cache.flush();
await cache.close();
```

In a project that already exports plain functions and imports them by name, keep that pattern and pick names that are clear bare (`flush` alone is not; `flushCache` is acceptable there). Don't restructure a module just to shorten its names.

## Words to avoid

**Default**, unless the project's conventions, a framework or an external contract use the word.

- **Abbreviations made by dropping letters:** `arr`, `btn`, `cb`, `cfg`, `ctx`, `err`, `idx`, `msg`, `num`, `obj`, `str`, `tmp`, `val`. Write the word. Abbreviations that are the normal name of the thing (`id`, `url`, `html`, `api`) are fine, and so is a one-letter name in a loop of a few lines.
- **Filler as the last word:** `async`, `base`, `data`, `fn`, `helper(s)`, `impl`, `info`, `later`, `list`, `manager`, `map`, `promise`, `util(s)`. `userList` is `users`. `configManager` names nothing.
- **`handle` as the first word.** `handleClick` says when it runs, not what it does. Name the action: `submit`, `toggle`, `dismiss`. Many React codebases use `handleX` by convention; there, follow the project.
- **Type or mechanism suffixes:** `searchUrl`, `searchHref`, `searchWith`, `getXFor`, `fetchAsync`, `saveIfNeeded`. `href={search({ query })}` already says it is a link. Name the concept: `search`.

## Name by role, not type

Name a variable or parameter for what it does in this code, not for its type. `recipient` and `sender`, not `user1` and `user2`; `retryAt`, not `timestamp`. When the type is weak (a `string`, a `number`, an `id`), the name has to carry the meaning: `orderId`, `timeoutMs`.

## Verbs, nouns and predicates

- Functions that act are verbs: `save`, `refresh`, `dismiss`.
- Values and getters are nouns: `orders`, `retryAt`, `invoice.total`.
- A pair of mutating and non-mutating operations is named so the difference shows: `sort()` changes in place, `sorted()` returns a copy.
- Booleans read as a state or an answered question: `ready`, `entitled`, `order.paid`. Use `is`/`has` only when the bare word would be ambiguous.
- A function that starts something and hands back how to undo it is named for what it starts: `const stop = watcher.start();` reads correctly. A function called `stop()` that starts something reads backwards.

## Keep names true

Never shorten a name into a word that means something else. `valid` hides what was checked. When several kinds of validity sit in the same function, `credentialsValid` is the right length.

Use the project's domain words, one word per meaning. If the project has a glossary, use its terms exactly, and add a new term there before using it. Never use two words for one concept or one word for two.

## Public names

Renaming an export is a contract change. Rename it only when you update every reference in the repository (including templates and doc-comment links), and keep strings outside the code unchanged: API schema ids, error codes sent to clients, database table and column names, serialized keys. A rename that changes a wire format is a migration, not a rename.
