# API design

A good API should make correct usage obvious and incorrect usage difficult.

## Design the contract before the implementation

For meaningful public APIs, determine:

- what the caller needs
- what the caller receives
- what can fail
- what state exists
- who owns that state
- what lifecycle exists
- what invariants must hold

Then implement the smallest surface that satisfies those requirements.

Do not expose implementation details simply because they already exist.

## Abstractions must justify themselves

Before introducing a new layer, ask what semantic value it provides.

Avoid wrappers like:

```ts
function getAnime(id: string) {
  return animeClient.getAnime(id);
}
```

unless `getAnime` establishes a meaningful domain boundary, adds behavior,
changes semantics, owns policy, or otherwise has a reason to exist.

A wrapper that merely forwards arguments and returns the result usually
makes navigation worse.

## Avoid interface/class duplication

Do not automatically create:

```ts
interface AnimeService {
  getAnime(id: string): Promise<Anime>;
}

class AnimeServiceImpl implements AnimeService {
  // ...
}
```

If there is one implementation and callers do not depend on a separate
contract, use:

```ts
class AnimeService {
  // ...
}
```

Interfaces are valuable when multiple implementations actually share a
meaningful contract:

```ts
interface MetadataProvider {
  getAnime(id: string): Promise<Anime>;
}

class AniListMetadataProvider implements MetadataProvider {
  // ...
}

class TmdbMetadataProvider implements MetadataProvider {
  // ...
}
```

The interface represents the capability.

The classes represent concrete providers.

## Functions versus classes

Choose based on ownership.

### Prefer functions when

- no persistent state exists
- the operation is naturally transformational
- there is no lifecycle
- several operations do not need to share invariants
- the behavior is independently useful

Example:

```ts
export function normalizeAnimeTitle(title: string): string {
  return title.trim().toLowerCase();
}
```

### Prefer classes when

A cohesive concept owns state or lifecycle.

Example:

```ts
export class TraktClient {
  private readonly baseUrl: URL;

  /**
   * Creates a Trakt API client.
   */
  constructor(options: TraktClientOptions) {
    this.baseUrl = new URL(options.baseUrl);
  }

  /**
   * Retrieves an anime entry from Trakt.
   */
  async getAnime(id: string): Promise<Anime> {
    // ...
  }
}
```

The class has a reason to exist because multiple operations share
configuration and behavior.

Do not create classes merely to hold functions.

Do not avoid classes merely because functions can technically accomplish
the same result.

## Constructors

Constructors establish valid object state.

They should generally:

- validate construction invariants
- normalize configuration
- initialize owned state

Avoid asynchronous initialization inside constructors.

If asynchronous construction is genuinely required, use an explicit static
creation method only when it improves the lifecycle:

```ts
export class Manifest {
  private constructor(
    private readonly entries: readonly ManifestEntry[]
  ) {}

  /**
   * Loads and validates a manifest.
   */
  static async load(path: string): Promise<Manifest> {
    const entries = await readManifest(path);

    return new Manifest(entries);
  }
}
```

Do not introduce factories when `new Class(...)` already expresses the
construction clearly.

## Inheritance

Inheritance should model an actual relationship.

Use it when:

- subclasses genuinely are specialized versions of the base type
- shared behavior belongs to the abstraction
- substitutability makes sense

Do not use inheritance solely to share a few helper methods.

Composition is usually clearer for unrelated capabilities.
