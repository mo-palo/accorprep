---
name: edit-html
description: "Editing discipline for large single-file HTML projects (index.html). Use before making any code changes to src/index.html — read-before-edit, verify multi-replace results, full field propagation checklist, no patch-on-patch. Invoke when: editing index.html, adding a new JS data field, fixing a ReferenceError, or doing a multi-step replacement."
argument-hint: "Describe the change you are about to make"
---

# Edit HTML — Discipline Checklist

## On invocation — announce it

**Always say this before starting work:**

> "Applying edit-html skill."

This lets the user know the discipline rules are active.

---

## Holistic fix rule — never fix in isolation

Before writing any fix, **grep for every occurrence** of the thing being changed (a value, a style, a class name, a field name, a label). Fix all occurrences in a single operation. Never fix one site and leave duplicates untouched.

**Anti-pattern to avoid:**

> Fix the form label color → user reports display card still has the old color → fix that too → user frustrated.

**Correct pattern:**

> Search `grep_search` for the value (`#ca8a04`, `"Question"`, etc.) across the whole file → list all occurrences → fix all in one `multi_replace_string_in_file`.

---

## Before every edit

1. **Read the exact lines** you plan to change with `read_file`. Never use conversation history as `oldString` — the file may have changed since that message.
2. **Identify all affected sites** — for JS changes, search for every function/variable that touches the code you're changing.

## After multi_replace_string_in_file

- Check the summary for failed replacements immediately.
- For each failure, `read_file` that area before writing the fix.
- Never assume the rest succeeded and proceed.

## Full-function replacement rule

For any function > ~10 lines needing multiple internal changes, replace the **entire function** in one operation. Do not stack small replacements inside the same function — context mismatches accumulate and produce broken intermediates.

## No patch-on-patch

If code is broken, re-read current state first. Never write a repair that assumes a previous repair applied correctly without verifying.

## Data model field propagation checklist

When adding a new field to a JS data object, verify **all** of these before finishing:

- [ ] Spread default: `raw.map(it => ({ ..., newField: defaultValue, ...it }))`
- [ ] `_readForm()` reads the DOM element into a local variable
- [ ] `_readForm()` return object includes the field
- [ ] **Every** `const { ..., newField } = _readForm(...)` destructuring updated (search all call sites)
- [ ] `items.push({ ..., newField })` includes the field
- [ ] `item.newField = newField` in the save/edit function
- [ ] Initial empty object passed to form builder (e.g. in `showAddForm`) includes the field
- [ ] Display render function reads `item.newField`
