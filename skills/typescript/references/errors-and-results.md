# Errors and results

Failures should be modeled according to how callers are expected to handle
them.

## Throw errors for exceptional failure

Use typed domain errors when an operation cannot fulfill its contract.

```ts
throw new MetadataRequestError("Failed to fetch metadata", {
  cause: error
});
```

Do not collapse meaningful errors into generic `Error` values when callers
need the distinction.

## Preserve causes

When translating an underlying error into a domain error, preserve the
original cause.

```ts
try {
  return await requestMetadata();
} catch (error) {
  throw new MetadataRequestError("Failed to fetch metadata", {
    cause: error
  });
}
```

The catch value is genuinely unknown until inspected.

That is an appropriate use of `unknown`.

Do not cast it merely to make TypeScript quiet.

## Results

Use discriminated result types where failure is an expected outcome rather
than an exceptional execution failure.

Example:

```ts
export type ImportResult =
  | {
      ok: true;
      imported: number;
    }
  | {
      ok: false;
      reason:
        | "unsupported-format"
        | "invalid-data";
    };
```

This is appropriate when callers are expected to branch on the result.

Do not return enormous result unions for failures that should simply throw
a domain error.

## Avoid stringly typed errors

Avoid:

```ts
throw new Error("NOT_FOUND");
```

Prefer:

```ts
throw new AnimeNotFoundError(id);
```

or a meaningful discriminated result when failure is expected.

## Do not swallow invalid state with fallbacks

Avoid:

```ts
const message = error.message ?? "Something went wrong";
```

when the error representation should already guarantee a message.

Establish invariants earlier rather than compensating throughout the
codebase.

Apply defaults once, where they belong: a schema, configuration parsing, or domain construction.

```ts
const limit = options.limit ?? 20;
```

belongs in config parsing, not in business logic that reads `options.limit`.
