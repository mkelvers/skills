# Documentation

Documentation describes contracts, intent, constraints, and behavior.

It should make the codebase easier to use without requiring callers to read
the implementation.

## Default rule

Use TSDoc when exported functions, types, classes, methods, or configuration have requirements the signature does not communicate. Document meaningful assumptions, guarantees, effects, ownership, and failures. Follow stricter project documentation rules. Explain non-obvious internal decisions where they matter.

Bad:

```ts
/**
 * Gets the anime.
 */
function getAnime() {}
```

Good:

```ts
/**
 * Retrieves the canonical anime record for the provided AniList identifier.
 *
 * @param id AniList media identifier.
 * @returns The matching anime.
 *
 * @throws {@link AnimeNotFoundError}
 * When no anime exists for the provided identifier.
 */
async function getAnime(id: number): Promise<Anime> {
  // ...
}
```

## Interfaces

Document why the contract exists and what implementations must guarantee.

```ts
/**
 * Provides metadata for anime from an external metadata source.
 *
 * Implementations must return normalized domain objects rather than
 * provider-specific response structures.
 */
export interface MetadataProvider {
  /**
   * Retrieves metadata for an anime.
   *
   * @param id Provider-specific media identifier.
   * @returns Normalized anime metadata.
   *
   * @throws {@link MetadataRequestError}
   * When the provider cannot be reached or returns an invalid response.
   */
  getAnime(id: string): Promise<AnimeMetadata>;
}
```

## Examples

Add examples where the intended usage is not immediately obvious.

Do not add examples to every trivial function.

Examples are particularly useful for:

- lifecycle APIs
- builders
- schedulers
- resource ownership
- generic utilities
- overloaded APIs
- configuration objects
- domain workflows

## Error documentation

If callers are expected to respond differently to different failures,
document those failures.

```ts
/**
 * Imports anime from an external file.
 *
 * @throws {@link UnsupportedImportFormatError}
 * When the provided format is not supported.
 *
 * @throws {@link InvalidImportDataError}
 * When the file does not match the expected schema.
 */
```

## Documentation should survive implementation changes

Prefer documenting semantics rather than internal algorithms.

Bad:

> Loops through the array and pushes each value into another array.

Good:

> Groups episodes by canonical season while preserving their original order.
