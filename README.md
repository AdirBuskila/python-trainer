# Python trainer

A Hebrew web app for practicing the course workbook in Python. Students write real Python in the
browser (Pyodide, in a Web Worker) and get instant automatic grading.

- `index.html`, `app.js`, `style.css`, `worker.js` - the app (static, no build step needed to serve)
- `harness.py` - the grader; the browser and the local validator use the same file
- `data/chNN_*.py` - exercises, one chapter per file (see `tools/AUTHORING.md`)
- `course.js` - generated bundle of all chapters

After changing exercises:

```
python tools/validate.py   # every reference solution must pass its tests
python tools/build.py      # regenerate course.js
```

Local preview: `python -m http.server 8791 --directory python-2`
