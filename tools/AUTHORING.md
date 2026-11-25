# Writing exercises for the Python trainer

The trainer is a Hebrew (RTL) web app. The student writes **real Python 3** in the browser; it runs in
Pyodide and is graded against the tests you write. Source data lives in `data/chNN_<topic>.py`, one file per
chapter, each defining a single dict named `CHAPTER`. `tools/build.py` bundles them into `course.js`.

The source material is a Hebrew exercise workbook (a PDF in this folder) written for a generic / C-style
language. Adapt every exercise to idiomatic beginner Python:
- arrays -> lists, matrices -> lists of lists, `switch` -> `if/elif` (or `match`), `Random` -> `import random`
- C++/C# only ideas (pointers, `new`, destructors, char*, fixed string sizes, getters for everything) ->
  drop them or turn them into the Python equivalent (`__init__` with default arguments, `__str__`, methods)
- "read N numbers" -> the student calls `input()` once per number, **one value per input line**
- **Rewrite the exercise text in your own words** (Hebrew). Do not copy the workbook sentences verbatim
  and never mention the workbook's author. Keep the idea, numbers and examples.

## Validate before you finish

```
python tools/validate.py ch05        # only files starting with ch05
```
It checks the schema, runs your `solution` against every test (must all pass), and checks that the
`starter` does NOT pass all tests. Fix until it prints `Problems: 0` for your files.
The harness is `harness.py` (read its docstring) — the browser uses the same file.

## Chapter dict

```python
CHAPTER = {
    "id": "loops",                       # short slug, unique
    "title": "לולאות",                    # Hebrew chapter title
    "icon": "🔁",                         # one emoji
    "summary": "while, for, range, סכומים ומונים",   # one line
    "learn": [                            # 4-8 short concept cards: the Python they need for this chapter
        {"title": "לולאת for עם range",
         "text": "`range(a, b)` נותן את המספרים מ-a עד b-1. ...",   # Hebrew, may use the markup below
         "code": "for i in range(1, 6):\n    print(i)"},            # optional runnable example
    ],
    "pitfalls": [                         # 3-6 common beginner mistakes (Hebrew, markup allowed)
        "`input()` תמיד מחזיר מחרוזת — צריך `int(input())` כדי לחשב.",
    ],
    "exercises": [ ... ],
}
```

## Exercise dict

```python
{
    "id": "loops-07",            # "<chapter id>-<two digit workbook number>"; for sub-parts "loops-15a"
    "num": "7",                  # the number as printed in the workbook ("15א" etc.) so the student can find it
    "title": "סכום ספרות",        # 2-4 Hebrew words
    "kind": "program",           # "program" | "function" | "manual"
    "difficulty": 2,             # 1 easy, 2 medium, 3 hard
    "exam": False,               # True if the workbook marks it "שאלה מבחינה" / "תרגיל מבחינה"
    "prompt": "...",             # Hebrew task, rewritten, with an exact I/O spec (see below)
    "starter": "...",            # code the editor starts with (must NOT already pass the tests)
    "hints": ["...", "...", "..."],   # 2-3 progressive Hebrew hints: idea -> structure -> almost-code
    "solution": "...",           # clean reference solution, beginner style, short comments in Hebrew ok
    "explain": "...",            # 2-5 Hebrew sentences: why the solution works / key idea to remember
    "tests": [ ... ],            # >= 3 for program/function; >= 1 visible (non-hidden)
}
```

### Kinds
- **program**: a full script that reads with `input()` and prints. Tests: `{"stdin": "...", "out": "..."}`.
- **function**: the student writes a function (or class) with an exact name. Tests use `call`/`expect`
  (see harness docstring). When the workbook asks for a function + a main program, grade the function with
  `call` tests and tell the student in the prompt that the main program is optional/for trying it out.
  Main programs inside `if __name__ == "__main__":` do not run during function tests. If the main program is
  the interesting part, make it a program exercise instead, or split into two exercises (`-15a`, `-15b`).
- **manual**: cannot be auto-graded (randomness, open-ended). No tests; give `"sample_stdin": "..."` so the Run
  button has input. Use sparingly.

### The prompt must state the exact I/O
Output comparison is lenient: it compares whitespace/comma separated tokens, numbers with tolerance
(`5` == `5.0`), words case-insensitively, and ignores `[ ] ( ) ' "` and `:`. Text passed to `input("...")` is
NOT captured, so prompts are fine. Still, say exactly what to print. Put the spec at the end of the prompt:

```
**קלט:** מספר שלם בכל שורה — קודם N ואז ...
**פלט:** הדפס רק את הסכום.
```
Prefer **English** words for printed messages (`YES`, `NO`, `even`, `odd`, `Not found`), and say them
explicitly in backticks, e.g. "הדפס `even` אם המספר זוגי, אחרת `odd`." Avoid long free text in output.
Don't require prints of labels like "The sum is:" — just the value(s), unless the task is about formatting.
For a list, print the values on one line separated by spaces (`print(*lst)`), and say so.

### Markup allowed in prompt / hints / explain / learn / pitfalls
- `inline code` in backticks, **bold**, blank line = new paragraph, lines starting with `- ` = bullets
- fenced code blocks with ``` (no language tag needed)
Python strings: use normal or triple-quoted strings; real newlines with "\n" or triple quotes.

### Tests
- Cover normal cases + edge cases (0, negatives, equal values, single element, last/first position, not found).
- Mark extra ones `"hidden": True`; the first 1-2 visible tests are shown as examples in the UI.
- Function returning a float: `expect` a literal like `"2.5"` (tolerance applies). Lists: `"[1, 2, 3]"`.
  Booleans: `"True"` (a student returning 1/0 also passes).
- Mutating functions: `{"setup": "a = [1, 2, 3]", "call": "rotate_right(a)", "check": "a", "expect": "[3, 1, 2]"}`
- Printing functions: `{"call": "triangle('abc')", "out": "abc\nbc\nc"}`
- Classes: `{"setup": "h = Hotel('Hilton', 'Eilat', 100, 14)", "call": "h.get_free()", "expect": "14"}`
- The starter must fail: e.g. `def digit_sum(n):\n    # כתוב כאן את הקוד\n    pass\n` or for programs a
  comment plus reading the input: `n = int(input())\n# כתוב כאן את הקוד\n`.

### Example (complete)

```python
{
    "id": "loops-15",
    "num": "15",
    "title": "שורש ספרתי",
    "kind": "function",
    "difficulty": 2,
    "exam": False,
    "prompt": "כתוב פונקציה `digital_root(n)` שמקבלת מספר שלם חיובי ומסכמת את ספרותיו שוב ושוב, עד שמתקבל מספר חד-ספרתי, ומחזירה אותו.\n\nלדוגמה: עבור `128` → 1+2+8=11 → 1+1=2, ולכן מוחזר `2`.\n\n**החזר:** את המספר החד-ספרתי (אל תדפיס).",
    "starter": "def digital_root(n):\n    # כתוב כאן את הקוד\n    pass\n",
    "hints": [
        "צריך שתי לולאות: חיצונית — כל עוד המספר גדול מ-9, ופנימית — שמסכמת ספרות.",
        "ספרת האחדות היא `n % 10`, ו-`n // 10` מוריד אותה.",
        "while n > 9:\n    s = 0\n    while n > 0:\n        s += n % 10\n        n //= 10\n    n = s",
    ],
    "solution": "def digital_root(n):\n    while n > 9:\n        s = 0\n        while n > 0:\n            s += n % 10\n            n //= 10\n        n = s\n    return n\n",
    "explain": "הלולאה הפנימית מפרקת מספר לספרות עם `% 10` ו-`// 10`. הלולאה החיצונית חוזרת על התהליך כל עוד יש יותר מספרה אחת.",
    "tests": [
        {"call": "digital_root(128)", "expect": "2"},
        {"call": "digital_root(7)", "expect": "7"},
        {"call": "digital_root(99999)", "expect": "9", "hidden": True},
        {"call": "digital_root(10)", "expect": "1", "hidden": True},
    ],
}
```
