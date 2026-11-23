# Naming

Use the shortest name that stays accurate at the call site. A long name can reveal a misplaced responsibility, but a word count cannot decide that. Keep domain terms, framework names, and public contracts where the surrounding code needs them.

❌ **Don't** abbreviate until the meaning disappears. A name like `valid` hides what was checked, and `handlerManager` gives no useful responsibility.

✅ **Do** put context in the owner when the owner is visible. `connection.close()` is clear. `hasValidProviderCredentials` is appropriate when several kinds of validity appear in the same function. Use verbs for operations and predicates for questions. Use a free predicate when there is no meaningful instance to ask.

Avoid suffixes that only repeat implementation details. Keep a qualifier when it distinguishes behavior callers need. Name a quantity when the name conveys units or policy. Keep incidental values near their use.
