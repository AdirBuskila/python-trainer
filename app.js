/* Python trainer — single-page app. Data comes from course.js (window.COURSE). */
(() => {
  "use strict";

  const COURSE = window.COURSE || { chapters: [] };
  const CHAPTERS = COURSE.chapters;
  const ALL = [];
  CHAPTERS.forEach((ch, ci) => ch.exercises.forEach((ex, i) => {
    ex.chapter = ch; ex.index = i; ex.chapterIndex = ci; ALL.push(ex);
  }));
  const BY_ID = Object.fromEntries(ALL.map((e) => [e.id, e]));
  const $app = document.getElementById("app");

  /* ------------------------------------------------------------------ storage */
  const KEY = "pytrainer-v1";
  const store = Object.assign(
    { status: {}, code: {}, saw: {}, hints: {}, last: null, days: [], exam: null, history: [] },
    safeParse(localStorage.getItem(KEY))
  );
  function safeParse(s) { try { return JSON.parse(s) || {}; } catch { return {}; } }
  let saveTimer = null;
  function save(now) {
    clearTimeout(saveTimer);
    const write = () => { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) { console.warn(e); } };
    if (now) write(); else saveTimer = setTimeout(write, 300);
  }
  function markActiveToday() {
    const d = new Date().toISOString().slice(0, 10);
    if (!store.days.includes(d)) { store.days.push(d); store.days = store.days.slice(-120); save(); }
  }
  function streak() {
    const set = new Set(store.days);
    let n = 0;
    const d = new Date();
    if (!set.has(d.toISOString().slice(0, 10))) d.setDate(d.getDate() - 1);
    while (set.has(d.toISOString().slice(0, 10))) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  const isSolved = (id) => store.status[id] === "solved";

  /* ------------------------------------------------------------------ python worker */
  const Py = {
    worker: null, ready: false, readyWaiters: [], pending: new Map(), seq: 0,
    start() {
      this.ready = false;
      setStatus("טוען את פייתון… (בפעם הראשונה זה לוקח כמה שניות)");
      this.worker = new Worker("worker.js?v=2");
      this.worker.onmessage = (ev) => {
        const m = ev.data;
        if (m.type === "ready") {
          this.ready = true; setStatus("פייתון מוכן ✓", "ready");
          this.readyWaiters.splice(0).forEach((f) => f());
        } else if (m.type === "fatal") {
          setStatus("שגיאה בטעינת פייתון — בדוק חיבור לאינטרנט ורענן", "error");
        } else if (m.type === "result") {
          const p = this.pending.get(m.id);
          if (p) { this.pending.delete(m.id); clearTimeout(p.timer); m.error ? p.reject(new Error(m.error)) : p.resolve(m.result); }
        }
      };
      this.worker.onerror = () => setStatus("שגיאה בטעינת פייתון — רענן את הדף", "error");
    },
    whenReady() { return this.ready ? Promise.resolve() : new Promise((r) => this.readyWaiters.push(r)); },
    async call(kind, payload, timeoutMs = 5000) {
      await this.whenReady();
      const id = ++this.seq;
      return new Promise((resolve, reject) => {
        const timer = setTimeout(() => {
          this.pending.delete(id);
          this.worker.terminate();
          this.pending.forEach((p) => { clearTimeout(p.timer); p.reject(new Error("restart")); });
          this.pending.clear();
          this.start();
          reject(new Error("timeout"));
        }, timeoutMs);
        this.pending.set(id, { resolve, reject, timer });
        this.worker.postMessage({ id, kind, ...payload });
      });
    },
    run(code, stdin) { return this.call("run", { code, stdin }); },
    async testOne(code, test) { return (await this.call("test", { code, tests: [test] }, 4000))[0]; },
  };
  function setStatus(text, cls) {
    const el = document.getElementById("pyStatus");
    el.textContent = text; el.className = "pystatus" + (cls ? " " + cls : "");
  }
  const TIMEOUT_MSG = "הקוד רץ יותר מדי זמן ונעצר. כנראה יש לולאה אינסופית (בדוק שהמשתנה בתנאי של ה-while משתנה בכל סיבוב), או שהקוד מחכה לעוד קלט.";

  /* ------------------------------------------------------------------ helpers */
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const HEB = /[֐-׿]/;

  function md(src) {
    if (src == null || src === "") return "";
    src = String(src);
    const blocks = [];
    src = src.replace(/```[a-zA-Z]*\n?([\s\S]*?)```/g, (m, c) => { blocks.push(c.replace(/\n+$/, "")); return `\u0000${blocks.length - 1}\u0000`; });
    const inline = (s) => esc(s)
      // Inside Hebrew text, runs like "1+2+8 = 11 → 2" or "3, 4, 5" would display reversed: isolate them LTR.
      .replace(/-?\d[\d\s+\-*/=→.,×^%:]*\d/g, (m) => /[+\-*/=→,×^%]/.test(m.replace(/^-/, "")) ? `<span class="ltr">${m}</span>` : m)
      .replace(/`([^`]+)`/g, (m, c) => `<code class="inl">${c}</code>`)
      .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
    const block = (i) => `<pre>${esc(blocks[+i])}</pre>`;
    return src.split(/\n\s*\n/).map((para) => {
      const t = para.trim();
      const only = t.match(/^\u0000(\d+)\u0000$/);
      if (only) return block(only[1]);
      const lines = t.split("\n");
      if (lines.every((l) => /^\s*[-•]\s+/.test(l))) {
        return "<ul>" + lines.map((l) => `<li>${restore(inline(l.replace(/^\s*[-•]\s+/, "")))}</li>`).join("") + "</ul>";
      }
      return "<p>" + restore(lines.map(inline).join("<br>")) + "</p>";
    }).join("");
    function restore(html) { return html.replace(/\u0000(\d+)\u0000/g, (m, i) => block(i)); }
  }
  // Hints are sometimes raw code: no Hebrew + looks like code -> show as a code block.
  function smartMd(text) {
    if (text && !HEB.test(text) && !text.includes("`")) return `<pre>${esc(text)}</pre>`;
    return md(text);
  }
  function diffStars(d) { return `<span class="diff" title="רמת קושי">${"★".repeat(d)}<span class="off">${"★".repeat(3 - d)}</span></span>`; }
  function statusIcon(id) {
    const s = store.status[id];
    if (s === "solved") return store.saw[id] ? "✅" : "🏆";
    if (s === "tried") return "🟡";
    return "⚪";
  }
  function toast(msg) {
    const t = document.getElementById("toast");
    t.textContent = msg; t.classList.add("show");
    clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove("show"), 2200);
  }
  function chapterProgress(ch) {
    const n = ch.exercises.length, s = ch.exercises.filter((e) => isSolved(e.id)).length;
    return { n, s, pct: n ? Math.round((s / n) * 100) : 0 };
  }
  function updateTop() {
    const s = ALL.filter((e) => isSolved(e.id)).length;
    document.getElementById("topCount").textContent = `${s}/${ALL.length}`;
    document.getElementById("topFill").style.width = (ALL.length ? (s / ALL.length) * 100 : 0) + "%";
  }
  function nextUnsolved(after) {
    const start = after ? ALL.indexOf(after) + 1 : 0;
    return ALL.slice(start).find((e) => !isSolved(e.id)) || ALL.find((e) => !isSolved(e.id));
  }
  function makeEditor(host, value, onChange, extraKeys = {}) {
    const cm = CodeMirror(host, {
      value, mode: "python", lineNumbers: true, indentUnit: 4, tabSize: 4, matchBrackets: true,
      autoCloseBrackets: true, direction: "ltr", viewportMargin: Infinity,
      extraKeys: Object.assign({
        Tab: (c) => c.somethingSelected() ? c.indentSelection("add") : c.replaceSelection("    ", "end"),
        "Shift-Tab": (c) => c.indentSelection("subtract"),
        "Ctrl-/": (c) => toggleComment(c), "Cmd-/": (c) => toggleComment(c),
      }, extraKeys),
    });
    if (onChange) cm.on("change", () => onChange(cm.getValue()));
    setTimeout(() => cm.refresh(), 0);
    return cm;
  }
  function toggleComment(cm) {
    const from = cm.getCursor("from").line, to = cm.getCursor("to").line;
    const lines = [];
    for (let i = from; i <= to; i++) lines.push(cm.getLine(i));
    const allC = lines.every((l) => /^\s*#/.test(l) || !l.trim());
    cm.operation(() => lines.forEach((l, k) => {
      const ln = from + k;
      if (!l.trim()) return;
      const nl = allC ? l.replace(/^(\s*)# ?/, "$1") : l.replace(/^(\s*)/, "$1# ");
      cm.replaceRange(nl, { line: ln, ch: 0 }, { line: ln, ch: l.length });
    }));
  }

  /* ------------------------------------------------------------------ router */
  function route() {
    const h = location.hash.replace(/^#\/?/, "");
    const [view, arg, arg2] = h.split("/");
    document.querySelectorAll(".topnav a").forEach((a) => a.classList.toggle("active", a.dataset.nav === (view || "home")));
    window.scrollTo(0, 0);
    updateTop();
    if (view === "ch" && arg) return renderChapter(decodeURIComponent(arg), arg2);
    if (view === "ex" && BY_ID[decodeURIComponent(arg)]) return renderExercise(BY_ID[decodeURIComponent(arg)]);
    if (view === "exam") return renderExam();
    if (view === "play") return renderPlay();
    return renderHome();
  }
  window.addEventListener("hashchange", route);

  /* ------------------------------------------------------------------ home */
  function renderHome() {
    document.title = "מאמן פייתון";
    const solved = ALL.filter((e) => isSolved(e.id)).length;
    const exams = ALL.filter((e) => e.exam);
    const examSolved = exams.filter((e) => isSolved(e.id)).length;
    const last = store.last && BY_ID[store.last];
    const cont = last && !isSolved(last.id) ? last : nextUnsolved(last);
    const st = streak();
    $app.innerHTML = `
      <section class="hero">
        <div class="card hero-main">
          <h1>היי שחר 👋 בוא נצליח במבחן</h1>
          <p>${ALL.length} תרגילים מחוברת התרגילים, מותאמים לפייתון. כותבים קוד אמיתי כאן בדפדפן, ומקבלים בדיקה אוטומטית מיד.</p>
          <div class="hero-actions">
            ${cont ? `<a class="btn" href="#/ex/${cont.id}">${solved ? "המשך מאיפה שעצרת" : "בוא נתחיל"} ← ${esc(cont.title)}</a>` : `<span>סיימת הכל! 🎉</span>`}
            <a class="btn ghost" href="#/exam">📝 מבחן תרגול</a>
            <button class="btn ghost" id="randomBtn">🎲 תרגיל אקראי</button>
          </div>
        </div>
        <div class="stats">
          <div class="card stat"><div class="num">${solved}<span class="muted" style="font-size:16px">/${ALL.length}</span></div><div class="lbl">תרגילים שנפתרו</div></div>
          <div class="card stat"><div class="num">${examSolved}<span class="muted" style="font-size:16px">/${exams.length}</span></div><div class="lbl">שאלות ממבחנים</div></div>
          <div class="card stat"><div class="num">${st} 🔥</div><div class="lbl">ימי תרגול ברצף</div></div>
          <div class="card stat"><div class="num">${CHAPTERS.filter((c) => chapterProgress(c).pct === 100).length}<span class="muted" style="font-size:16px">/${CHAPTERS.length}</span></div><div class="lbl">פרקים שהושלמו</div></div>
        </div>
      </section>
      <h2>הפרקים</h2>
      <div class="chapters">
        ${CHAPTERS.map((ch, i) => {
          const p = chapterProgress(ch);
          const ex = ch.exercises.filter((e) => e.exam).length;
          return `<a class="card chapter-card" href="#/ch/${ch.id}">
            <div class="top"><div class="icon">${ch.icon}</div><div><div class="n">פרק ${i + 1}</div><h3>${esc(ch.title)}</h3></div></div>
            <div class="sum">${esc(ch.summary)}</div>
            <div class="foot"><div class="bar"><div class="fill" style="width:${p.pct}%"></div></div><span>${p.s}/${p.n}</span>${ex ? `<span class="pill exam">${ex} ממבחנים</span>` : ""}</div>
          </a>`;
        }).join("")}
      </div>
      <div class="card tips">
        <h3>איך להשתמש במאמן</h3>
        <ul>
          <li>בכל פרק יש לשונית <b>לימוד</b> עם החומר שצריך לדעת וטעויות נפוצות — כדאי לקרוא לפני התרגילים.</li>
          <li>בתרגיל: <b>▶ הרץ</b> (Ctrl+Enter) מריץ את הקוד עם הקלט שבתיבה. <b>✓ בדוק</b> (Ctrl+Shift+Enter) מריץ את כל הבדיקות.</li>
          <li>תקוע? קח <b>רמז</b> אחד בכל פעם. את הפתרון כדאי לפתוח רק אחרי ניסיון אמיתי.</li>
          <li>🏆 = נפתר לבד · ✅ = נפתר אחרי הצצה בפתרון · 🟡 = ניסית ועוד לא עבר. ההתקדמות נשמרת בדפדפן הזה.</li>
          <li>לפני המבחן: עשה כמה <b>מבחני תרגול</b> עם שעון — בלי רמזים ובלי פתרונות.</li>
        </ul>
      </div>
      <div class="settings"><button id="resetAll">איפוס כל ההתקדמות</button></div>`;
    document.getElementById("randomBtn").onclick = () => {
      const pool = ALL.filter((e) => !isSolved(e.id) && e.kind !== "manual");
      const pick = (pool.length ? pool : ALL)[Math.floor(Math.random() * (pool.length || ALL.length))];
      location.hash = "#/ex/" + pick.id;
    };
    document.getElementById("resetAll").onclick = () => {
      if (confirm("למחוק את כל ההתקדמות והקוד ששמרת? אי אפשר לבטל.")) {
        localStorage.removeItem(KEY); location.reload();
      }
    };
  }

  /* ------------------------------------------------------------------ chapter */
  function renderChapter(id, tab) {
    const ch = CHAPTERS.find((c) => c.id === id);
    if (!ch) return renderHome();
    document.title = ch.title + " · מאמן פייתון";
    const idx = CHAPTERS.indexOf(ch);
    const p = chapterProgress(ch);
    tab = tab || (p.s > 0 ? "ex" : "learn");
    $app.innerHTML = `
      <div class="crumbs"><a href="#/">בית</a> / פרק ${idx + 1}</div>
      <div class="chapter-head">
        <div class="icon">${ch.icon}</div>
        <div style="flex:1"><h1>${esc(ch.title)}</h1><div class="muted">${esc(ch.summary)}</div></div>
        <div style="width:180px"><div class="bar"><div class="fill" style="width:${p.pct}%"></div></div><div class="muted" style="font-size:13px;margin-top:4px">${p.s} מתוך ${p.n} נפתרו</div></div>
      </div>
      <div class="tabs">
        <button data-tab="learn" class="${tab === "learn" ? "active" : ""}">📖 לימוד</button>
        <button data-tab="ex" class="${tab === "ex" ? "active" : ""}">💻 תרגילים (${p.n})</button>
      </div>
      <div id="tabBody"></div>`;
    $app.querySelectorAll(".tabs button").forEach((b) => b.onclick = () => { history.replaceState(null, "", `#/ch/${ch.id}/${b.dataset.tab}`); renderChapter(ch.id, b.dataset.tab); });
    const body = document.getElementById("tabBody");
    if (tab === "learn") {
      body.innerHTML = `
        <div class="learn-grid">
          ${ch.learn.map((l, i) => `<div class="card learn-card"><h3>${esc(l.title)}</h3>${md(l.text)}
            ${l.code ? `<div class="code-wrap"><pre>${esc(l.code)}</pre><button class="btn small try" data-i="${i}">▶ נסה</button></div>` : ""}</div>`).join("")}
        </div>
        ${ch.pitfalls && ch.pitfalls.length ? `<div class="card pitfalls"><h3>⚠️ טעויות נפוצות</h3><ul>${ch.pitfalls.map((x) => `<li>${md(x).replace(/^<p>|<\/p>$/g, "")}</li>`).join("")}</ul></div>` : ""}
        <div style="margin-top:20px;text-align:center"><a class="btn primary" href="#/ch/${ch.id}/ex">לתרגילים ←</a></div>`;
      body.querySelectorAll(".try").forEach((b) => b.onclick = () => { sessionStorage.setItem("play-code", ch.learn[+b.dataset.i].code); location.hash = "#/play"; });
    } else {
      let filter = sessionStorage.getItem("ex-filter") || "all";
      const draw = () => {
        const list = ch.exercises.filter((e) => filter === "all" || (filter === "todo" && !isSolved(e.id)) || (filter === "exam" && e.exam));
        body.innerHTML = `
          <div class="filters">
            ${[["all", "הכל"], ["todo", "עוד לא נפתרו"], ["exam", "רק ממבחנים"]].map(([k, t]) => `<button data-f="${k}" class="${filter === k ? "active" : ""}">${t}</button>`).join("")}
          </div>
          <div class="ex-list">
            ${list.map((e) => `<a class="card ex-row" href="#/ex/${e.id}">
              <span class="st">${statusIcon(e.id)}</span><span class="num">תרגיל ${esc(e.num)}</span>
              <span class="ttl">${esc(e.title)}</span>
              <span>${e.exam ? '<span class="pill exam">ממבחן</span>' : ""} ${e.kind === "function" ? '<span class="pill">פונקציה</span>' : ""}</span>
              ${diffStars(e.difficulty)}</a>`).join("") || '<p class="muted">אין תרגילים בסינון הזה.</p>'}
          </div>`;
        body.querySelectorAll(".filters button").forEach((b) => b.onclick = () => { filter = b.dataset.f; sessionStorage.setItem("ex-filter", filter); draw(); });
      };
      draw();
    }
  }

  /* ------------------------------------------------------------------ exercise */
  function examplesHtml(ex) {
    if (ex.kind === "manual") return "";
    const vis = ex.tests.filter((t) => !t.hidden).slice(0, 2);
    if (!vis.length) return "";
    return `<div class="examples"><h3>דוגמה${vis.length > 1 ? "ות" : ""}</h3>${vis.map((t) => {
      if ("call" in t) {
        const right = [t.expect != null ? `→ ${t.expect}` : "", t.out != null ? t.out : ""].filter(Boolean).join("\n");
        return `<div class="example"><div><div class="lbl">קריאה</div><pre>${esc((t.setup ? t.setup + "\n" : "") + t.call + (t.check ? "\n" + t.check : ""))}</pre></div>
                <div><div class="lbl">${t.expect != null ? "מחזיר" : "מדפיס"}</div><pre>${esc(right)}</pre></div></div>`;
      }
      return `<div class="example"><div><div class="lbl">קלט</div><pre>${esc(t.stdin || "(אין קלט)")}</pre></div><div><div class="lbl">פלט צפוי</div><pre>${esc(t.out)}</pre></div></div>`;
    }).join("")}</div>`;
  }

  function defaultStdin(ex) {
    if (ex.sample_stdin != null) return ex.sample_stdin;
    const t = ex.tests.find((x) => !x.hidden && x.stdin != null) || ex.tests.find((x) => x.stdin != null);
    return t ? t.stdin : "";
  }

  /**
   * Draw an exercise. opts.exam: { codeKey, onChange, hideHelp, header } for exam mode.
   */
  function renderExercise(ex, opts = {}) {
    const exam = !!opts.exam;
    if (!exam) { store.last = ex.id; save(); }
    document.title = ex.title + " · מאמן פייתון";
    const ch = ex.chapter;
    const codeKey = exam ? opts.codeKey : ex.id;
    const codeStore = exam ? opts.codeStore : store.code;
    const prev = ch.exercises[ex.index - 1], next = ch.exercises[ex.index + 1];
    const hintsShown = exam ? 0 : (store.hints[ex.id] || 0);

    $app.innerHTML = `
      ${opts.header || `<div class="crumbs"><a href="#/">בית</a> / <a href="#/ch/${ch.id}/ex">${esc(ch.title)}</a> / תרגיל ${esc(ex.num)}</div>`}
      <div class="ex-layout">
        <section class="card ex-panel">
          <div class="ex-title">
            <span style="font-size:22px">${exam ? "📝" : statusIcon(ex.id)}</span>
            <h1>${esc(ex.title)}</h1>
            ${ex.exam ? '<span class="pill exam">שאלה ממבחן</span>' : ""}
            ${diffStars(ex.difficulty)}
          </div>
          <div class="muted" style="font-size:13px;margin-bottom:12px">${esc(ch.title)} · תרגיל ${esc(ex.num)} בחוברת${ex.kind === "function" ? " · כתוב פונקציה" : ""}</div>
          <div class="prompt">${md(ex.prompt)}</div>
          ${examplesHtml(ex)}
          ${exam ? "" : `
          <div class="help-row">
            ${ex.hints.length ? `<button class="btn warn small" id="hintBtn"></button>` : ""}
            <button class="btn small" id="solBtn">👀 הצג פתרון</button>
          </div>
          <div id="hints"></div>
          <div id="solution"></div>
          <div class="ex-nav">
            ${prev ? `<a class="btn small" href="#/ex/${prev.id}">→ הקודם</a>` : "<span></span>"}
            ${next ? `<a class="btn small" href="#/ex/${next.id}">הבא ←</a>` : `<a class="btn small" href="#/ch/${ch.id}/ex">לרשימת התרגילים</a>`}
          </div>`}
        </section>
        <section class="card editor-panel">
          <div class="editor-bar">
            <span class="fname">solution.py</span>
            <button class="btn small" id="resetBtn" title="החזר לקוד ההתחלתי">↺</button>
            <button class="btn small go" id="runBtn">▶ הרץ <span class="kbd">Ctrl+↵</span></button>
            ${ex.kind === "manual"
              ? (exam ? "" : `<button class="btn small primary" id="doneBtn">✓ סמן שפתרתי</button>`)
              : `<button class="btn small primary" id="checkBtn">✓ בדוק</button>`}
          </div>
          <div id="editor"></div>
          <div class="io-split">
            <div class="io-box"><label>קלט (שורה לכל input)</label><textarea id="stdin" spellcheck="false"></textarea></div>
            <div class="io-box"><label>פלט</label><pre id="out"><span class="dim">לחץ ▶ הרץ כדי לראות את הפלט</span></pre></div>
          </div>
          <div id="results"></div>
        </section>
      </div>`;

    const starter = ex.starter || "";
    const cm = makeEditor(document.getElementById("editor"), codeStore[codeKey] ?? starter, (v) => {
      codeStore[codeKey] = v; (opts.onChange || save)();
    }, { "Ctrl-Enter": () => doRun(), "Cmd-Enter": () => doRun(), "Shift-Ctrl-Enter": () => doCheck(), "Shift-Cmd-Enter": () => doCheck() });
    const $stdin = document.getElementById("stdin");
    $stdin.value = defaultStdin(ex);
    const $out = document.getElementById("out");
    const $res = document.getElementById("results");

    document.getElementById("resetBtn").onclick = () => {
      if (cm.getValue() === starter || confirm("להחזיר את הקוד להתחלה? הקוד שכתבת יימחק.")) cm.setValue(starter);
    };
    const $run = document.getElementById("runBtn");
    $run.onclick = () => doRun();
    const $check = document.getElementById("checkBtn");
    if ($check) $check.onclick = () => doCheck();
    const $done = document.getElementById("doneBtn");
    if ($done) $done.onclick = () => { store.status[ex.id] = "solved"; markActiveToday(); save(true); updateTop(); toast("סומן כפתור 🎉"); renderExercise(ex); };

    async function doRun() {
      $run.disabled = true;
      $out.innerHTML = `<span class="dim">${Py.ready ? "מריץ…" : "מחכה שפייתון ייטען…"}</span>`;
      try {
        const r = await Py.run(cm.getValue(), $stdin.value);
        let html = esc(r.output);
        if (!r.output && !r.error) html = `<span class="dim">(אין פלט${ex.kind === "function" ? " — הקוד רק מגדיר פונקציה. כדי לנסות אותה הוסף למשל print(...) עם קריאה לפונקציה" : ""})</span>`;
        if (r.error) html += `<span class="err">❌ ${esc(r.error)}</span>`;
        $out.innerHTML = html;
      } catch (e) {
        $out.innerHTML = `<span class="err">${e.message === "timeout" ? TIMEOUT_MSG : esc(e.message)}</span>`;
      }
      $run.disabled = false;
    }

    async function doCheck() {
      if (!$check || $check.disabled) return;
      $check.disabled = true;
      const code = cm.getValue();
      const tests = ex.tests;
      $res.innerHTML = `<div class="results"><div class="summary">${Py.ready ? "בודק…" : "מחכה שפייתון ייטען…"}</div></div>`;
      const results = [];
      for (const t of tests) {
        try { results.push(await Py.testOne(code, t)); }
        catch (e) { results.push({ passed: false, got: "", expected: t.out ?? t.expect ?? "", error: e.message === "timeout" ? TIMEOUT_MSG : e.message }); }
      }
      const passed = results.filter((r) => r.passed).length;
      const all = passed === tests.length;
      if (exam) {
        opts.onResult && opts.onResult(passed, tests.length);
      } else {
        markActiveToday();
        if (all) store.status[ex.id] = "solved";
        else if (!isSolved(ex.id)) store.status[ex.id] = "tried";
        save(true); updateTop();
      }
      $res.innerHTML = `<div class="results">
        <div class="summary ${all ? "pass" : "fail"}">${all ? "✔ כל הבדיקות עברו!" : `✘ עברו ${passed} מתוך ${tests.length} בדיקות`}</div>
        ${results.map((r, i) => caseHtml(tests[i], r, i)).join("")}
      </div>
      ${all && !exam ? `<div class="celebrate">🎉 מעולה! ${store.saw[ex.id] ? "" : "פתרת בלי להציץ בפתרון."}
        ${next ? `<a class="btn go small" href="#/ex/${next.id}">לתרגיל הבא ←</a>` : `<a class="btn go small" href="#/ch/${ch.id}/ex">חזרה לפרק</a>`}</div>` : ""}`;
      const firstFail = $res.querySelector(".case.fail");
      if (firstFail) firstFail.open = true;
      $check.disabled = false;
      if (all && !exam) {
        $res.scrollIntoView({ behavior: "smooth", block: "nearest" });
        document.querySelector(".ex-title span").textContent = statusIcon(ex.id);
      }
    }

    if (exam) return cm;

    // hints
    const $hints = document.getElementById("hints");
    const $hintBtn = document.getElementById("hintBtn");
    let shown = hintsShown;
    const drawHints = () => {
      $hints.innerHTML = ex.hints.slice(0, shown).map((h, i) => `<div class="hint"><div class="hl">רמז ${i + 1}</div>${smartMd(h)}</div>`).join("");
      if ($hintBtn) {
        $hintBtn.textContent = shown >= ex.hints.length ? "אין עוד רמזים" : `💡 רמז (${shown + 1}/${ex.hints.length})`;
        $hintBtn.disabled = shown >= ex.hints.length;
      }
    };
    if ($hintBtn) $hintBtn.onclick = () => { shown++; store.hints[ex.id] = shown; save(); drawHints(); };
    drawHints();

    // solution
    const $sol = document.getElementById("solution");
    const drawSol = () => {
      $sol.innerHTML = `<div class="solution"><h3>פתרון לדוגמה</h3><pre>${esc(ex.solution)}</pre>${md(ex.explain)}
        <button class="btn small" id="loadSol">טען את הפתרון לעורך</button></div>`;
      document.getElementById("loadSol").onclick = () => {
        if (confirm("להחליף את הקוד שבעורך בפתרון?")) cm.setValue(ex.solution);
      };
      document.getElementById("solBtn").textContent = "🙈 הסתר פתרון";
    };
    document.getElementById("solBtn").onclick = () => {
      if ($sol.innerHTML) { $sol.innerHTML = ""; document.getElementById("solBtn").textContent = "👀 הצג פתרון"; return; }
      if (!store.status[ex.id] && !store.saw[ex.id] && !confirm("עוד לא ניסית לבדוק את הקוד. בטוח שאתה רוצה לראות את הפתרון? מנסים קודם = לומדים יותר 💪")) return;
      if (!isSolved(ex.id)) store.saw[ex.id] = true;
      save(); drawSol();
    };
    return cm;
  }

  function caseHtml(t, r, i) {
    const name = t.hidden ? `בדיקה ${i + 1} (נסתרת)` : `בדיקה ${i + 1}`;
    const what = "call" in t ? (t.setup ? t.setup + "\n" : "") + t.call + (t.check ? "\n# ואז בודקים: " + t.check : "") : null;
    return `<details class="case ${r.passed ? "pass" : "fail"}">
      <summary>${r.passed ? "✔" : "✘"} ${name}${!r.passed && r.error ? " — שגיאה" : ""}</summary>
      <div class="body">
        ${what != null ? `<div><div class="lbl">קריאה</div><pre>${esc(what)}</pre></div>` : `<div><div class="lbl">קלט</div><pre>${esc(t.stdin || "(אין)")}</pre></div>`}
        <div><div class="lbl">ציפינו ל</div><pre>${esc(r.expected)}</pre></div>
        <div><div class="lbl">התקבל</div><pre>${esc(r.got)}</pre></div>
        ${r.error ? `<div class="errline">❌ ${esc(r.error)}</div>` : ""}
      </div></details>`;
  }

  /* ------------------------------------------------------------------ exam mode */
  let examTimer = null;
  function renderExam() {
    clearInterval(examTimer);
    document.title = "מבחן תרגול · מאמן פייתון";
    const ex = store.exam;
    if (!ex) return renderExamSetup();
    if (ex.finished) return renderExamResult();
    const q = Math.min(ex.cur || 0, ex.ids.length - 1);
    const exercise = BY_ID[ex.ids[q]];
    if (!exercise) { store.exam = null; save(true); return renderExamSetup(); }
    const header = `<div class="exam-bar">
        <b>מבחן תרגול</b>
        ${ex.ids.map((id, i) => `<button class="q ${i === q ? "cur" : ""} ${ex.score[id] && ex.score[id][0] === ex.score[id][1] ? "done" : ""}" data-q="${i}">${i + 1}</button>`).join("")}
        <span class="timer" id="timer">--:--</span>
        <button class="btn primary small" id="finishExam">הגש מבחן</button>
      </div>`;
    renderExercise(exercise, {
      exam: true, header, codeKey: exercise.id, codeStore: ex.code,
      onChange: () => save(),
      onResult: (p, n) => { ex.score[exercise.id] = [p, n]; save(true); document.querySelector(`.q[data-q="${q}"]`).classList.toggle("done", p === n); },
    });
    $app.querySelectorAll(".exam-bar .q").forEach((b) => b.onclick = () => { ex.cur = +b.dataset.q; save(true); renderExam(); window.scrollTo(0, 0); });
    document.getElementById("finishExam").onclick = () => { if (confirm("להגיש את המבחן? הקוד של כל השאלות ייבדק.")) finishExam(); };
    const $t = document.getElementById("timer");
    const tick = () => {
      if (!ex.minutes) { const m = Math.floor((Date.now() - ex.start) / 60000); $t.textContent = `⏱ ${m} דק׳`; return; }
      const left = ex.start + ex.minutes * 60000 - Date.now();
      if (left <= 0) { clearInterval(examTimer); toast("הזמן נגמר! בודק את המבחן…"); finishExam(); return; }
      const m = Math.floor(left / 60000), s = Math.floor((left % 60000) / 1000);
      $t.textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
      $t.classList.toggle("low", left < 5 * 60000);
    };
    tick(); examTimer = setInterval(tick, 1000);
  }

  function renderExamSetup() {
    const pool = ALL.filter((e) => e.exam && e.kind !== "manual");
    const hist = (store.history || []).slice(-5).reverse();
    $app.innerHTML = `<div class="card exam-setup">
      <h1>📝 מבחן תרגול</h1>
      <p class="muted">שאלות אקראיות מתוך ${pool.length} שאלות שהופיעו במבחנים (קודם כאלה שעוד לא פתרת). בלי רמזים ובלי פתרונות — כמו במבחן אמיתי. בסוף מקבלים ציון לפי הבדיקות שעברו.</p>
      <div class="row"><label>מספר שאלות</label>
        <select id="nq">${[3, 4, 5, 6].map((n) => `<option ${n === 4 ? "selected" : ""}>${n}</option>`).join("")}</select>
        <label>זמן</label>
        <select id="mins"><option value="45">45 דקות</option><option value="90" selected>90 דקות</option><option value="120">שעתיים</option><option value="0">בלי שעון</option></select>
      </div>
      <div class="row"><label>נושאים</label>
        <select id="scope"><option value="all">כל הנושאים</option>${CHAPTERS.filter((c) => c.exercises.some((e) => e.exam)).map((c) => `<option value="${c.id}">${esc(c.title)}</option>`).join("")}</select>
      </div>
      <button class="btn primary" id="startExam" style="margin-top:10px">התחל מבחן</button>
      ${hist.length ? `<h3 style="margin-top:24px">מבחנים קודמים</h3><table style="width:100%">${hist.map((h) => `<tr><td>${new Date(h.date).toLocaleDateString("he-IL")}</td><td>${h.n} שאלות</td><td><b>${h.grade}</b></td></tr>`).join("")}</table>` : ""}
    </div>`;
    document.getElementById("startExam").onclick = () => {
      const n = +document.getElementById("nq").value;
      const scope = document.getElementById("scope").value;
      let p = pool.filter((e) => scope === "all" || e.chapter.id === scope);
      // prefer unsolved, then shuffle, and avoid two parts of the same workbook question
      p = shuffle(p).sort((a, b) => isSolved(a.id) - isSolved(b.id));
      const picked = [], seen = new Set();
      for (const e of p) {
        const base = e.id.replace(/[a-z]$/, "");
        if (seen.has(base)) continue;
        seen.add(base); picked.push(e);
        if (picked.length === n) break;
      }
      if (!picked.length) return toast("אין שאלות בנושא הזה");
      picked.sort((a, b) => ALL.indexOf(a) - ALL.indexOf(b));
      store.exam = { ids: picked.map((e) => e.id), start: Date.now(), minutes: +document.getElementById("mins").value, cur: 0, code: {}, score: {} };
      save(true); renderExam();
    };
  }
  function shuffle(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

  async function finishExam() {
    clearInterval(examTimer);
    const ex = store.exam;
    $app.innerHTML = `<div class="card exam-result"><h2>בודק את המבחן…</h2><p class="muted" id="prog"></p></div>`;
    for (const id of ex.ids) {
      const e = BY_ID[id];
      const code = ex.code[id] ?? e.starter;
      let p = 0;
      for (const t of e.tests) {
        document.getElementById("prog").textContent = `שאלה ${ex.ids.indexOf(id) + 1}…`;
        try { if ((await Py.testOne(code, t)).passed) p++; } catch { /* timeout counts as fail */ }
      }
      ex.score[id] = [p, e.tests.length];
      if (p === e.tests.length) { store.status[id] = "solved"; store.code[id] = code; }
    }
    ex.finished = true;
    ex.grade = Math.round(ex.ids.reduce((s, id) => s + ex.score[id][0] / ex.score[id][1], 0) / ex.ids.length * 100);
    store.history = (store.history || []).concat([{ date: Date.now(), n: ex.ids.length, grade: ex.grade }]).slice(-30);
    markActiveToday(); save(true); updateTop();
    renderExamResult();
  }

  function renderExamResult() {
    const ex = store.exam;
    const msg = ex.grade >= 90 ? "מצוין! אתה מוכן 🚀" : ex.grade >= 70 ? "יפה מאוד! עוד קצת ליטוש 💪" : ex.grade >= 55 ? "עברת — כדאי לחזור על הנושאים שנפלת בהם" : "לא נורא — זה בדיוק בשביל זה מתרגלים. חזור על השאלות למטה";
    $app.innerHTML = `<div class="card exam-result">
      <h1>תוצאות המבחן</h1>
      <div class="big">${ex.grade}</div><p>${msg}</p>
      <table>${ex.ids.map((id, i) => { const e = BY_ID[id], [p, n] = ex.score[id]; return `<tr>
        <td>${p === n ? "✔" : "✘"}</td><td>שאלה ${i + 1}: <a href="#/ex/${id}">${esc(e.title)}</a> <span class="muted">(${esc(e.chapter.title)})</span></td><td>${p}/${n} בדיקות</td></tr>`; }).join("")}</table>
      <p class="muted" style="font-size:14px">לחץ על שאלה כדי לפתוח אותה במצב רגיל — שם יש רמזים ופתרון. הקוד מהמבחן לא נשמר בה, אלא אם עברת את כל הבדיקות.</p>
      <div style="display:flex;gap:10px;margin-top:14px"><button class="btn primary" id="newExam">מבחן חדש</button><a class="btn" href="#/">לדף הבית</a></div>
    </div>`;
    document.getElementById("newExam").onclick = () => { store.exam = null; save(true); renderExam(); };
  }

  /* ------------------------------------------------------------------ playground */
  function renderPlay() {
    document.title = "מגרש משחקים · מאמן פייתון";
    const fromLearn = sessionStorage.getItem("play-code");
    sessionStorage.removeItem("play-code");
    const code = fromLearn ?? store.code.__play ?? 'name = input("מה השם שלך? ")\nprint(f"שלום {name}!")\n\nfor i in range(1, 6):\n    print(i, i ** 2)\n';
    $app.innerHTML = `
      <div class="crumbs"><a href="#/">בית</a> / מגרש משחקים</div>
      <h1>🧪 מגרש משחקים</h1>
      <p class="muted">מקום לנסות כל קוד שבא לך. הקלט נלקח מתיבת הקלט — שורה לכל קריאה ל-input().</p>
      <section class="card editor-panel" style="position:static">
        <div class="editor-bar"><span class="fname">playground.py</span><button class="btn small go" id="runBtn">▶ הרץ <span class="kbd">Ctrl+↵</span></button></div>
        <div id="editor"></div>
        <div class="io-split">
          <div class="io-box"><label>קלט</label><textarea id="stdin" spellcheck="false">שחר</textarea></div>
          <div class="io-box"><label>פלט</label><pre id="out"></pre></div>
        </div>
      </section>`;
    const $out = document.getElementById("out");
    const run = async () => {
      $out.innerHTML = `<span class="dim">${Py.ready ? "מריץ…" : "מחכה שפייתון ייטען…"}</span>`;
      try {
        const r = await Py.run(cm.getValue(), document.getElementById("stdin").value);
        $out.innerHTML = esc(r.output) + (r.error ? `<span class="err">❌ ${esc(r.error)}</span>` : "") || '<span class="dim">(אין פלט)</span>';
      } catch (e) { $out.innerHTML = `<span class="err">${e.message === "timeout" ? TIMEOUT_MSG : esc(e.message)}</span>`; }
    };
    const cm = makeEditor(document.getElementById("editor"), code, (v) => { store.code.__play = v; save(); }, { "Ctrl-Enter": run, "Cmd-Enter": run });
    document.getElementById("runBtn").onclick = run;
    if (fromLearn) run();
  }

  /* ------------------------------------------------------------------ boot */
  Py.start();
  route();
})();
