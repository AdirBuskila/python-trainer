// Runs student code in Pyodide, off the main thread so infinite loops can be killed.
const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
importScripts(PYODIDE_URL + "pyodide.js");

let py = null;

async function init() {
  py = await loadPyodide({ indexURL: PYODIDE_URL });
  const src = await (await fetch("harness.py?v=" + self.HARNESS_V)).text();
  py.FS.writeFile("/home/pyodide/harness.py", src);
  py.runPython("import sys; sys.path.insert(0, '/home/pyodide'); import harness, json");
  postMessage({ type: "ready" });
}

self.HARNESS_V = new URL(self.location.href).searchParams.get("v") || "1";
const ready = init().catch((e) => postMessage({ type: "fatal", error: String(e) }));

self.onmessage = async (ev) => {
  await ready;
  const { id, kind, code, stdin, tests } = ev.data;
  try {
    py.globals.set("_code", code);
    let result;
    if (kind === "run") {
      py.globals.set("_stdin", stdin || "");
      result = JSON.parse(py.runPython("json.dumps(harness.run_code(_code, _stdin))"));
      result = { output: result[0], error: result[1] };
    } else {
      py.globals.set("_tests", JSON.stringify(tests));
      result = JSON.parse(py.runPython("json.dumps(harness.run_tests(_code, json.loads(_tests)))"));
    }
    postMessage({ type: "result", id, result });
  } catch (e) {
    postMessage({ type: "result", id, error: String(e) });
  }
};
