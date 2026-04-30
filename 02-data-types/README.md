# Data Types

Everything you need to understand Python's built-in data types — from the basics to memory internals and mutability.

---

## Contents

| File | Type | What it covers |
|------|------|----------------|
| `DataTypes.md` | Notes | Categories of types, mutable vs immutable, sequences, mappings, sets, detailed comparison table with sizes |
| `AdvancedDataTypes.md` | Notes | Deep dive into `tuple`, `list`, `dict`, `set` — 10 examples each, comparison table with lookup speeds and thread-safety notes |
| `mutable_immutable_guide.md` | Notes | Memory model, variables as references, identity (`id()`), Python vs Java comparison |
| `BuiltInFunctionsAndImmutability.md` | Notes | Built-in functions (`input`, `type`, `id`, `len`, `range` …), object identity, why immutability matters |
| `list-example.py` | Script | All list methods with examples: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`, `copy`, `clear`, `count`, `index`, `extend` |
| `tuple-example.py` | Script | Tuple methods and patterns: `count`, `index`, unpacking, extended unpacking, `zip`, `enumerate`, tuples as dict keys |
| `set-examples.py` | Script | Set operations: `add`, `remove`, `discard`, `pop`, `union`, `intersection`, `difference`, `issubset`, `issuperset`, comprehensions |
| `dist-examples.py` | Script | Dictionary methods: `get`, `keys`, `values`, `items`, `update`, `pop`, `popitem`, `setdefault`, `fromkeys`, merge with `\|` |
| `string-examples.py` | Script | String methods: case, search, split/join, strip, replace, padding, character tests, `encode`, `format`, `format_map` |
| `PythonVariablesAndDataTypes.pptx` | Slides | Presentation covering variables and data types |

---

## Key Concepts

### Two categories every type falls into

| | Immutable | Mutable |
|---|-----------|---------|
| **What it means** | Cannot change after creation | Can change in place |
| **Examples** | `int`, `float`, `str`, `tuple`, `frozenset`, `bool` | `list`, `dict`, `set`, `bytearray` |
| **Hashable?** | ✅ Yes — can be dict keys | ❌ No — cannot be dict keys |
| **Thread safe?** | ✅ Safer to share across threads | ⚠️ Needs care with concurrent writes |

### Lookup speed by type

| Type | Fast operation | Complexity |
|------|---------------|------------|
| `list` / `tuple` | Index access `lst[i]` | O(1) |
| `list` / `tuple` | Value search `x in lst` | O(n) — scans every element |
| `dict` | Key lookup `d[key]` | O(1) avg |
| `set` | Membership `x in s` | O(1) avg |

---

## Running the example scripts

```bash
python list-example.py
python tuple-example.py
python set-examples.py
python dist-examples.py
python string-examples.py
```

Each script is self-contained — run it, read the output, try changing values.

---

## Learning order

1. `DataTypes.md` — what types exist and how they are categorised
2. `mutable_immutable_guide.md` — why the mutable/immutable distinction matters
3. `BuiltInFunctionsAndImmutability.md` — built-in tools for working with any type
4. `AdvancedDataTypes.md` — `tuple`, `list`, `dict`, `set` in depth with examples
5. Run the `*-example.py` scripts — hands-on practice with every method
6. Slides — `PythonVariablesAndDataTypes.pptx`
