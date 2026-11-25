"""Validate exercise data: schema + every reference solution passes its tests.

Usage:  python tools/validate.py            (all chapters)
        python tools/validate.py ch05        (files whose name starts with ch05)
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import harness  # noqa: E402

KINDS = {"program", "function", "manual"}
REQ_EX = ["id", "num", "title", "kind", "difficulty", "prompt", "starter", "hints", "solution", "explain", "tests"]
REQ_CH = ["id", "title", "icon", "summary", "learn", "pitfalls", "exercises"]


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTER


def chapter_files(prefix=""):
    return sorted(p for p in (ROOT / "data").glob("ch*.py") if p.name.startswith(prefix))


def check_chapter(path, seen_ids):
    errors = []
    ch = load(path)
    for k in REQ_CH:
        if k not in ch:
            errors.append(f"chapter missing '{k}'")
    for item in ch.get("learn", []):
        if not {"title", "text"} <= item.keys():
            errors.append(f"learn item needs title+text: {item.get('title')}")
    for ex in ch.get("exercises", []):
        eid = ex.get("id", "?")
        pre = f"[{eid}]"
        for k in REQ_EX:
            if k not in ex:
                errors.append(f"{pre} missing '{k}'")
        if eid in seen_ids:
            errors.append(f"{pre} duplicate id")
        seen_ids.add(eid)
        if ex.get("kind") not in KINDS:
            errors.append(f"{pre} bad kind {ex.get('kind')}")
            continue
        if ex.get("difficulty") not in (1, 2, 3):
            errors.append(f"{pre} difficulty must be 1-3")
        tests = ex.get("tests", [])
        if ex["kind"] == "manual":
            if "sample_stdin" not in ex:
                errors.append(f"{pre} manual exercise should give sample_stdin")
            continue
        if len(tests) < 3:
            errors.append(f"{pre} needs >= 3 tests (has {len(tests)})")
        if not any(not t.get("hidden") for t in tests):
            errors.append(f"{pre} needs at least one visible (non-hidden) test as an example")
        for i, t in enumerate(tests):
            if ex["kind"] == "program" and ("call" in t or "out" not in t):
                errors.append(f"{pre} test {i}: program tests need 'out' and no 'call'")
            if ex["kind"] == "function" and "call" not in t:
                errors.append(f"{pre} test {i}: function tests need 'call'")
            if "call" in t and "expect" not in t and "out" not in t:
                errors.append(f"{pre} test {i}: call needs 'expect' and/or 'out'")
        results = harness.run_tests(ex.get("solution", ""), tests)
        for i, r in enumerate(results):
            if not r["passed"]:
                errors.append(f"{pre} SOLUTION FAILS test {i}: error={r['error']!r} got={r['got']!r} expected={r['expected']!r}")
        starter_results = harness.run_tests(ex.get("starter", ""), tests)
        if all(r["passed"] for r in starter_results):
            errors.append(f"{pre} the starter code already passes every test - tests are too weak")
    return ch, errors


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    seen, total, bad = set(), 0, 0
    for path in chapter_files(prefix):
        try:
            ch, errors = check_chapter(path, seen)
        except Exception as e:  # noqa: BLE001
            print(f"{path.name}: FAILED TO LOAD: {e!r}")
            bad += 1
            continue
        n = len(ch.get("exercises", []))
        total += n
        status = "OK" if not errors else f"{len(errors)} problem(s)"
        print(f"{path.name}: {n} exercises - {status}")
        for e in errors:
            print("   ", e)
        bad += len(errors)
    print(f"\nTotal exercises: {total}. Problems: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
