"""Test harness shared by the browser (Pyodide) and the local validator.

A test case is a dict. Two shapes:

  Program case (the whole script is run):
    {"stdin": "3\n5\n", "out": "8"}
      stdin  - text fed to input(), one line per call
      out    - expected printed output (compared leniently, see _tokens)

  Function case (the script is run once to define things, then an expression is evaluated):
    {"call": "digit_sum(123)", "expect": "6"}
    {"setup": "a = [1, 2, 3]", "call": "rotate(a)", "check": "a", "expect": "[3, 1, 2]"}
    {"call": "triangle('abc')", "out": "abc\nbc\nc"}
      setup  - optional code run before the call (same namespace)
      call   - expression to evaluate
      check  - optional expression whose value is compared instead of the call's result
      expect - Python literal the value must equal (floats compared with tolerance)
      out    - optional expected output printed during the call
      stdin  - optional input for the script (rarely needed)

Prompts passed to input("...") are NOT part of the captured output, so students may use them freely.
"""

import ast
import io
import math
import re
import sys
import traceback


class _NoMoreInput(BaseException):  # BaseException: a student try/except Exception must not swallow it
    pass


def _tokens(text):
    text = re.sub(r"[\[\]()'\"]", " ", str(text))
    return [t for t in re.split(r"[\s,:]+", text.strip()) if t]


def _num(tok):
    try:
        return float(tok)
    except ValueError:
        return None


def _tok_equal(a, b):
    na, nb = _num(a), _num(b)
    if na is not None and nb is not None:
        return math.isclose(na, nb, rel_tol=1e-6, abs_tol=1e-6)
    return a.lower() == b.lower()


def outputs_match(got, expected):
    ga, ea = _tokens(got), _tokens(expected)
    return len(ga) == len(ea) and all(_tok_equal(x, y) for x, y in zip(ga, ea))


def values_equal(got, expected):
    if isinstance(expected, bool):
        return (got is True or got is False or got in (0, 1)) and bool(got) == expected
    if isinstance(got, bool) and isinstance(expected, int):
        return int(got) == expected
    if isinstance(expected, (int, float)) and isinstance(got, (int, float)):
        return math.isclose(got, expected, rel_tol=1e-6, abs_tol=1e-6)
    if isinstance(expected, (list, tuple)) and isinstance(got, (list, tuple)):
        return len(got) == len(expected) and all(values_equal(g, e) for g, e in zip(got, expected))
    if isinstance(expected, dict) and isinstance(got, dict):
        return got.keys() == expected.keys() and all(values_equal(got[k], expected[k]) for k in expected)
    if isinstance(expected, str) and isinstance(got, str):
        return got.strip() == expected.strip()
    return got == expected


def _make_input(stdin, echo=False):
    lines = iter((stdin or "").splitlines())

    def fake_input(prompt=""):
        try:
            value = next(lines)
        except StopIteration:
            raise _NoMoreInput()
        if echo:  # look like a terminal: show the prompt and the typed value
            print(f"{prompt}{value}")
        return value

    return fake_input


def _short_tb(code_name):
    etype, evalue, tb = sys.exc_info()
    frames = [f for f in traceback.extract_tb(tb) if f.filename == code_name]
    where = f" (שורה {frames[-1].lineno})" if frames else ""
    return f"{etype.__name__}: {evalue}{where}"


def run_code(code, stdin=""):
    """Run a script freely (the 'Run' button). Returns (output, error_or_None)."""
    buf = io.StringIO()
    ns = {"__name__": "__main__", "input": _make_input(stdin, echo=True)}
    old = sys.stdout
    sys.stdout = buf
    err = None
    try:
        exec(compile(code, "<student>", "exec"), ns)
    except _NoMoreInput:
        err = "הקוד ביקש עוד קלט (input) אבל לא נשאר קלט בתיבה. הוסף שורות קלט."
    except SystemExit:
        pass
    except Exception:
        err = _short_tb("<student>")
    finally:
        sys.stdout = old
    return buf.getvalue(), err


def run_case(code, case):
    """Returns dict: passed, got, expected, error, kind."""
    stdin = case.get("stdin", "")
    buf = io.StringIO()
    is_call = "call" in case
    # In function cases a main program guarded by `if __name__ == "__main__":` does not run.
    ns = {"__name__": "__trainer__" if is_call else "__main__", "input": _make_input(stdin)}
    old = sys.stdout
    res = {"passed": False, "got": "", "expected": "", "error": None}
    try:
        sys.stdout = buf
        try:
            exec(compile(code, "<student>", "exec"), ns)
        except SystemExit:
            pass
        if not is_call:
            res["got"] = buf.getvalue()
            res["expected"] = case.get("out", "")
            res["passed"] = outputs_match(res["got"], res["expected"])
            return res
        if "setup" in case:
            exec(case["setup"], ns)
        buf.seek(0)
        buf.truncate()
        value = eval(case["call"], ns)
        if "check" in case:
            value = eval(case["check"], ns)
        printed = buf.getvalue()
        ok = True
        got_parts, exp_parts = [], []
        if "expect" in case:
            expected = ast.literal_eval(case["expect"])
            ok = ok and values_equal(value, expected)
            got_parts.append(repr(value))
            exp_parts.append(case["expect"])
        if "out" in case:
            ok = ok and outputs_match(printed, case["out"])
            got_parts.append(printed.rstrip())
            exp_parts.append(case["out"])
        res["passed"] = ok
        res["got"] = "\n".join(got_parts)
        res["expected"] = "\n".join(exp_parts)
    except _NoMoreInput:
        if is_call:
            res["error"] = ("הקוד קרא ל-input() אבל בבדיקה הזו אין קלט. "
                            "בתרגיל פונקציה כתוב רק את הפונקציה (או שים את התוכנית הראשית תחת if __name__ == '__main__':)")
        else:
            res["error"] = "הקוד ביקש יותר קלט ממה שיש בבדיקה. בדוק כמה פעמים אתה קורא ל-input()."
        res["got"] = buf.getvalue()
    except NameError as e:
        res["error"] = f"NameError: {e} — ודא שהשם של הפונקציה/המחלקה זהה בדיוק למה שנדרש"
    except Exception:
        res["error"] = _short_tb("<student>")
        res["got"] = buf.getvalue()
    finally:
        sys.stdout = old
    return res


def run_tests(code, cases):
    return [run_case(code, c) for c in cases]
