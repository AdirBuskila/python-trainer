CHAPTER = {
    "id": "lists",
    "title": "רשימות (מערכים)",
    "icon": "📋",
    "summary": "יצירה, אינדקסים, לולאות, חיתוך, מונים, מיון ומחרוזות כרצפים",
    "learn": [
        {"title": "מה זו רשימה ואיך ניגשים לאיברים",
         "text": "רשימה (`list`) היא מה שבשפות אחרות נקרא **מערך**: אוסף ערכים לפי סדר.\n\n"
                 "- יוצרים עם סוגריים מרובעים: `a = [4, 7, 1]`, רשימה ריקה: `a = []`\n"
                 "- `a[0]` הוא האיבר הראשון, `a[len(a) - 1]` האחרון\n"
                 "- אינדקס שלילי סופר מהסוף: `a[-1]` האחרון, `a[-2]` זה שלפניו\n"
                 "- `len(a)` הוא מספר האיברים\n"
                 "- אפשר לשנות איבר: `a[1] = 99`\n\n"
                 "גישה לאינדקס שלא קיים (למשל `a[3]` ברשימה של 3 איברים) נותנת `IndexError`.",
         "code": "a = [4, 7, 1]\nprint(a[0], a[-1], len(a))\na[1] = 99\nprint(a)"},
        {"title": "בניית רשימה עם append",
         "text": "`a.append(x)` מוסיף את `x` לסוף הרשימה. כך בונים רשימה חדשה בלולאה: מתחילים מרשימה ריקה ומוסיפים.\n\n"
                 "קליטת מספרים — שתי דרכים:\n"
                 "- מספר בכל שורה: `a.append(int(input()))` בתוך לולאה\n"
                 "- כולם בשורה אחת מופרדים ברווחים: `a = list(map(int, input().split()))`\n\n"
                 "הדפסת רשימה בשורה אחת עם רווחים: `print(*a)`.",
         "code": "a = []\nfor i in range(5):\n    a.append(i * i)\nprint(a)\nprint(*a)"},
        {"title": "לולאה על ערכים מול לולאה על אינדקסים",
         "text": "- `for x in a:` — מקבלים את **הערכים** אחד אחד. מתאים כשלא צריך לדעת את המיקום.\n"
                 "- `for i in range(len(a)):` — מקבלים את **האינדקסים** 0, 1, ..., ואת הערך דרך `a[i]`. "
                 "צריך את זה כשמשנים איברים, משווים לשכן (`a[i]` ו-`a[i + 1]`) או כשהמיקום חשוב.\n"
                 "- `for i, x in enumerate(a):` — גם אינדקס וגם ערך יחד.\n\n"
                 "כשמשווים לשכן `a[i + 1]` — הלולאה צריכה לרוץ עד `range(len(a) - 1)` כדי לא לצאת מהרשימה.",
         "code": "a = [10, 20, 30]\nfor x in a:\n    print(x)\nfor i in range(len(a)):\n    print(i, a[i])\nfor i, x in enumerate(a):\n    print(i, x)"},
        {"title": "חיתוך (slicing)",
         "text": "`a[start:stop:step]` מחזיר **רשימה חדשה** — מ-`start` ועד `stop` לא כולל.\n\n"
                 "- `a[1:4]` איברים 1, 2, 3\n"
                 "- `a[:3]` שלושת הראשונים, `a[3:]` מהרביעי עד הסוף\n"
                 "- `a[::2]` איברים במקומות הזוגיים 0, 2, 4...\n"
                 "- `a[::-1]` הרשימה הפוכה\n\n"
                 "גם על מחרוזות זה עובד: `'house'[1:]` הוא `'ouse'`.",
         "code": "a = [0, 1, 2, 3, 4, 5]\nprint(a[1:4], a[:3], a[3:])\nprint(a[::2], a[::-1])"},
        {"title": "פונקציות מוכנות שימושיות",
         "text": "- `sum(a)`, `max(a)`, `min(a)` — סכום, מקסימום, מינימום\n"
                 "- `a.count(x)` — כמה פעמים `x` מופיע\n"
                 "- `a.index(x)` — האינדקס של ההופעה **הראשונה** של `x` (שגיאה אם אינו קיים!)\n"
                 "- `x in a` — `True` אם `x` ברשימה\n"
                 "- `a.sort()` ממיין את הרשימה עצמה; `sorted(a)` מחזיר רשימה ממוינת חדשה\n\n"
                 "במבחן לעיתים מבקשים לממש את זה בעצמך עם לולאה — כדאי לדעת את שתי הדרכים.",
         "code": "a = [3, 8, 1, 8]\nprint(sum(a), max(a), min(a))\nprint(a.count(8), a.index(8), 5 in a)\na.sort()\nprint(a)"},
        {"title": "שינוי במקום מול רשימה חדשה",
         "text": "רשימה שמועברת לפונקציה **אינה מועתקת**: אם הפונקציה משנה `a[i]` או קוראת ל-`a.append`, "
                 "השינוי נראה גם בחוץ. זה \"שינוי במקום\" — אין צורך ב-`return`.\n\n"
                 "אם התרגיל מבקש **רשימה חדשה** — בנה רשימה אחרת (`b = []` ואז `append`) והחזר אותה, בלי לגעת במקורית.\n\n"
                 "החלפת שני איברים בפייתון: `a[i], a[j] = a[j], a[i]`.",
         "code": "def double_all(a):\n    for i in range(len(a)):\n        a[i] *= 2\n\nnums = [1, 2, 3]\ndouble_all(nums)\nprint(nums)\nnums[0], nums[2] = nums[2], nums[0]\nprint(nums)"},
        {"title": "מערך מונים",
         "text": "כשהערכים בטווח קטן וידוע (ספרות 0-9, ציונים 0-100), יוצרים רשימת מונים: `counts = [0] * 10`. "
                 "עבור כל ערך `x` מגדילים `counts[x] += 1`. בסוף `counts[d]` הוא מספר ההופעות של `d`.\n\n"
                 "אם הטווח לא מתחיל ב-0 (למשל 75-100) — מזיזים: `counts[x - 75] += 1`.\n\n"
                 "זה הרבה יותר יעיל מלספור כל ערך בנפרד בלולאה נוספת.",
         "code": "digits = [3, 1, 3, 9, 3]\ncounts = [0] * 10\nfor d in digits:\n    counts[d] += 1\nfor d in range(10):\n    if counts[d] > 0:\n        print(d, counts[d])"},
        {"title": "מחרוזות כרצפים, split ו-join",
         "text": "מחרוזת מתנהגת כמו רשימה של תווים: `len(s)`, `s[0]`, `s[-1]`, חיתוך ולולאת `for ch in s`. "
                 "ההבדל: אי אפשר לשנות תו במקום — בונים מחרוזת חדשה (`result += ch`).\n\n"
                 "- `s.split()` מפרק משפט לרשימת מילים\n"
                 "- `' '.join(words)` מחבר רשימת מחרוזות למחרוזת אחת\n"
                 "- `ch.isupper()`, `ch.islower()`, `word.startswith('d')`",
         "code": "s = 'cat Dragon dog'\nwords = s.split()\nprint(words, len(words))\nprint('-'.join(words))\nfor ch in 'aBc':\n    print(ch, ch.isupper())"},
    ],
    "pitfalls": [
        "האינדקס הראשון הוא `0` והאחרון הוא `len(a) - 1`. לולאה `range(len(a))` כבר עוצרת בזמן — אל תכתוב `range(len(a) + 1)`.",
        "כשמשווים `a[i]` ל-`a[i + 1]` הלולאה צריכה להיות `range(len(a) - 1)`, אחרת `IndexError` באיבר האחרון.",
        "`b = a` **לא** מעתיק — שני השמות מצביעים לאותה רשימה. העתקה אמיתית: `b = a[:]` או `b = list(a)`.",
        "לולאה `for x in a:` ואז `x = 0` **לא** משנה את הרשימה. כדי לשנות צריך `a[i] = ...` עם אינדקס.",
        "`a.sort()` מחזיר `None` — אל תכתוב `a = a.sort()`.",
        "פונקציה שמתבקשת **להחזיר** — השתמש ב-`return`, לא ב-`print`.",
    ],
    "exercises": [
        # ---------------------------------------------------------------- 1
        {
            "id": "lists-01", "num": "1", "title": "סכום, מכפלה וממוצע",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `sum_prod_avg(a)` שמקבלת רשימה לא ריקה של מספרים ומחשבת את סכום האיברים, את מכפלתם ואת הממוצע שלהם.\n\n"
                      "(בחוברת יש בדיוק 10 ערכים — כאן הרשימה יכולה להיות בכל אורך.)\n\n"
                      "לדוגמה: עבור `[1, 2, 3, 4]` מוחזר `(10, 24, 2.5)`.\n\n"
                      "**החזר:** שלושה ערכים — `return s, p, avg` (סכום, מכפלה, ממוצע).",
            "starter": "def sum_prod_avg(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "צריך שני משתנים מצטברים: סכום שמתחיל ב-0 ומכפלה שמתחילה ב-1.",
                "עבור על הערכים עם `for x in a:` — הוסף לסכום והכפל במכפלה. הממוצע הוא הסכום חלקי `len(a)`.",
                "s = 0\np = 1\nfor x in a:\n    s += x\n    p *= x\nreturn s, p, s / len(a)",
            ],
            "solution": "def sum_prod_avg(a):\n    s = 0\n    p = 1\n    for x in a:\n        s += x\n        p *= x\n    return s, p, s / len(a)\n",
            "explain": "מכפלה מתחילה ב-1 ולא ב-0 — אחרת הכול יוצא 0. הממוצע הוא הסכום חלקי מספר האיברים, `len(a)`. "
                       "בפייתון אפשר להחזיר כמה ערכים יחד (`return s, p, avg`) — הם חוזרים כ-tuple. אפשר גם `sum(a)` לסכום.",
            "tests": [
                {"call": "sum_prod_avg([1, 2, 3, 4])", "expect": "(10, 24, 2.5)"},
                {"call": "sum_prod_avg([5])", "expect": "(5, 5, 5.0)"},
                {"call": "sum_prod_avg([2, -3, 0])", "expect": "(-1, 0, -0.3333333333)", "hidden": True},
                {"call": "sum_prod_avg([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])", "expect": "(100, 10000000000, 10.0)", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 2
        {
            "id": "lists-02", "num": "2", "title": "חיוביים ושליליים",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `count_signs(a)` שמקבלת רשימת מספרים וסופרת כמה מהם חיוביים וכמה שליליים. האפס אינו חיובי ואינו שלילי.\n\n"
                      "(בחוברת 20 מספרים — כאן כל אורך.)\n\n"
                      "לדוגמה: עבור `[1, -2, 0, 5]` מוחזר `(2, 1)`.\n\n"
                      "**החזר:** `return pos, neg`.",
            "starter": "def count_signs(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שני מונים שמתחילים ב-0.",
                "בלולאה על הערכים: אם `x > 0` הגדל את מונה החיוביים, אחרת אם `x < 0` את מונה השליליים.",
                "pos = 0\nneg = 0\nfor x in a:\n    if x > 0:\n        pos += 1\n    elif x < 0:\n        neg += 1",
            ],
            "solution": "def count_signs(a):\n    pos = 0\n    neg = 0\n    for x in a:\n        if x > 0:\n            pos += 1\n        elif x < 0:\n            neg += 1\n    return pos, neg\n",
            "explain": "זו תבנית המונה: מאתחלים ל-0 ומגדילים כשהתנאי מתקיים. שימוש ב-`elif` (ולא `else`) חשוב כדי שאפסים לא ייספרו כשליליים.",
            "tests": [
                {"call": "count_signs([1, -2, 0, 5])", "expect": "(2, 1)"},
                {"call": "count_signs([0, 0])", "expect": "(0, 0)"},
                {"call": "count_signs([])", "expect": "(0, 0)", "hidden": True},
                {"call": "count_signs([-1, -1, -7, 3])", "expect": "(1, 3)", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 3
        {
            "id": "lists-03", "num": "3", "title": "הפרש מהממוצע",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `print_avg_diffs(a)` שמקבלת רשימה לא ריקה של מספרים ו**מדפיסה** שלוש שורות:\n\n"
                      "- בשורה הראשונה — סכום האיברים\n"
                      "- בשורה השנייה — הממוצע\n"
                      "- בשורה השלישית — לכל איבר לפי הסדר, ההפרש שלו מהממוצע (`איבר - ממוצע`), מופרדים ברווחים\n\n"
                      "לדוגמה: עבור `[1, 2, 3, 4, 5]` יודפס:\n```\n15\n3.0\n-2.0 -1.0 0.0 1.0 2.0\n```\n"
                      "**פלט:** שלוש השורות בלבד (הפונקציה לא מחזירה דבר).",
            "starter": "def print_avg_diffs(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "קודם חשב את הסכום ואת הממוצע — רק אחרי שיש ממוצע אפשר לחשב הפרשים. כלומר צריך לעבור על הרשימה פעמיים.",
                "בנה רשימת הפרשים חדשה עם `append` ואז הדפס אותה עם `print(*diffs)`.",
                "s = sum(a)\navg = s / len(a)\nprint(s)\nprint(avg)\ndiffs = []\nfor x in a:\n    diffs.append(x - avg)\nprint(*diffs)",
            ],
            "solution": "def print_avg_diffs(a):\n    s = sum(a)\n    avg = s / len(a)\n    print(s)\n    print(avg)\n    diffs = []\n    for x in a:\n        diffs.append(x - avg)\n    print(*diffs)\n",
            "explain": "זו הסיבה הקלאסית לשמור נתונים ברשימה: את הממוצע יודעים רק אחרי שעוברים על כל המספרים, ואז צריך לעבור עליהם שוב. "
                       "`print(*diffs)` מדפיס את האיברים בשורה אחת עם רווחים.",
            "tests": [
                {"call": "print_avg_diffs([1, 2, 3, 4, 5])", "out": "15\n3\n-2 -1 0 1 2"},
                {"call": "print_avg_diffs([7])", "out": "7\n7\n0"},
                {"call": "print_avg_diffs([1, 2])", "out": "3\n1.5\n-0.5 0.5", "hidden": True},
                {"call": "print_avg_diffs([-4, 0, 10])", "out": "6\n2\n-6 -2 8", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 4
        {
            "id": "lists-04", "num": "4", "title": "מקומות זוגיים",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `even_positions(a)` שמחזירה רשימה חדשה ובה רק האיברים שנמצאים באינדקסים הזוגיים של `a` (0, 2, 4, ...).\n\n"
                      "לדוגמה: עבור `[10, 20, 30, 40, 50]` מוחזר `[10, 30, 50]`.\n\n"
                      "**החזר:** רשימה חדשה.",
            "starter": "def even_positions(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "כאן המיקום חשוב, לא הערך — עבור על אינדקסים.",
                "`range(0, len(a), 2)` נותן בדיוק 0, 2, 4, ...",
                "result = []\nfor i in range(0, len(a), 2):\n    result.append(a[i])\nreturn result",
            ],
            "solution": "def even_positions(a):\n    result = []\n    for i in range(0, len(a), 2):\n        result.append(a[i])\n    return result\n",
            "explain": "`range` עם צעד 2 עובר רק על האינדקסים הזוגיים. דרך קצרה יותר היא חיתוך: `a[::2]`.",
            "tests": [
                {"call": "even_positions([10, 20, 30, 40, 50])", "expect": "[10, 30, 50]"},
                {"call": "even_positions([7])", "expect": "[7]"},
                {"call": "even_positions([])", "expect": "[]", "hidden": True},
                {"call": "even_positions([1, 2, 3, 4])", "expect": "[1, 3]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 5
        {
            "id": "lists-05", "num": "5", "title": "הזזה ימינה",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `rotate_right(a)` שמזיזה את כל איברי הרשימה מקום אחד ימינה (לאינדקס הבא), והאיבר האחרון עובר למקום הראשון.\n\n"
                      "הפונקציה **משנה את הרשימה עצמה** ולא מחזירה דבר.\n\n"
                      "לדוגמה: אחרי `rotate_right(a)` כאשר `a = [1, 2, 3, 4]`, הרשימה תהיה `[4, 1, 2, 3]`.",
            "starter": "def rotate_right(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שמור קודם את האיבר האחרון במשתנה — אחרת הוא יידרס.",
                "הזז מהסוף להתחלה: `a[i] = a[i - 1]` עבור i מ-`len(a) - 1` עד 1. אם תזיז מההתחלה, תעתיק את אותו ערך שוב ושוב.",
                "if len(a) == 0:\n    return\nlast = a[-1]\nfor i in range(len(a) - 1, 0, -1):\n    a[i] = a[i - 1]\na[0] = last",
            ],
            "solution": "def rotate_right(a):\n    if len(a) == 0:\n        return\n    last = a[-1]\n    # מזיזים מהסוף להתחלה כדי לא לדרוס ערכים\n    for i in range(len(a) - 1, 0, -1):\n        a[i] = a[i - 1]\n    a[0] = last\n",
            "explain": "כשמזיזים ימינה חייבים לעבור מהסוף להתחלה, אחרת `a[1] = a[0]` ואז `a[2] = a[1]` מעתיקים את אותו ערך לכל מקום. "
                       "האחרון נשמר מראש ומוצב בסוף ב-`a[0]`. אין צורך ב-`return` כי הרשימה שונתה במקום.",
            "tests": [
                {"setup": "a = [1, 2, 3, 4]", "call": "rotate_right(a)", "check": "a", "expect": "[4, 1, 2, 3]"},
                {"setup": "a = [1, 2]", "call": "rotate_right(a)", "check": "a", "expect": "[2, 1]"},
                {"setup": "a = [9]", "call": "rotate_right(a)", "check": "a", "expect": "[9]", "hidden": True},
                {"setup": "a = [5, 6, 7, 8, 9, 10]", "call": "rotate_right(a)", "check": "a", "expect": "[10, 5, 6, 7, 8, 9]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 6
        {
            "id": "lists-06", "num": "6", "title": "הדפסה הפוכה",
            "kind": "program", "difficulty": 1, "exam": False,
            "prompt": "כתוב תוכנית שקולטת מספרים לרשימה ומדפיסה אותם בסדר הפוך.\n\n"
                      "קודם נקלט `N` (כמה מספרים יהיו), ואחריו `N` מספרים שלמים — אחד בכל שורה. (בחוברת N=10.)\n\n"
                      "**קלט:** שורה עם N, ואז N שורות עם מספר בכל אחת.\n"
                      "**פלט:** המספרים בסדר הפוך, בשורה אחת מופרדים ברווחים.",
            "starter": "n = int(input())\n# כתוב כאן את הקוד\n",
            "hints": [
                "צור רשימה ריקה והוסף אליה כל מספר שנקלט עם `append`.",
                "להדפסה הפוכה: לולאה על אינדקסים מ-`n - 1` עד 0 — `range(n - 1, -1, -1)`. או פשוט `a[::-1]`.",
                "a = []\nfor i in range(n):\n    a.append(int(input()))\nprint(*a[::-1])",
            ],
            "solution": "n = int(input())\na = []\nfor i in range(n):\n    a.append(int(input()))\nresult = []\nfor i in range(n - 1, -1, -1):\n    result.append(a[i])\nprint(*result)\n",
            "explain": "קליטה לרשימה: לולאה של N פעמים עם `a.append(int(input()))`. "
                       "`range(n - 1, -1, -1)` רץ אחורה עד 0 כולל (ה-stop הוא -1 כי הוא לא נכלל). הקיצור הפייתוני: `a[::-1]`.",
            "tests": [
                {"stdin": "4\n1\n2\n3\n4\n", "out": "4 3 2 1"},
                {"stdin": "1\n7\n", "out": "7"},
                {"stdin": "10\n5\n-3\n8\n0\n1\n2\n9\n9\n4\n6\n", "out": "6 4 9 9 2 1 0 8 -3 5", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 7
        {
            "id": "lists-07", "num": "7", "title": "החלפת זוגות",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `swap_pairs(a)` שמחליפה כל זוג איברים סמוכים: האיבר שבאינדקס 0 עם זה שבאינדקס 1, 2 עם 3, 4 עם 5 וכן הלאה. "
                      "אם אורך הרשימה אי-זוגי, האיבר האחרון נשאר במקומו.\n\n"
                      "הפונקציה **משנה את הרשימה עצמה**.\n\n"
                      "לדוגמה: `[1, 2, 3, 4]` הופכת ל-`[2, 1, 4, 3]`, ו-`[1, 2, 3]` הופכת ל-`[2, 1, 3]`.",
            "starter": "def swap_pairs(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על האינדקסים הזוגיים בלבד: 0, 2, 4...",
                "לכל `i` כזה החלף בין `a[i]` ל-`a[i + 1]` — אבל רק אם `i + 1` קיים. `range(0, len(a) - 1, 2)` דואג לזה.",
                "for i in range(0, len(a) - 1, 2):\n    a[i], a[i + 1] = a[i + 1], a[i]",
            ],
            "solution": "def swap_pairs(a):\n    for i in range(0, len(a) - 1, 2):\n        a[i], a[i + 1] = a[i + 1], a[i]\n",
            "explain": "הלולאה קופצת ב-2 כדי שכל זוג יוחלף פעם אחת. הגבול `len(a) - 1` מונע גישה ל-`a[i + 1]` מחוץ לרשימה כשהאורך אי-זוגי. "
                       "ההחלפה `a[i], a[i + 1] = a[i + 1], a[i]` היא הדרך הפייתונית — בלי משתנה עזר.",
            "tests": [
                {"setup": "a = [1, 2, 3, 4]", "call": "swap_pairs(a)", "check": "a", "expect": "[2, 1, 4, 3]"},
                {"setup": "a = [1, 2, 3]", "call": "swap_pairs(a)", "check": "a", "expect": "[2, 1, 3]"},
                {"setup": "a = [5]", "call": "swap_pairs(a)", "check": "a", "expect": "[5]", "hidden": True},
                {"setup": "a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]", "call": "swap_pairs(a)", "check": "a", "expect": "[8, 9, 6, 7, 4, 5, 2, 3, 0, 1]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 8
        {
            "id": "lists-08", "num": "8", "title": "רק החיוביים",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `positives(a)` שמחזירה **רשימה חדשה** ובה רק המספרים החיוביים (גדולים מ-0) מתוך `a`, באותו סדר.\n\n"
                      "לדוגמה: עבור `[3, -1, 0, 7]` מוחזר `[3, 7]`.\n\n"
                      "**החזר:** רשימה חדשה (אם אין חיוביים — רשימה ריקה).",
            "starter": "def positives(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "התחל מרשימה ריקה `result = []`.",
                "עבור על הערכים, ולכל `x > 0` עשה `result.append(x)`.",
                "result = []\nfor x in a:\n    if x > 0:\n        result.append(x)\nreturn result",
            ],
            "solution": "def positives(a):\n    result = []\n    for x in a:\n        if x > 0:\n            result.append(x)\n    return result\n",
            "explain": "זו תבנית ה\"סינון\": רשימה ריקה + `append` לכל ערך שעומד בתנאי. הרשימה המקורית לא משתנה, והגודל של החדשה נקבע לפי כמה ערכים עברו את התנאי.",
            "tests": [
                {"call": "positives([3, -1, 0, 7])", "expect": "[3, 7]"},
                {"call": "positives([-1, -5])", "expect": "[]"},
                {"call": "positives([1, 2])", "expect": "[1, 2]", "hidden": True},
                {"call": "positives([0, 4, -4, 4])", "expect": "[4, 4]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 9
        {
            "id": "lists-09", "num": "9", "title": "סכומים מצטברים",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `prefix_sums(a)` שמחליפה כל איבר ברשימה בסכום של כל האיברים שלפניו **כולל אותו עצמו** (לפי הערכים המקוריים).\n\n"
                      "הפונקציה **משנה את הרשימה עצמה**.\n\n"
                      "לדוגמה: `[1, 2, 3, 4]` הופכת ל-`[1, 3, 6, 10]`.",
            "starter": "def prefix_sums(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "אין צורך לסכם מחדש בכל פעם — שמור סכום רץ.",
                "בלולאה על האינדקסים: הוסף את `a[i]` לסכום הרץ, ואז שים את הסכום ב-`a[i]`.",
                "total = 0\nfor i in range(len(a)):\n    total += a[i]\n    a[i] = total",
            ],
            "solution": "def prefix_sums(a):\n    total = 0\n    for i in range(len(a)):\n        total += a[i]\n        a[i] = total\n",
            "explain": "הסכום הרץ `total` מכיל בכל רגע את סכום כל מה שעברנו. כי אנחנו קוראים את `a[i]` לפני שדורסים אותו, הסכום תמיד מחושב מהערכים המקוריים. "
                       "צריך לולאת אינדקסים כי משנים את הרשימה.",
            "tests": [
                {"setup": "a = [1, 2, 3, 4]", "call": "prefix_sums(a)", "check": "a", "expect": "[1, 3, 6, 10]"},
                {"setup": "a = [5]", "call": "prefix_sums(a)", "check": "a", "expect": "[5]"},
                {"setup": "a = [2, -2, 5]", "call": "prefix_sums(a)", "check": "a", "expect": "[2, 0, 5]", "hidden": True},
                {"setup": "a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]", "call": "prefix_sums(a)", "check": "a", "expect": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 10
        {
            "id": "lists-10", "num": "10", "title": "פיבונאצ'י הפוך",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "סדרת פיבונאצ'י מתחילה ב-`0, 1` וכל איבר הבא הוא סכום שני הקודמים: `0 1 1 2 3 5 8 13 ...`\n\n"
                      "כתוב פונקציה `fib_reversed(n)` שבונה רשימה של `n` איברי הסדרה הראשונים (n ≥ 1) ומחזירה אותה **בסדר הפוך**.\n\n"
                      "לדוגמה: `fib_reversed(8)` מחזירה `[13, 8, 5, 3, 2, 1, 1, 0]`.\n\n"
                      "**החזר:** הרשימה ההפוכה.",
            "starter": "def fib_reversed(n):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "התחל מ-`fib = [0, 1]` והוסף איברים עד שיש n.",
                "האיבר הבא הוא `fib[-1] + fib[-2]` — שני האחרונים. שים לב למקרה n=1 (רק `[0]`).",
                "fib = [0, 1]\nwhile len(fib) < n:\n    fib.append(fib[-1] + fib[-2])\nfib = fib[:n]\nreturn fib[::-1]",
            ],
            "solution": "def fib_reversed(n):\n    fib = [0, 1]\n    while len(fib) < n:\n        fib.append(fib[-1] + fib[-2])\n    fib = fib[:n]  # אם n == 1 נשאר רק [0]\n    return fib[::-1]\n",
            "explain": "אינדקסים שליליים נוחים כאן: `fib[-1]` ו-`fib[-2]` הם תמיד שני האחרונים, בלי לחשב אינדקס. "
                       "`fib[:n]` חותך למקרה ש-n=1, ו-`[::-1]` הופך את הרשימה.",
            "tests": [
                {"call": "fib_reversed(8)", "expect": "[13, 8, 5, 3, 2, 1, 1, 0]"},
                {"call": "fib_reversed(1)", "expect": "[0]"},
                {"call": "fib_reversed(2)", "expect": "[1, 0]", "hidden": True},
                {"call": "fib_reversed(5)", "expect": "[3, 2, 1, 1, 0]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 11
        {
            "id": "lists-11", "num": "11", "title": "המשכורת הגבוהה",
            "kind": "program", "difficulty": 1, "exam": False,
            "prompt": "כתוב תוכנית שקולטת רשימת משכורות ומדפיסה את המשכורת הגבוהה ביותר.\n\n"
                      "הפעם כל המשכורות מגיעות **בשורה אחת, מופרדות ברווחים** (בחוברת 10 משכורות — כאן כל כמות). "
                      "כך קולטים שורה כזו לרשימת מספרים:\n```\na = list(map(int, input().split()))\n```\n"
                      "`split()` מפרק את השורה למחרוזות, `map(int, ...)` ממיר כל אחת למספר, ו-`list` הופך לרשימה.\n\n"
                      "**קלט:** שורה אחת של מספרים שלמים מופרדים ברווחים.\n"
                      "**פלט:** רק המשכורת הגבוהה ביותר.",
            "starter": "a = list(map(int, input().split()))\n# כתוב כאן את הקוד\n",
            "hints": [
                "אפשר `max(a)` — אבל כדאי לדעת גם לממש בלולאה, זה נשאל במבחנים.",
                "התחל מ-`best = a[0]` (לא מ-0! מה אם כולם שליליים?) ועבור על השאר.",
                "best = a[0]\nfor x in a:\n    if x > best:\n        best = x\nprint(best)",
            ],
            "solution": "a = list(map(int, input().split()))\nbest = a[0]\nfor x in a:\n    if x > best:\n        best = x\nprint(best)\n",
            "explain": "מציאת מקסימום: מתחילים מהאיבר הראשון ומעדכנים בכל פעם שמוצאים גדול יותר. "
                       "מתחילים מ-`a[0]` ולא מ-0, כדי שזה יעבוד גם לערכים שליליים. בפייתון `max(a)` עושה את אותו הדבר.",
            "tests": [
                {"stdin": "5000 7200 6100\n", "out": "7200"},
                {"stdin": "9000\n", "out": "9000"},
                {"stdin": "4000 4000 3999 12000 8000 7000 6500 5000 3000 11999\n", "out": "12000", "hidden": True},
                {"stdin": "15000 100 200\n", "out": "15000", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 12
        {
            "id": "lists-12", "num": "12", "title": "ציונים 75-100",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `print_grade_counts(grades)` שמקבלת רשימת ציונים, כולם בטווח 75 עד 100, ומדפיסה כמה פעמים הופיע כל ציון.\n\n"
                      "חשוב על דרך **יעילה**: מעבר אחד על הרשימה בעזרת מערך מונים, בלי לספור כל ציון בנפרד. (בחוברת 120 ציונים — כאן כל כמות.)\n\n"
                      "לדוגמה: עבור `[75, 80, 75, 100]` יודפס:\n```\n75 2\n80 1\n100 1\n```\n"
                      "**פלט:** לכל ציון שהופיע לפחות פעם אחת, מהקטן לגדול — שורה עם הציון ומספר ההופעות, מופרדים ברווח.",
            "starter": "def print_grade_counts(grades):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "יש 26 ציונים אפשריים (75..100). צור `counts = [0] * 26`.",
                "ציון `g` נספר ב-`counts[g - 75]`. בסוף, האינדקס `i` מייצג את הציון `i + 75`.",
                "counts = [0] * 26\nfor g in grades:\n    counts[g - 75] += 1\nfor i in range(26):\n    if counts[i] > 0:\n        print(i + 75, counts[i])",
            ],
            "solution": "def print_grade_counts(grades):\n    counts = [0] * 26  # אינדקס 0 = ציון 75, אינדקס 25 = ציון 100\n    for g in grades:\n        counts[g - 75] += 1\n    for i in range(26):\n        if counts[i] > 0:\n            print(i + 75, counts[i])\n",
            "explain": "מערך מונים עם הזזה: הציון 75 נשמר באינדקס 0, ולכן `g - 75`. כך עוברים על הציונים פעם אחת בלבד, "
                       "במקום לולאה נפרדת לכל אחד מ-26 הציונים. ההדפסה בסדר עולה מגיעה \"בחינם\" כי עוברים על האינדקסים לפי הסדר.",
            "tests": [
                {"call": "print_grade_counts([75, 80, 75, 100])", "out": "75 2\n80 1\n100 1"},
                {"call": "print_grade_counts([90])", "out": "90 1"},
                {"call": "print_grade_counts([100, 99, 100, 76, 76, 76])", "out": "76 3\n99 1\n100 2", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 13
        {
            "id": "lists-13", "num": "13", "title": "רצפי אחדות",
            "kind": "function", "difficulty": 3, "exam": False,
            "prompt": "כתוב פונקציה `ones_runs(bits)` שמקבלת רשימה של אפסים ואחדות, וסופרת **רצפים** של אחדות לפי האורך שלהם.\n\n"
                      "לדוגמה, עבור `11010111010101111011` (כרשימה `[1, 1, 0, 1, 0, 1, 1, 1, 0, ...]`) יש 3 רצפים באורך 1, 2 רצפים באורך 2, רצף אחד באורך 3 ורצף אחד באורך 4. יודפס:\n"
                      "```\n1 3\n2 2\n3 1\n4 1\n```\n"
                      "**פלט:** לכל אורך רצף שהופיע, מהקצר לארוך — שורה עם האורך ומספר הרצפים באורך הזה. אם אין אף `1` ברשימה — הדפס `No ones`. "
                      "(רשימה שכולה אחדות היא רצף אחד ארוך.)",
            "starter": "def ones_runs(bits):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שמור משתנה `run` — אורך הרצף הנוכחי. כל `1` מגדיל אותו; `0` מסיים את הרצף.",
                "כשרצף מסתיים (ב-`0`, וגם **אחרי הלולאה** — אולי הרשימה מסתיימת ב-1) ו-`run > 0`, הגדל את `counts[run]`. "
                "רצף לא יכול להיות ארוך מהרשימה, אז `counts = [0] * (len(bits) + 1)`.",
                "for b in bits:\n    if b == 1:\n        run += 1\n    else:\n        if run > 0:\n            counts[run] += 1\n        run = 0\nif run > 0:\n    counts[run] += 1",
            ],
            "solution": "def ones_runs(bits):\n    counts = [0] * (len(bits) + 1)  # counts[k] = כמה רצפים באורך k\n    run = 0\n    for b in bits:\n        if b == 1:\n            run += 1\n        else:\n            if run > 0:\n                counts[run] += 1\n            run = 0\n    if run > 0:  # רצף שנגמר בסוף הרשימה\n        counts[run] += 1\n    if sum(counts) == 0:\n        print('No ones')\n        return\n    for k in range(1, len(counts)):\n        if counts[k] > 0:\n            print(k, counts[k])\n",
            "explain": "שני רעיונות: מונה רצף (`run`) שמתאפס כשהרצף נשבר, ומערך מונים לפי אורך. "
                       "הטעות הנפוצה היא לשכוח את הרצף האחרון — אם הרשימה מסתיימת ב-1, אין `0` שיסגור אותו, ולכן בודקים שוב אחרי הלולאה.",
            "tests": [
                {"call": "ones_runs([1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1])", "out": "1 3\n2 2\n3 1\n4 1"},
                {"call": "ones_runs([0, 0, 0])", "out": "No ones"},
                {"call": "ones_runs([1, 1, 1])", "out": "3 1", "hidden": True},
                {"call": "ones_runs([0, 1, 0, 1, 1, 0])", "out": "1 1\n2 1", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 14a
        {
            "id": "lists-14a", "num": "14", "title": "מיון בועות",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `bubble_sort(a)` שממיינת את הרשימה מהקטן לגדול בשיטת **מיון בועות**, ומשנה את הרשימה עצמה.\n\n"
                      "בכל סבב משווים כל זוג שכנים `a[j]`, `a[j + 1]`, ואם הם בסדר הפוך — מחליפים. אחרי הסבב הראשון הגדול ביותר \"צף\" לסוף, אחרי השני — השני בגודלו, וכן הלאה.\n\n"
                      "אל תשתמש ב-`sort()` או `sorted()` — המטרה לממש בעצמך.\n\n"
                      "לדוגמה: `[5, 2, 9, 1]` הופכת ל-`[1, 2, 5, 9]`.",
            "starter": "def bubble_sort(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שתי לולאות מקוננות: החיצונית סופרת סבבים, הפנימית עוברת על זוגות שכנים.",
                "בסבב מספר `i` (מ-0), `i` האיברים האחרונים כבר במקומם — לכן הפנימית רצה `range(len(a) - 1 - i)`.",
                "n = len(a)\nfor i in range(n - 1):\n    for j in range(n - 1 - i):\n        if a[j] > a[j + 1]:\n            a[j], a[j + 1] = a[j + 1], a[j]",
            ],
            "solution": "def bubble_sort(a):\n    n = len(a)\n    for i in range(n - 1):\n        for j in range(n - 1 - i):\n            if a[j] > a[j + 1]:\n                a[j], a[j + 1] = a[j + 1], a[j]\n",
            "explain": "כל סבב מזיז את הגדול ביותר שעוד לא במקומו אל הסוף, ולכן אחרי n-1 סבבים הכול ממוין. "
                       "הגבול `n - 1 - i` חוסך השוואות מיותרות וגם מונע יציאה מהרשימה ב-`a[j + 1]`.",
            "tests": [
                {"setup": "a = [5, 2, 9, 1]", "call": "bubble_sort(a)", "check": "a", "expect": "[1, 2, 5, 9]"},
                {"setup": "a = [3, 3, 1]", "call": "bubble_sort(a)", "check": "a", "expect": "[1, 3, 3]"},
                {"setup": "a = []", "call": "bubble_sort(a)", "check": "a", "expect": "[]", "hidden": True},
                {"setup": "a = [-1, -5, 0, 10, 7, 7, 2]", "call": "bubble_sort(a)", "check": "a", "expect": "[-5, -1, 0, 2, 7, 7, 10]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 14b
        {
            "id": "lists-14b", "num": "14", "title": "מיון בחירה",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "דרך נוספת למיין: כתוב פונקציה `selection_sort(a)` שממיינת את הרשימה מהקטן לגדול בשיטת **מיון בחירה**, ומשנה את הרשימה עצמה.\n\n"
                      "לכל מקום `i` מההתחלה: מוצאים את האינדקס של האיבר הקטן ביותר בחלק `a[i:]`, ומחליפים אותו עם `a[i]`.\n\n"
                      "אל תשתמש ב-`sort()`, `sorted()` או `min()`.\n\n"
                      "לדוגמה: `[5, 2, 9, 1]` הופכת ל-`[1, 2, 5, 9]`.",
            "starter": "def selection_sort(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "לולאה חיצונית על `i`, ובתוכה חיפוש אינדקס המינימום מ-`i` עד הסוף.",
                "התחל מ-`min_i = i`, ועבור `j` מ-`i + 1`: אם `a[j] < a[min_i]` עדכן `min_i = j`. אחרי הלולאה הפנימית — החלף.",
                "for i in range(len(a)):\n    min_i = i\n    for j in range(i + 1, len(a)):\n        if a[j] < a[min_i]:\n            min_i = j\n    a[i], a[min_i] = a[min_i], a[i]",
            ],
            "solution": "def selection_sort(a):\n    for i in range(len(a)):\n        min_i = i\n        for j in range(i + 1, len(a)):\n            if a[j] < a[min_i]:\n                min_i = j\n        a[i], a[min_i] = a[min_i], a[i]\n",
            "explain": "אחרי שלב `i`, התחילית `a[:i + 1]` כבר ממוינת ומכילה את הקטנים ביותר. שומרים את **האינדקס** של המינימום (לא את הערך), כדי שנוכל להחליף. "
                       "בחיים האמיתיים פשוט כותבים `a.sort()` — אבל במבחן מבקשים לממש.",
            "tests": [
                {"setup": "a = [5, 2, 9, 1]", "call": "selection_sort(a)", "check": "a", "expect": "[1, 2, 5, 9]"},
                {"setup": "a = [4]", "call": "selection_sort(a)", "check": "a", "expect": "[4]"},
                {"setup": "a = [3, 1, 3, 1, 2]", "call": "selection_sort(a)", "check": "a", "expect": "[1, 1, 2, 3, 3]", "hidden": True},
                {"setup": "a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]", "call": "selection_sort(a)", "check": "a", "expect": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 15
        {
            "id": "lists-15", "num": "15", "title": "מיקום בחזקת שלוש",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `count_cube_positions(a)` שמחזירה כמה איברים ברשימה שווים **למיקום שלהם בחזקת שלוש**, כאשר המיקום נספר **מ-1** (האיבר הראשון במיקום 1).\n\n"
                      "לדוגמה: עבור `[1, 4, 27, 5, 125, 80, 16, 2, 400, 1000]` מוחזר `4`: "
                      "1 במיקום 1 (1³=1), 27 במיקום 3, 125 במיקום 5 ו-1000 במיקום 10.\n\n"
                      "**החזר:** מספר האיברים.",
            "starter": "def count_cube_positions(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "צריך גם את האינדקס וגם את הערך — `range(len(a))` או `enumerate`.",
                "האינדקס בפייתון מתחיל מ-0, אז המיקום הוא `i + 1`. חזקה: `(i + 1) ** 3`.",
                "count = 0\nfor i in range(len(a)):\n    if a[i] == (i + 1) ** 3:\n        count += 1\nreturn count",
            ],
            "solution": "def count_cube_positions(a):\n    count = 0\n    for i in range(len(a)):\n        if a[i] == (i + 1) ** 3:  # המיקום נספר מ-1\n            count += 1\n    return count\n",
            "explain": "כשהשאלה סופרת מיקומים מ-1 ופייתון מ-0, ההמרה היא `i + 1`. שווה לבדוק על הדוגמה: באינדקס 2 (מיקום 3) יושב 27 = 3³.",
            "tests": [
                {"call": "count_cube_positions([1, 4, 27, 5, 125, 80, 16, 2, 400, 1000])", "expect": "4"},
                {"call": "count_cube_positions([8, 8])", "expect": "1"},
                {"call": "count_cube_positions([])", "expect": "0", "hidden": True},
                {"call": "count_cube_positions([0, 1, 9])", "expect": "0", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 16
        {
            "id": "lists-16", "num": "16", "title": "מספר הופעות",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `count_value(a, x)` שמחזירה כמה פעמים המספר `x` מופיע ברשימה `a`. ממש בעזרת לולאה (בלי `a.count`).\n\n"
                      "לדוגמה: `count_value([1, 2, 1, 1], 1)` מחזירה `3`.\n\n"
                      "**החזר:** מספר ההופעות.",
            "starter": "def count_value(a, x):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "מונה שמתחיל ב-0.",
                "עבור על הערכים ולכל ערך שווה ל-`x` הגדל את המונה.",
                "count = 0\nfor v in a:\n    if v == x:\n        count += 1\nreturn count",
            ],
            "solution": "def count_value(a, x):\n    count = 0\n    for v in a:\n        if v == x:\n            count += 1\n    return count\n",
            "explain": "תבנית מונה פשוטה. בפייתון יש קיצור מוכן: `a.count(x)` — טוב לדעת, אבל במבחן לפעמים מבקשים לממש בעצמך.",
            "tests": [
                {"call": "count_value([1, 2, 1, 1], 1)", "expect": "3"},
                {"call": "count_value([4, 5], 6)", "expect": "0"},
                {"call": "count_value([], 5)", "expect": "0", "hidden": True},
                {"call": "count_value([-2, -2, 2], -2)", "expect": "2", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 17
        {
            "id": "lists-17", "num": "17", "title": "עותק הפוך",
            "kind": "function", "difficulty": 1, "exam": False,
            "prompt": "כתוב פונקציה `reversed_copy(a)` שמחזירה **רשימה חדשה** `b` ובה איברי `a` בסדר הפוך. הרשימה `a` **לא** משתנה.\n\n"
                      "לדוגמה: עבור `a = [6, 4, 5, 3, 7, 1, 9, 8, 6, 3, 2]` מוחזר `[2, 3, 6, 8, 9, 1, 7, 3, 5, 4, 6]`.\n\n"
                      "נסה לממש עם לולאה ולא עם `[::-1]`.\n\n"
                      "**החזר:** הרשימה החדשה.",
            "starter": "def reversed_copy(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "צור `b = []` ומלא אותה מהסוף של `a` להתחלה.",
                "האינדקסים מהסוף: `range(len(a) - 1, -1, -1)`.",
                "b = []\nfor i in range(len(a) - 1, -1, -1):\n    b.append(a[i])\nreturn b",
            ],
            "solution": "def reversed_copy(a):\n    b = []\n    for i in range(len(a) - 1, -1, -1):\n        b.append(a[i])\n    return b\n",
            "explain": "בונים רשימה חדשה, ולכן `a` נשארת כמו שהייתה. שים לב: `a.reverse()` היה הופך את `a` עצמה — לא מה שביקשו. "
                       "`a[::-1]` מחזיר עותק הפוך ולא משנה את `a`.",
            "tests": [
                {"setup": "a = [6, 4, 5, 3, 7, 1, 9, 8, 6, 3, 2]", "call": "reversed_copy(a)", "expect": "[2, 3, 6, 8, 9, 1, 7, 3, 5, 4, 6]"},
                {"setup": "a = [1, 2, 3]", "call": "reversed_copy(a)", "check": "a", "expect": "[1, 2, 3]"},
                {"call": "reversed_copy([7])", "expect": "[7]", "hidden": True},
                {"call": "reversed_copy([])", "expect": "[]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 18
        {
            "id": "lists-18", "num": "18", "title": "ממוצע של שתי רשימות",
            "kind": "program", "difficulty": 2, "exam": False,
            "prompt": "כתוב תוכנית שקולטת שתי רשימות באותו אורך, `A` ו-`B`, ובונה רשימה חדשה `C` שבה כל איבר הוא הממוצע של האיברים המתאימים (באותו אינדקס) ב-`A` וב-`B`.\n\n"
                      "(בחוברת האורך 10 — כאן כל אורך.)\n\n"
                      "**קלט:** שתי שורות. בכל שורה מספרים שלמים מופרדים ברווחים — השורה הראשונה היא `A`, השנייה `B`. "
                      "קליטת שורה כזו: `list(map(int, input().split()))`.\n"
                      "**פלט:** איברי `C` בשורה אחת, מופרדים ברווחים.",
            "starter": "a = list(map(int, input().split()))\nb = list(map(int, input().split()))\n# כתוב כאן את הקוד\n",
            "hints": [
                "צריך לעבור על שתי הרשימות במקביל — לכן לולאה על אינדקסים.",
                "`c.append((a[i] + b[i]) / 2)` לכל `i` ב-`range(len(a))`.",
                "c = []\nfor i in range(len(a)):\n    c.append((a[i] + b[i]) / 2)\nprint(*c)",
            ],
            "solution": "a = list(map(int, input().split()))\nb = list(map(int, input().split()))\nc = []\nfor i in range(len(a)):\n    c.append((a[i] + b[i]) / 2)\nprint(*c)\n",
            "explain": "כשעובדים עם שתי רשימות במקביל, אותו אינדקס `i` משמש לשתיהן. הסוגריים ב-`(a[i] + b[i]) / 2` חשובים — בלעדיהם רק `b[i]` יחולק ב-2.",
            "tests": [
                {"stdin": "1 3 5 7 9\n3 2 7 3 2\n", "out": "2.0 2.5 6.0 5.0 5.5"},
                {"stdin": "4\n6\n", "out": "5.0"},
                {"stdin": "-1 0 10 1 2 3 4 5 6 7\n1 3 10 0 0 0 0 0 0 0\n", "out": "0 1.5 10 0.5 1 1.5 2 2.5 3 3.5", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 19
        {
            "id": "lists-19", "num": "19", "title": "רשימה סימטרית",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `is_symmetric(a)` שמחזירה `True` אם הרשימה **סימטרית** (נקראת אותו דבר מההתחלה ומהסוף, כמו פלינדרום) ו-`False` אחרת.\n\n"
                      "לדוגמה: `[1, 2, 3, 2, 1]` סימטרית, `[1, 2]` לא.\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def is_symmetric(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "משווים את הראשון לאחרון, את השני לזה שלפני האחרון, וכן הלאה.",
                "בן הזוג של `a[i]` הוא `a[len(a) - 1 - i]`. מספיק לבדוק עד האמצע. ברגע שמוצאים זוג שונה — `return False`.",
                "for i in range(len(a) // 2):\n    if a[i] != a[len(a) - 1 - i]:\n        return False\nreturn True",
            ],
            "solution": "def is_symmetric(a):\n    for i in range(len(a) // 2):\n        if a[i] != a[len(a) - 1 - i]:\n            return False\n    return True\n",
            "explain": "תבנית \"חפש דוגמה נגדית\": מחזירים `False` ברגע שמוצאים זוג לא תואם, ו-`True` רק אחרי שהלולאה עברה עד הסוף. "
                       "`return True` חייב להיות **מחוץ** ללולאה. קיצור: `return a == a[::-1]`.",
            "tests": [
                {"call": "is_symmetric([1, 2, 3, 2, 1])", "expect": "True"},
                {"call": "is_symmetric([1, 2])", "expect": "False"},
                {"call": "is_symmetric([7])", "expect": "True", "hidden": True},
                {"call": "is_symmetric([1, 2, 2, 1])", "expect": "True", "hidden": True},
                {"call": "is_symmetric([1, 2, 3, 1])", "expect": "False", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 20
        {
            "id": "lists-20", "num": "20", "title": "מונה ספרות",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `digit_counts(digits)` שמקבלת רשימה של ספרות (מספרים 0 עד 9) ומחזירה רשימה של 10 מונים: באינדקס `d` — כמה פעמים הופיעה הספרה `d`.\n\n"
                      "לדוגמה: עבור `[1, 2, 2, 9]` מוחזר `[0, 1, 2, 0, 0, 0, 0, 0, 0, 1]`.\n\n"
                      "(מהרשימה הזו קל להדפיס את הכמויות בסדר ממוין — לפי הספרה.)\n\n"
                      "**החזר:** רשימת 10 המונים.",
            "starter": "def digit_counts(digits):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "`counts = [0] * 10` — מונה לכל ספרה.",
                "הספרה עצמה היא האינדקס: `counts[d] += 1`.",
                "counts = [0] * 10\nfor d in digits:\n    counts[d] += 1\nreturn counts",
            ],
            "solution": "def digit_counts(digits):\n    counts = [0] * 10\n    for d in digits:\n        counts[d] += 1\n    return counts\n",
            "explain": "זה מערך המונים הקלאסי: הערך משמש כאינדקס. מעבר אחד על הנתונים מספיק כדי לספור את כל הספרות יחד.",
            "tests": [
                {"call": "digit_counts([1, 2, 2, 9])", "expect": "[0, 1, 2, 0, 0, 0, 0, 0, 0, 1]"},
                {"call": "digit_counts([])", "expect": "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"},
                {"call": "digit_counts([0, 0, 0, 5, 9, 9])", "expect": "[3, 0, 0, 0, 0, 1, 0, 0, 0, 2]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 21
        {
            "id": "lists-21", "num": "21", "title": "התפלגות ציונים",
            "kind": "program", "difficulty": 2, "exam": False,
            "prompt": "כתוב תוכנית שקולטת ציונים בטווח 0-100 ומדפיסה כמה תלמידים קיבלו כל ציון. השתמש במערך מונים.\n\n"
                      "(בחוברת 120 ציונים — כאן קודם נקלט N.)\n\n"
                      "**קלט:** שורה עם N, ואז N ציונים — אחד בכל שורה.\n"
                      "**פלט:** לכל ציון שהופיע, מהנמוך לגבוה — שורה עם הציון ומספר התלמידים, מופרדים ברווח.",
            "starter": "n = int(input())\n# כתוב כאן את הקוד\n",
            "hints": [
                "יש 101 ציונים אפשריים (0..100) — `counts = [0] * 101`.",
                "בלולאה של n פעמים: `g = int(input())` ואז `counts[g] += 1`.",
                "for g in range(101):\n    if counts[g] > 0:\n        print(g, counts[g])",
            ],
            "solution": "n = int(input())\ncounts = [0] * 101\nfor i in range(n):\n    g = int(input())\n    counts[g] += 1\nfor g in range(101):\n    if counts[g] > 0:\n        print(g, counts[g])\n",
            "explain": "גודל מערך המונים הוא 101 כי צריך אינדקסים 0 עד 100 כולל. בכלל לא צריך לשמור את הציונים עצמם — רק את המונים.",
            "tests": [
                {"stdin": "5\n90\n100\n90\n0\n75\n", "out": "0 1\n75 1\n90 2\n100 1"},
                {"stdin": "1\n55\n", "out": "55 1"},
                {"stdin": "4\n100\n100\n100\n100\n", "out": "100 4", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 22
        {
            "id": "lists-22", "num": "22", "title": "חיוביים ואורכם",
            "kind": "program", "difficulty": 1, "exam": False,
            "prompt": "כתוב תוכנית שקולטת רשימה של מספרים חיוביים ושליליים, בונה רשימה חדשה שבה רק המספרים החיוביים, ומדפיסה את הרשימה החדשה ואת האורך שלה.\n\n"
                      "**קלט:** שורה אחת של מספרים שלמים מופרדים ברווחים.\n"
                      "**פלט:** בשורה הראשונה — המספרים החיוביים מופרדים ברווחים (אם אין — שורה ריקה). בשורה השנייה — כמה יש.",
            "starter": "a = list(map(int, input().split()))\n# כתוב כאן את הקוד\n",
            "hints": [
                "סינון: `pos = []` ו-`append` לכל `x > 0`.",
                "`print(*pos)` ואז `print(len(pos))`.",
                "pos = []\nfor x in a:\n    if x > 0:\n        pos.append(x)\nprint(*pos)\nprint(len(pos))",
            ],
            "solution": "a = list(map(int, input().split()))\npos = []\nfor x in a:\n    if x > 0:\n        pos.append(x)\nprint(*pos)\nprint(len(pos))\n",
            "explain": "בפייתון אין צורך לדעת מראש את גודל הרשימה החדשה — היא גדלה עם `append`, ו-`len` נותן את הגודל בסוף. "
                       "(בשפות עם מערך בגודל קבוע היה צריך קודם לספור.)",
            "tests": [
                {"stdin": "3 -1 0 7 -5 2\n", "out": "3 7 2\n3"},
                {"stdin": "-1 -2\n", "out": "0"},
                {"stdin": "8\n", "out": "8\n1", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 23
        {
            "id": "lists-23", "num": "23", "title": "הזוג עם הממוצע הגבוה",
            "kind": "function", "difficulty": 2, "exam": False,
            "prompt": "כתוב פונקציה `best_pair(a)` שמקבלת רשימה של לפחות 2 מספרים שלמים ומוצאת את זוג האיברים **הסמוכים** (`a[i]`, `a[i + 1]`) שהממוצע שלהם הגבוה ביותר. "
                      "אם כמה זוגות שווים בממוצע — מחזירים את הזוג **הראשון**.\n\n"
                      "לדוגמה: עבור `[2, 8, 1, 5, 7, 3, 9, 4, 5, 1, 7, 3]` מוחזר `(9, 4)` (ממוצע 6.5).\n\n"
                      "**החזר:** `return a[i], a[i + 1]` של הזוג שנמצא.",
            "starter": "def best_pair(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "ממוצע של שניים גבוה יותר בדיוק כשהסכום שלהם גבוה יותר — אפשר להשוות סכומים.",
                "שמור את האינדקס של הזוג הטוב ביותר, התחל מ-0. לולאה `range(1, len(a) - 1)`; עדכן רק ב-`>` (לא `>=`) כדי לשמור את הראשון.",
                "best = 0\nfor i in range(1, len(a) - 1):\n    if a[i] + a[i + 1] > a[best] + a[best + 1]:\n        best = i\nreturn a[best], a[best + 1]",
            ],
            "solution": "def best_pair(a):\n    best = 0  # אינדקס תחילת הזוג הטוב ביותר\n    for i in range(1, len(a) - 1):\n        if a[i] + a[i + 1] > a[best] + a[best + 1]:\n            best = i\n    return a[best], a[best + 1]\n",
            "explain": "זה חיפוש מקסימום, אבל על זוגות: שומרים את **האינדקס** של הזוג הטוב, ומשווים עם `>` חזק כדי שבתיקו יישאר הראשון. "
                       "הלולאה עוצרת ב-`len(a) - 1` כי `a[i + 1]` חייב להיות קיים.",
            "tests": [
                {"call": "best_pair([2, 8, 1, 5, 7, 3, 9, 4, 5, 1, 7, 3])", "expect": "(9, 4)"},
                {"call": "best_pair([1, 5, 2, 4])", "expect": "(5, 2)"},
                {"call": "best_pair([3, 3, 1, 5])", "expect": "(3, 3)", "hidden": True},
                {"call": "best_pair([1, 2])", "expect": "(1, 2)", "hidden": True},
                {"call": "best_pair([1, 2, 3, 10])", "expect": "(3, 10)", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 24
        {
            "id": "lists-24", "num": "24", "title": "מערך מצטלב",
            "kind": "function", "difficulty": 3, "exam": True,
            "prompt": "רשימה נקראת **מצטלבת** אם:\n\n"
                      "- האיברים באינדקסים הזוגיים (0, 2, 4, ...) מסודרים בסדר **עולה ממש** (כל אחד גדול מהקודם, בלי שווים)\n"
                      "- האיברים באינדקסים האי-זוגיים (1, 3, 5, ...) מסודרים בסדר **יורד ממש**\n\n"
                      "לדוגמה, `[1, 9, 2, 8, 4, 7, 7, 4, 12]` מצטלבת: בזוגיים `1, 2, 4, 7, 12` ובאי-זוגיים `9, 8, 7, 4`.\n\n"
                      "כתוב פונקציה `is_zigzag_sorted(a)` שמחזירה `True` אם הרשימה מצטלבת ו-`False` אחרת. (בחוברת 51 איברים — כאן כל אורך.)\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def is_zigzag_sorted(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "כל איבר צריך להשוות לאיבר שנמצא **שני מקומות לפניו** (אותה זוגיות של אינדקס).",
                "לולאה על `i` מ-2 עד הסוף. אם `i` זוגי — צריך `a[i] > a[i - 2]`; אם אי-זוגי — `a[i] < a[i - 2]`. אם לא — `return False`.",
                "for i in range(2, len(a)):\n    if i % 2 == 0 and a[i] <= a[i - 2]:\n        return False\n    if i % 2 == 1 and a[i] >= a[i - 2]:\n        return False\nreturn True",
            ],
            "solution": "def is_zigzag_sorted(a):\n    for i in range(2, len(a)):\n        if i % 2 == 0 and a[i] <= a[i - 2]:\n            return False  # בזוגיים חייב לעלות\n        if i % 2 == 1 and a[i] >= a[i - 2]:\n            return False  # באי-זוגיים חייב לרדת\n    return True\n",
            "explain": "במקום לבנות שתי רשימות, משווים כל איבר לזה שנמצא שני מקומות לפניו — שהוא השכן שלו באותה \"תת-רשימה\". "
                       "\"ממש\" אומר שגם שוויון פוסל, ולכן התנאים הם `<=` ו-`>=`. אפשר גם עם חיתוך: `a[::2]` ו-`a[1::2]`.",
            "tests": [
                {"call": "is_zigzag_sorted([1, 9, 2, 8, 4, 7, 7, 4, 12])", "expect": "True"},
                {"call": "is_zigzag_sorted([1, 9, 2, 9, 4])", "expect": "False"},
                {"call": "is_zigzag_sorted([5])", "expect": "True", "hidden": True},
                {"call": "is_zigzag_sorted([1, 9, 1, 8])", "expect": "False", "hidden": True},
                {"call": "is_zigzag_sorted([3, 2])", "expect": "True", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 25a
        {
            "id": "lists-25a", "num": "25א", "title": "סכום שלושה",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `sum3(x, y, z)` שמקבלת שלושה מספרים שלמים ומחזירה את סכומם.\n\n"
                      "לדוגמה: `sum3(1, 2, 3)` מחזירה `6`.\n\n"
                      "**החזר:** הסכום.",
            "starter": "def sum3(x, y, z):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שורה אחת.",
                "return x + y + z",
            ],
            "solution": "def sum3(x, y, z):\n    return x + y + z\n",
            "explain": "פונקציית עזר קטנה. בסעיף ב' משתמשים בה — במבחן הרבה פעמים סעיף א' הוא כלי לסעיף הבא.",
            "tests": [
                {"call": "sum3(1, 2, 3)", "expect": "6"},
                {"call": "sum3(0, 0, 0)", "expect": "0"},
                {"call": "sum3(-5, 10, 2)", "expect": "7", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 25b
        {
            "id": "lists-25b", "num": "25ב", "title": "שלשות עולות",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "רשימה היא **\"רשימת שלשות עולות\"** אם כשמחלקים אותה לשלשות עוקבות (איברים 0-2, 3-5, 6-8, ...) — הסכום של כל שלשה **גדול** מהסכום של השלשה שלפניה.\n\n"
                      "כתוב פונקציה `is_rising_triples(a)` שמחזירה `True` אם הרשימה היא רשימת שלשות עולות ו-`False` אחרת. "
                      "אורך הרשימה הוא כפולה של 3. **השתמש בפונקציה `sum3` מסעיף א'** — העתק אותה לכאן.\n\n"
                      "לדוגמה: עבור `[1, 2, 3, 4, 5, 6, 7, 8, 9]` הסכומים 6, 15, 24 ולכן מוחזר `True`.\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def sum3(x, y, z):\n    return x + y + z\n\n\ndef is_rising_triples(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על תחילת כל שלשה: `range(0, len(a), 3)`. סכום השלשה: `sum3(a[i], a[i + 1], a[i + 2])`.",
                "שמור את סכום השלשה הקודמת והשווה. לשלשה הראשונה אין קודמת — התחל מהשנייה (`range(3, len(a), 3)`) והשווה ל-`i - 3`.",
                "for i in range(3, len(a), 3):\n    if sum3(a[i], a[i + 1], a[i + 2]) <= sum3(a[i - 3], a[i - 2], a[i - 1]):\n        return False\nreturn True",
            ],
            "solution": "def sum3(x, y, z):\n    return x + y + z\n\n\ndef is_rising_triples(a):\n    for i in range(3, len(a), 3):\n        current = sum3(a[i], a[i + 1], a[i + 2])\n        previous = sum3(a[i - 3], a[i - 2], a[i - 1])\n        if current <= previous:\n            return False\n    return True\n",
            "explain": "הלולאה קופצת ב-3 כך ש-`i` הוא תמיד תחילת שלשה, והשלשה הקודמת מתחילה ב-`i - 3`. "
                       "\"גדול\" פירושו גדול ממש — שוויון פוסל, ולכן `<=`. השימוש ב-`sum3` הוא מה שהשאלה דורשת (וחוסך קוד).",
            "tests": [
                {"call": "is_rising_triples([1, 2, 3, 4, 5, 6, 7, 8, 9])", "expect": "True"},
                {"call": "is_rising_triples([1, 2, 3, 3, 2, 1])", "expect": "False"},
                {"call": "is_rising_triples([5, 5, 5])", "expect": "True", "hidden": True},
                {"call": "is_rising_triples([9, 9, 9, 1, 1, 1])", "expect": "False", "hidden": True},
                {"call": "is_rising_triples([0, 0, 1, 0, 0, 2, 5, -3, 0])", "expect": "False", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 26
        {
            "id": "lists-26", "num": "26", "title": "זוגות עם סכום אי-זוגי",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `odd_sum_pairs(a)` שמקבלת רשימה של מספרים שלמים חיוביים ומדפיסה את כל זוגות האיברים **הסמוכים** שהסכום שלהם אי-זוגי. (בחוברת 55 איברים — כאן כל אורך.)\n\n"
                      "לדוגמה: עבור `[7, 4, 1, 1, 9, 2, 4, 3]` יודפס:\n```\n7 4\n4 1\n9 2\n4 3\n```\n"
                      "**פלט:** כל זוג בשורה נפרדת — שני המספרים מופרדים ברווח, לפי הסדר ברשימה. אם אין זוגות — לא מודפס כלום.",
            "starter": "def odd_sum_pairs(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "זוג סמוך: `a[i]` ו-`a[i + 1]`. הלולאה רצה עד `len(a) - 1`.",
                "סכום אי-זוגי: `(a[i] + a[i + 1]) % 2 == 1`.",
                "for i in range(len(a) - 1):\n    if (a[i] + a[i + 1]) % 2 == 1:\n        print(a[i], a[i + 1])",
            ],
            "solution": "def odd_sum_pairs(a):\n    for i in range(len(a) - 1):\n        if (a[i] + a[i + 1]) % 2 == 1:\n            print(a[i], a[i + 1])\n",
            "explain": "הזוגות חופפים: (7,4) ואחריו (4,1) — כל איבר הוא חלק משני זוגות, לכן הצעד הוא 1. "
                       "סכום של שני מספרים אי-זוגי בדיוק כשאחד זוגי והשני אי-זוגי.",
            "tests": [
                {"call": "odd_sum_pairs([7, 4, 1, 1, 9, 2, 4, 3])", "out": "7 4\n4 1\n9 2\n4 3"},
                {"call": "odd_sum_pairs([1, 2])", "out": "1 2"},
                {"call": "odd_sum_pairs([2, 4, 6])", "out": "", "hidden": True},
                {"call": "odd_sum_pairs([1, 1, 2, 2, 3])", "out": "1 2\n2 3", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 27
        {
            "id": "lists-27", "num": "27", "title": "זוגיות לפי מקום",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `parity_match(a)` שמחזירה `True` אם בכל האינדקסים הזוגיים יש מספרים זוגיים **ו**בכל האינדקסים האי-זוגיים יש מספרים אי-זוגיים, ו-`False` אחרת. (0 נחשב זוגי.)\n\n"
                      "לדוגמה: עבור `[4, 9, 2, 3, 8, 11, 12]` מוחזר `True`.\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def parity_match(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "הדרישה: הזוגיות של הערך שווה לזוגיות של האינדקס.",
                "`a[i] % 2` ו-`i % 2` צריכים להיות שווים. אם לא — `return False`.",
                "for i in range(len(a)):\n    if a[i] % 2 != i % 2:\n        return False\nreturn True",
            ],
            "solution": "def parity_match(a):\n    for i in range(len(a)):\n        if a[i] % 2 != i % 2:\n            return False\n    return True\n",
            "explain": "במקום שני מקרים נפרדים, שמים לב שהתנאי הוא בדיוק \"שארית הערך ב-2 שווה לשארית האינדקס ב-2\". "
                       "בפייתון `%` של מספר שלילי ב-2 נותן 0 או 1, כך שזה עובד גם לשליליים.",
            "tests": [
                {"call": "parity_match([4, 9, 2, 3, 8, 11, 12])", "expect": "True"},
                {"call": "parity_match([1, 2])", "expect": "False"},
                {"call": "parity_match([0])", "expect": "True", "hidden": True},
                {"call": "parity_match([2, 3, 4, 6])", "expect": "False", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 28a
        {
            "id": "lists-28a", "num": "28א", "title": "סכום ספרות",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `digit_sum(n)` שמקבלת מספר שלם חיובי ומחזירה את סכום ספרותיו. (בחוברת המספר תלת-ספרתי — הפתרון עם לולאה עובד לכל מספר.)\n\n"
                      "לדוגמה: `digit_sum(123)` מחזירה `6`.\n\n"
                      "**החזר:** סכום הספרות.",
            "starter": "def digit_sum(n):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "`n % 10` היא ספרת האחדות, `n // 10` מוריד אותה.",
                "s = 0\nwhile n > 0:\n    s += n % 10\n    n //= 10\nreturn s",
            ],
            "solution": "def digit_sum(n):\n    s = 0\n    while n > 0:\n        s += n % 10\n        n //= 10\n    return s\n",
            "explain": "פירוק מספר לספרות: לוקחים את האחדות עם `% 10` ומקצרים עם `// 10` עד שהמספר נהיה 0.",
            "tests": [
                {"call": "digit_sum(123)", "expect": "6"},
                {"call": "digit_sum(905)", "expect": "14"},
                {"call": "digit_sum(100)", "expect": "1", "hidden": True},
                {"call": "digit_sum(24)", "expect": "6", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 28b
        {
            "id": "lists-28b", "num": "28ב", "title": "מחלקים זוגיים",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `even_divisors(n)` שמקבלת מספר שלם חיובי ומחזירה **כמה** מחלקים זוגיים יש לו (כולל המספר עצמו אם הוא זוגי).\n\n"
                      "לדוגמה: ל-24 יש 6 מחלקים זוגיים — 2, 4, 6, 8, 12, 24 — ולכן `even_divisors(24)` מחזירה `6`.\n\n"
                      "**החזר:** מספר המחלקים הזוגיים.",
            "starter": "def even_divisors(n):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על כל המועמדים מ-1 עד n כולל.",
                "`d` מחלק את `n` אם `n % d == 0`. הוא זוגי אם `d % 2 == 0`.",
                "count = 0\nfor d in range(2, n + 1, 2):\n    if n % d == 0:\n        count += 1\nreturn count",
            ],
            "solution": "def even_divisors(n):\n    count = 0\n    for d in range(2, n + 1, 2):  # רק מועמדים זוגיים\n        if n % d == 0:\n            count += 1\n    return count\n",
            "explain": "`range(2, n + 1, 2)` עובר רק על מספרים זוגיים, כך שנשאר לבדוק רק חלוקה. ה-`n + 1` חשוב כדי לכלול את n עצמו.",
            "tests": [
                {"call": "even_divisors(24)", "expect": "6"},
                {"call": "even_divisors(7)", "expect": "0"},
                {"call": "even_divisors(12)", "expect": "4", "hidden": True},
                {"call": "even_divisors(2)", "expect": "1", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 28c
        {
            "id": "lists-28c", "num": "28ג", "title": "רשימה יפה",
            "kind": "function", "difficulty": 3, "exam": True,
            "prompt": "מספר שלם חיובי נקרא **יפה** אם מספר המחלקים הזוגיים שלו שווה לסכום ספרותיו. למשל 24 יפה: יש לו 6 מחלקים זוגיים וגם 2+4=6.\n\n"
                      "רשימה נקראת **יפה** אם יש בה **יותר** מספרים יפים ממספרים לא-יפים.\n\n"
                      "כתוב פונקציה `is_nice_list(a)` שמחזירה `True` אם הרשימה יפה ו-`False` אחרת. "
                      "**השתמש בפונקציות `digit_sum` ו-`even_divisors` מסעיפים א' ו-ב'** — העתק אותן לכאן. (בחוברת זו תוכנית עם 55 מספרים — כאן פונקציה שמקבלת רשימה.)\n\n"
                      "לדוגמה: עבור `[24, 32, 7]` מוחזר `True` (24 ו-32 יפים, 7 לא).\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def digit_sum(n):\n    # העתק מסעיף א'\n    pass\n\n\ndef even_divisors(n):\n    # העתק מסעיף ב'\n    pass\n\n\ndef is_nice_list(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "מספר `x` יפה אם `even_divisors(x) == digit_sum(x)`.",
                "ספור כמה יפים יש. הלא-יפים הם `len(a) - nice`. השווה עם `>` (שוויון אינו \"יותר\").",
                "nice = 0\nfor x in a:\n    if even_divisors(x) == digit_sum(x):\n        nice += 1\nreturn nice > len(a) - nice",
            ],
            "solution": "def digit_sum(n):\n    s = 0\n    while n > 0:\n        s += n % 10\n        n //= 10\n    return s\n\n\ndef even_divisors(n):\n    count = 0\n    for d in range(2, n + 1, 2):\n        if n % d == 0:\n            count += 1\n    return count\n\n\ndef is_nice_list(a):\n    nice = 0\n    for x in a:\n        if even_divisors(x) == digit_sum(x):\n            nice += 1\n    return nice > len(a) - nice\n",
            "explain": "הפתרון בנוי מאבני הבניין של הסעיפים הקודמים — כך בנויות הרבה שאלות מבחן. "
                       "`return nice > len(a) - nice` מחזיר ישירות ביטוי בוליאני, בלי `if`. שים לב שבתיקו התשובה `False`.",
            "tests": [
                {"call": "is_nice_list([24, 32, 7])", "expect": "True"},
                {"call": "is_nice_list([24, 7])", "expect": "False"},
                {"call": "is_nice_list([24])", "expect": "True", "hidden": True},
                {"call": "is_nice_list([24, 32, 7, 12])", "expect": "False", "hidden": True},
                {"call": "is_nice_list([7, 12, 30])", "expect": "False", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 29
        {
            "id": "lists-29", "num": "29", "title": "רשימת שלשות",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "רשימה היא **רשימת שלשות** אם היא מורכבת משלשות רצופות (איברים 0-2, 3-5, ...) שבכל אחת שלושה מספרים **זהים**.\n\n"
                      "כתוב פונקציה `is_triples_list(a)` שמחזירה `True` אם `a` היא רשימת שלשות ו-`False` אחרת. רשימה שאורכה אינו כפולה של 3 אינה רשימת שלשות.\n\n"
                      "לדוגמה: `[4, 4, 4, 2, 2, 2, 1, 1, 1, 4, 4, 4]` היא רשימת שלשות.\n\n"
                      "**החזר:** `True` או `False`.",
            "starter": "def is_triples_list(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "קודם בדוק `len(a) % 3 != 0` — אם כן, `False`.",
                "עבור על תחילות השלשות `range(0, len(a), 3)` ובדוק ש-`a[i] == a[i + 1] == a[i + 2]`.",
                "if len(a) % 3 != 0:\n    return False\nfor i in range(0, len(a), 3):\n    if a[i] != a[i + 1] or a[i] != a[i + 2]:\n        return False\nreturn True",
            ],
            "solution": "def is_triples_list(a):\n    if len(a) % 3 != 0:\n        return False\n    for i in range(0, len(a), 3):\n        if a[i] != a[i + 1] or a[i] != a[i + 2]:\n            return False\n    return True\n",
            "explain": "בדיקת האורך בהתחלה מבטיחה שלעולם לא נצא מהרשימה ב-`a[i + 2]`. "
                       "שים לב: השלשות לא חייבות להיות שונות זו מזו — 4,4,4 יכולה להופיע פעמיים.",
            "tests": [
                {"call": "is_triples_list([4, 4, 4, 2, 2, 2, 1, 1, 1, 4, 4, 4])", "expect": "True"},
                {"call": "is_triples_list([4, 4, 4, 2, 2])", "expect": "False"},
                {"call": "is_triples_list([1, 1, 2, 2, 2, 2])", "expect": "False", "hidden": True},
                {"call": "is_triples_list([7, 7, 7])", "expect": "True", "hidden": True},
                {"call": "is_triples_list([5, 5, 5, 5, 5, 6])", "expect": "False", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 30a
        {
            "id": "lists-30a", "num": "30א", "title": "הופעות ספרה",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `count_digit(n, d)` שמקבלת מספר שלם חיובי `n` וספרה `d` (0-9), ומחזירה כמה פעמים `d` מופיעה ב-`n`.\n\n"
                      "לדוגמה: `count_digit(1232, 2)` מחזירה `2`.\n\n"
                      "**החזר:** מספר ההופעות.",
            "starter": "def count_digit(n, d):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "פרק את המספר לספרות עם `% 10` ו-`// 10`, וספור את אלה ששוות ל-`d`.",
                "count = 0\nwhile n > 0:\n    if n % 10 == d:\n        count += 1\n    n //= 10\nreturn count",
            ],
            "solution": "def count_digit(n, d):\n    count = 0\n    while n > 0:\n        if n % 10 == d:\n            count += 1\n        n //= 10\n    return count\n",
            "explain": "אותה לולאת פירוק לספרות, עם מונה. (דרך אחרת: `str(n).count(str(d))` — אבל במבחן מצפים לחשבון.)",
            "tests": [
                {"call": "count_digit(1232, 2)", "expect": "2"},
                {"call": "count_digit(7070, 0)", "expect": "2"},
                {"call": "count_digit(5, 3)", "expect": "0", "hidden": True},
                {"call": "count_digit(999, 9)", "expect": "3", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 30b
        {
            "id": "lists-30b", "num": "30ב", "title": "החלפה לפי אינדקס",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `replace_by_index_count(a)` שמקבלת רשימה של מספרים שלמים חיוביים (באורך עד 10) ומחליפה כל איבר `a[i]` **במספר הפעמים שהספרה `i` מופיעה בו**. "
                      "**השתמש בפונקציה `count_digit` מסעיף א'** — העתק אותה לכאן.\n\n"
                      "הפונקציה **משנה את הרשימה עצמה**. (בחוברת יש גם קליטה של 10 מספרים — כאן רק הפונקציה.)\n\n"
                      "לדוגמה: `[7070, 12311, 2345]` הופכת ל-`[2, 3, 1]` — 0 מופיע פעמיים ב-7070, 1 מופיע 3 פעמים ב-12311, ו-2 מופיע פעם אחת ב-2345.",
            "starter": "def count_digit(n, d):\n    # העתק מסעיף א'\n    pass\n\n\ndef replace_by_index_count(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "האינדקס `i` הוא הספרה שמחפשים, והערך `a[i]` הוא המספר שבו מחפשים.",
                "לולאה על `range(len(a))` ובתוכה `a[i] = count_digit(a[i], i)`.",
                "for i in range(len(a)):\n    a[i] = count_digit(a[i], i)",
            ],
            "solution": "def count_digit(n, d):\n    count = 0\n    while n > 0:\n        if n % 10 == d:\n            count += 1\n        n //= 10\n    return count\n\n\ndef replace_by_index_count(a):\n    for i in range(len(a)):\n        a[i] = count_digit(a[i], i)\n",
            "explain": "כאן גם האינדקס וגם הערך משמשים בחישוב, ולכן לולאת `range(len(a))`. "
                       "מותר לדרוס את `a[i]` מיד, כי החישוב של כל מקום תלוי רק בערך המקורי שלו עצמו.",
            "tests": [
                {"setup": "a = [7070, 12311, 2345]", "call": "replace_by_index_count(a)", "check": "a", "expect": "[2, 3, 1]"},
                {"setup": "a = [5]", "call": "replace_by_index_count(a)", "check": "a", "expect": "[0]"},
                {"setup": "a = [10, 11, 22]", "call": "replace_by_index_count(a)", "check": "a", "expect": "[1, 2, 2]", "hidden": True},
                {"setup": "a = [1, 1, 1, 3333, 44, 5, 66, 7, 88, 9999]", "call": "replace_by_index_count(a)", "check": "a", "expect": "[0, 1, 0, 4, 2, 1, 2, 1, 2, 4]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 31
        {
            "id": "lists-31", "num": "31", "title": "זוגות שסכומם n",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `count_pairs_sum(a, n)` שמחזירה כמה זוגות של איברים **סמוכים** ברשימה `a` סכומם שווה ל-`n`.\n\n"
                      "לדוגמה: עבור `[9, 2, 3, 9, 7, 1, 4, 1]` ו-`n = 5` מוחזר `3` — הזוגות (2,3), (1,4), (4,1).\n\n"
                      "**החזר:** מספר הזוגות.",
            "starter": "def count_pairs_sum(a, n):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "זוגות סמוכים: `a[i]` ו-`a[i + 1]` עבור `i` ב-`range(len(a) - 1)`.",
                "count = 0\nfor i in range(len(a) - 1):\n    if a[i] + a[i + 1] == n:\n        count += 1\nreturn count",
            ],
            "solution": "def count_pairs_sum(a, n):\n    count = 0\n    for i in range(len(a) - 1):\n        if a[i] + a[i + 1] == n:\n            count += 1\n    return count\n",
            "explain": "מונה + השוואה לשכן. הגבול `len(a) - 1` מונע `IndexError`, והוא גם מטפל נכון ברשימה של איבר אחד (אין אף זוג).",
            "tests": [
                {"call": "count_pairs_sum([9, 2, 3, 9, 7, 1, 4, 1], 5)", "expect": "3"},
                {"call": "count_pairs_sum([5], 5)", "expect": "0"},
                {"call": "count_pairs_sum([1, 1, 1], 2)", "expect": "2", "hidden": True},
                {"call": "count_pairs_sum([2, 3, 2, 3], 5)", "expect": "3", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 32
        {
            "id": "lists-32", "num": "32", "title": "רשימת ממוצעים",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `average_lists(a, b)` שמקבלת שתי רשימות באותו אורך ומחזירה **רשימה חדשה** `c` שבה `c[i]` הוא הממוצע של `a[i]` ו-`b[i]`.\n\n"
                      "לדוגמה: עבור `a = [1, 3, 5, 7, 9]` ו-`b = [3, 2, 7, 3, 2]` מוחזר `[2.0, 2.5, 6.0, 5.0, 5.5]`.\n\n"
                      "**החזר:** הרשימה החדשה.",
            "starter": "def average_lists(a, b):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "לולאה על האינדקסים, אותו `i` לשתי הרשימות.",
                "c = []\nfor i in range(len(a)):\n    c.append((a[i] + b[i]) / 2)\nreturn c",
            ],
            "solution": "def average_lists(a, b):\n    c = []\n    for i in range(len(a)):\n        c.append((a[i] + b[i]) / 2)\n    return c\n",
            "explain": "זה אותו רעיון כמו בתרגיל 18, בניסוח של מבחן: פונקציה שמקבלת רשימות ומחזירה רשימה חדשה. החילוק `/` תמיד נותן `float`.",
            "tests": [
                {"call": "average_lists([1, 3, 5, 7, 9], [3, 2, 7, 3, 2])", "expect": "[2.0, 2.5, 6.0, 5.0, 5.5]"},
                {"call": "average_lists([4], [4])", "expect": "[4.0]"},
                {"call": "average_lists([-1, 0], [1, 3])", "expect": "[0.0, 1.5]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 33
        {
            "id": "lists-33", "num": "33", "title": "סכום עם השכן",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `pair_sums_circular(a)` שמחליפה כל איבר בסכום שלו ושל האיבר **הבא** אחריו. האיבר האחרון מוחלף בסכום שלו ושל האיבר **הראשון המקורי** (לפני השינוי).\n\n"
                      "הפונקציה **משנה את הרשימה עצמה**. (בחוברת זו תוכנית שקולטת 8 מספרים — כאן פונקציה לכל אורך.)\n\n"
                      "לדוגמה: `[1, 2, 3, 4, 5, 6, 7, 8]` הופכת ל-`[3, 5, 7, 9, 11, 13, 15, 9]`.",
            "starter": "def pair_sums_circular(a):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "הבעיה: עד שמגיעים לאחרון, `a[0]` כבר השתנה. שמור את `a[0]` במשתנה **לפני** הלולאה.",
                "לולאה עד `len(a) - 1`: `a[i] = a[i] + a[i + 1]` (ה-`a[i + 1]` עוד לא שונה). ואחריה טפל באחרון.",
                "first = a[0]\nfor i in range(len(a) - 1):\n    a[i] = a[i] + a[i + 1]\na[-1] = a[-1] + first",
            ],
            "solution": "def pair_sums_circular(a):\n    first = a[0]  # שומרים לפני שהוא משתנה\n    for i in range(len(a) - 1):\n        a[i] = a[i] + a[i + 1]\n    a[-1] = a[-1] + first\n",
            "explain": "כשמשנים רשימה במקום, צריך לשים לב מה כבר נדרס. מתקדמים משמאל לימין, ולכן `a[i + 1]` עדיין מקורי כשמשתמשים בו — "
                       "אבל `a[0]` כבר לא, ולכן שומרים אותו מראש. ברשימה של איבר אחד הוא מתחבר לעצמו.",
            "tests": [
                {"setup": "a = [1, 2, 3, 4, 5, 6, 7, 8]", "call": "pair_sums_circular(a)", "check": "a", "expect": "[3, 5, 7, 9, 11, 13, 15, 9]"},
                {"setup": "a = [1, 2]", "call": "pair_sums_circular(a)", "check": "a", "expect": "[3, 3]"},
                {"setup": "a = [5]", "call": "pair_sums_circular(a)", "check": "a", "expect": "[10]", "hidden": True},
                {"setup": "a = [10, -1, 4]", "call": "pair_sums_circular(a)", "check": "a", "expect": "[9, 3, 14]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 34
        {
            "id": "lists-34", "num": "34", "title": "מילים צועקות",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `count_shouting_words(sentence)` שמקבלת משפט (מילים מופרדות ברווחים) ומחזירה כמה מילים מכילות **יותר** אותיות גדולות מאשר קטנות.\n\n"
                      "לדוגמה: עבור `\"Rivka AVI MOTi VERed SHLomo\"` מוחזר `3` (AVI, MOTi, VERed; ב-SHLomo יש 3 מול 3 — לא יותר).\n\n"
                      "**החזר:** מספר המילים.",
            "starter": "def count_shouting_words(sentence):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "`sentence.split()` נותן רשימת מילים. כל מילה היא רצף של תווים.",
                "לכל מילה ספור אותיות גדולות (`ch.isupper()`) וקטנות (`ch.islower()`).",
                "for word in sentence.split():\n    upper = 0\n    lower = 0\n    for ch in word:\n        if ch.isupper():\n            upper += 1\n        elif ch.islower():\n            lower += 1\n    if upper > lower:\n        count += 1",
            ],
            "solution": "def count_shouting_words(sentence):\n    count = 0\n    for word in sentence.split():\n        upper = 0\n        lower = 0\n        for ch in word:\n            if ch.isupper():\n                upper += 1\n            elif ch.islower():\n                lower += 1\n        if upper > lower:\n            count += 1\n    return count\n",
            "explain": "`split()` הופך משפט לרשימה, ואז לולאה מקוננת: על המילים ובתוכה על התווים של כל מילה. "
                       "המונים של אותיות מתאפסים **בתוך** הלולאה החיצונית — לכל מילה מחדש.",
            "tests": [
                {"call": "count_shouting_words('Rivka AVI MOTi VERed SHLomo')", "expect": "3"},
                {"call": "count_shouting_words('hello World')", "expect": "0"},
                {"call": "count_shouting_words('ABC')", "expect": "1", "hidden": True},
                {"call": "count_shouting_words('aB Cd XY')", "expect": "1", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 35
        {
            "id": "lists-35", "num": "35", "title": "בין ההופעות של X",
            "kind": "function", "difficulty": 2, "exam": True,
            "prompt": "כתוב פונקציה `between_first_last(a, x)` שמחזירה רשימה חדשה עם כל האיברים שנמצאים **בין** ההופעה הראשונה של `x` להופעה האחרונה שלו (לא כולל את שתי ההופעות האלה). "
                      "מובטח ש-`x` מופיע ברשימה לפחות פעמיים. (בחוברת זו תוכנית שקולטת 20 מספרים ו-X — כאן פונקציה.)\n\n"
                      "לדוגמה: עבור `[10, 3, 5, 7, 3, 5, 7, 9, 4, 2, 4, 3, 5, 7, 9, 0, 7, 6, 11, 1]` ו-`x = 3` מוחזר `[5, 7, 3, 5, 7, 9, 4, 2, 4]`.\n\n"
                      "**החזר:** הרשימה החדשה.",
            "starter": "def between_first_last(a, x):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "צריך שני אינדקסים: של ההופעה הראשונה ושל האחרונה.",
                "הראשונה: `a.index(x)` או לולאה מההתחלה. האחרונה: לולאה מהסוף אחורה. ואז חיתוך.",
                "first = a.index(x)\nlast = first\nfor i in range(len(a)):\n    if a[i] == x:\n        last = i\nreturn a[first + 1:last]",
            ],
            "solution": "def between_first_last(a, x):\n    first = a.index(x)\n    last = first\n    for i in range(len(a)):\n        if a[i] == x:\n            last = i  # בסוף הלולאה זו ההופעה האחרונה\n    return a[first + 1:last]\n",
            "explain": "`a.index(x)` נותן את ההופעה הראשונה. לאחרונה — לולאה שמעדכנת בכל הופעה, כך שבסוף נשאר האינדקס האחרון. "
                       "החיתוך `a[first + 1:last]` לא כולל את שני הקצוות: `+1` מדלג על הראשונה, ו-`last` עצמו לא נכלל.",
            "tests": [
                {"call": "between_first_last([10, 3, 5, 7, 3, 5, 7, 9, 4, 2, 4, 3, 5, 7, 9, 0, 7, 6, 11, 1], 3)", "expect": "[5, 7, 3, 5, 7, 9, 4, 2, 4]"},
                {"call": "between_first_last([1, 2, 1], 1)", "expect": "[2]"},
                {"call": "between_first_last([4, 4], 4)", "expect": "[]", "hidden": True},
                {"call": "between_first_last([7, 1, 2, 7, 3, 7, 8], 7)", "expect": "[1, 2, 7, 3]", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 36
        {
            "id": "lists-36", "num": "36", "title": "העברה לסוף",
            "kind": "program", "difficulty": 2, "exam": True,
            "prompt": "בתוכנית מוגדרת הרשימה:\n```\narr = [4, 4, 8, 13, 12, 45, 6, 4, 7, 8, 5, 4, 3]\n```\n"
                      "התוכנית קולטת מספר `x` ומעבירה את **כל** ההופעות שלו לסוף הרשימה. שאר האיברים נשארים באותו סדר יחסי.\n\n"
                      "לדוגמה: עבור `4` יודפס `8 13 12 45 6 7 8 5 3 4 4 4 4`.\n\n"
                      "**קלט:** מספר שלם אחד.\n"
                      "**פלט:** הרשימה החדשה בשורה אחת מופרדת ברווחים. אם `x` לא ברשימה — הדפס `Not found`.",
            "starter": "arr = [4, 4, 8, 13, 12, 45, 6, 4, 7, 8, 5, 4, 3]\nx = int(input())\n# כתוב כאן את הקוד\n",
            "hints": [
                "בדוק קודם אם `x in arr`.",
                "בנה רשימה חדשה: קודם כל האיברים ששונים מ-`x`, ואחר כך הוסף את `x` כמספר הפעמים שהוא הופיע.",
                "result = []\nfor v in arr:\n    if v != x:\n        result.append(v)\nwhile len(result) < len(arr):\n    result.append(x)\nprint(*result)",
            ],
            "solution": "arr = [4, 4, 8, 13, 12, 45, 6, 4, 7, 8, 5, 4, 3]\nx = int(input())\nif x not in arr:\n    print('Not found')\nelse:\n    result = []\n    for v in arr:\n        if v != x:\n            result.append(v)\n    # משלימים את מה שחסר בהופעות של x\n    while len(result) < len(arr):\n        result.append(x)\n    print(*result)\n",
            "explain": "במקום להזיז איברים בתוך הרשימה (מסובך), בונים רשימה חדשה: קודם כל מה ששונה מ-x, ואז ממלאים ב-x עד האורך המקורי. "
                       "`x in arr` הוא הדרך הפשוטה לבדוק קיום.",
            "tests": [
                {"stdin": "4\n", "out": "8 13 12 45 6 7 8 5 3 4 4 4 4"},
                {"stdin": "99\n", "out": "Not found"},
                {"stdin": "45\n", "out": "4 4 8 13 12 6 4 7 8 5 4 3 45", "hidden": True},
                {"stdin": "8\n", "out": "4 4 13 12 45 6 4 7 5 4 3 8 8", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 37
        {
            "id": "lists-37", "num": "37", "title": "מחיקת רצפים",
            "kind": "function", "difficulty": 3, "exam": True,
            "prompt": "כתוב פונקציה `remove_runs(s)` שמקבלת מחרוזת ומחזירה מחרוזת חדשה שבה נמחקו כל **הרצפים** (באורך 2 ומעלה) של תווים זהים. תווים שמופיעים לבד נשארים.\n\n"
                      "המחיקה נעשית במעבר אחד: אם אחרי המחיקה נוצרים תווים זהים צמודים — הם נשארים.\n\n"
                      "לדוגמה: עבור `\"xxxabbbcdddcxxxyyz\"` מוחזר `\"accz\"`.\n\n"
                      "**החזר:** המחרוזת החדשה.",
            "starter": "def remove_runs(s):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על המחרוזת בקבוצות: לכל מקום `i`, מצא איפה נגמר הרצף של התו `s[i]`.",
                "עם `while`: `j = i`, וכל עוד `j < len(s)` ו-`s[j] == s[i]` — `j += 1`. אורך הרצף הוא `j - i`. אם הוא 1 — הוסף את התו לתוצאה. ואז `i = j`.",
                "result = ''\ni = 0\nwhile i < len(s):\n    j = i\n    while j < len(s) and s[j] == s[i]:\n        j += 1\n    if j - i == 1:\n        result += s[i]\n    i = j\nreturn result",
            ],
            "solution": "def remove_runs(s):\n    result = ''\n    i = 0\n    while i < len(s):\n        j = i\n        while j < len(s) and s[j] == s[i]:\n            j += 1\n        # s[i:j] הוא רצף של אותו תו\n        if j - i == 1:\n            result += s[i]\n        i = j\n    return result\n",
            "explain": "הרעיון: לחלק את המחרוזת לרצפים של תו זהה. `j` רץ קדימה עד שהתו משתנה, ואז `i = j` קופץ לרצף הבא. "
                       "מחרוזת אי אפשר לשנות במקום — בונים חדשה עם `+=`. שים לב לסדר בתנאי: `j < len(s)` נבדק לפני `s[j]` כדי לא לצאת מהמחרוזת.",
            "tests": [
                {"call": "remove_runs('xxxabbbcdddcxxxyyz')", "expect": "'accz'"},
                {"call": "remove_runs('abc')", "expect": "'abc'"},
                {"call": "remove_runs('aabb')", "expect": "''", "hidden": True},
                {"call": "remove_runs('abbbc')", "expect": "'ac'", "hidden": True},
                {"call": "remove_runs('a')", "expect": "'a'", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 38
        {
            "id": "lists-38", "num": "38", "title": "ספירת a, b, c",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `abc(s)` שמקבלת מחרוזת וסופרת כמה פעמים מופיע בה כל אחד מהתווים `a`, `b`, `c`.\n\n"
                      "לדוגמה: עבור `\"ayccybaxyc\"` מוחזר `(2, 1, 3)`.\n\n"
                      "תוכנית ראשית שקוראת ל-`abc` ומדפיסה `a 2 b 1 c 3` היא רשות — לניסוי בלבד (שים אותה תחת `if __name__ == \"__main__\":`).\n\n"
                      "**החזר:** `return count_a, count_b, count_c`.",
            "starter": "def abc(s):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שלושה מונים, לולאה אחת על התווים.",
                "for ch in s:\n    if ch == 'a':\n        ca += 1\n    elif ch == 'b':\n        cb += 1\n    elif ch == 'c':\n        cc += 1",
            ],
            "solution": "def abc(s):\n    ca = 0\n    cb = 0\n    cc = 0\n    for ch in s:\n        if ch == 'a':\n            ca += 1\n        elif ch == 'b':\n            cb += 1\n        elif ch == 'c':\n            cc += 1\n    return ca, cb, cc\n\n\nif __name__ == \"__main__\":\n    a, b, c = abc('ayccybaxyc')\n    print('a', a, 'b', b, 'c', c)\n",
            "explain": "מחרוזת היא רצף, ולכן `for ch in s` עובר על התווים. פונקציה בפייתון יכולה להחזיר כמה ערכים, ואת התוצאה \"פותחים\" כך: `a, b, c = abc(s)`. "
                       "אפשר גם `s.count('a')`.",
            "tests": [
                {"call": "abc('ayccybaxyc')", "expect": "(2, 1, 3)"},
                {"call": "abc('xyz')", "expect": "(0, 0, 0)"},
                {"call": "abc('')", "expect": "(0, 0, 0)", "hidden": True},
                {"call": "abc('cab')", "expect": "(1, 1, 1)", "hidden": True},
                {"call": "abc('ABCabc')", "expect": "(1, 1, 1)", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 39
        {
            "id": "lists-39", "num": "39", "title": "פיצול לזוגיים ואי-זוגיים",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `split_even_odd(arr)` שמקבלת רשימת מספרים שלמים ובונה שתי רשימות חדשות: `even` עם המספרים הזוגיים ו-`odd` עם האי-זוגיים, באותו סדר כמו ב-`arr`.\n\n"
                      "לדוגמה: עבור `[56, 10, 9, 23, 65, 45, 78, 44, 12, 2]` מוחזר `([56, 10, 78, 44, 12, 2], [9, 23, 65, 45])`.\n\n"
                      "(בחוברת יש גם קליטה של 10 מספרים והדפסה — כאן רק הפונקציה.)\n\n"
                      "**החזר:** `return even, odd`.",
            "starter": "def split_even_odd(arr):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "שתי רשימות ריקות, לולאה אחת.",
                "even = []\nodd = []\nfor x in arr:\n    if x % 2 == 0:\n        even.append(x)\n    else:\n        odd.append(x)",
            ],
            "solution": "def split_even_odd(arr):\n    even = []\n    odd = []\n    for x in arr:\n        if x % 2 == 0:\n            even.append(x)\n        else:\n            odd.append(x)\n    return even, odd\n",
            "explain": "כל איבר הולך בדיוק לאחת משתי הרשימות, ולכן `if/else`. `len(even)` ו-`len(odd)` נותנים כמה יש בכל אחת.",
            "tests": [
                {"call": "split_even_odd([56, 10, 9, 23, 65, 45, 78, 44, 12, 2])", "expect": "([56, 10, 78, 44, 12, 2], [9, 23, 65, 45])"},
                {"call": "split_even_odd([])", "expect": "([], [])"},
                {"call": "split_even_odd([-3, 0])", "expect": "([0], [-3])", "hidden": True},
                {"call": "split_even_odd([1, 3])", "expect": "([], [1, 3])", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 40
        {
            "id": "lists-40", "num": "40", "title": "מילים שמתחילות באות",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `print_words(line, letter)` שמקבלת מחרוזת של מילים מופרדות ברווחים ואות אחת, ומדפיסה כל מילה שמתחילה באות הזו (בדיוק — אותיות גדולות וקטנות שונות זו מזו).\n\n"
                      "לדוגמה: עבור `\"cat Dragon horse tiger dog dolphin mouse dinosaur\"` והאות `'d'` יודפס:\n```\ndog\ndolphin\ndinosaur\n```\n"
                      "**פלט:** כל מילה מתאימה בשורה נפרדת, לפי הסדר.",
            "starter": "def print_words(line, letter):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "`line.split()` נותן רשימת מילים.",
                "המילה מתאימה אם `word[0] == letter` (או `word.startswith(letter)`).",
                "for word in line.split():\n    if word[0] == letter:\n        print(word)",
            ],
            "solution": "def print_words(line, letter):\n    for word in line.split():\n        if word[0] == letter:\n            print(word)\n",
            "explain": "`split()` מפרק את המחרוזת למילים, ו-`word[0]` הוא התו הראשון של כל מילה. ההשוואה רגישה לגודל אות, ולכן `Dragon` לא מודפסת עבור `'d'`.",
            "tests": [
                {"call": "print_words('cat Dragon horse tiger dog dolphin mouse dinosaur', 'd')", "out": "dog\ndolphin\ndinosaur"},
                {"call": "print_words('apple banana', 'z')", "out": ""},
                {"call": "print_words('Dog dig Door', 'D')", "out": "Dog\nDoor", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 41
        {
            "id": "lists-41", "num": "41", "title": "משולש ממחרוזת",
            "kind": "function", "difficulty": 1, "exam": True,
            "prompt": "כתוב פונקציה `triangle(string)` שמדפיסה את המחרוזת בצורת משולש: בשורה הראשונה המחרוזת המלאה, בשנייה בלי התו הראשון, בשלישית בלי שני התווים הראשונים, וכן הלאה — עד שבשורה האחרונה נשאר רק התו האחרון.\n\n"
                      "לדוגמה: עבור `\"house\"` יודפס:\n```\nhouse\nouse\nuse\nse\ne\n```\n"
                      "**פלט:** השורות בלבד.",
            "starter": "def triangle(string):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "חיתוך `string[i:]` נותן את המחרוזת בלי `i` התווים הראשונים.",
                "for i in range(len(string)):\n    print(string[i:])",
            ],
            "solution": "def triangle(string):\n    for i in range(len(string)):\n        print(string[i:])\n",
            "explain": "חיתוך עובד על מחרוזות בדיוק כמו על רשימות. `string[i:]` מתחיל מאינדקס `i` ועד הסוף, ו-`i` רץ מ-0 עד האורך פחות 1.",
            "tests": [
                {"call": "triangle('house')", "out": "house\nouse\nuse\nse\ne"},
                {"call": "triangle('a')", "out": "a"},
                {"call": "triangle('ab')", "out": "ab\nb", "hidden": True},
            ],
        },
        # ---------------------------------------------------------------- 42
        {
            "id": "lists-42", "num": "42", "title": "מיקומי X",
            "kind": "program", "difficulty": 2, "exam": True,
            "prompt": "כתוב תוכנית שקולטת רשימה של מספרים שלמים ומספר `x`, ובודקת אם `x` נמצא ברשימה. אם כן — בונה רשימה חדשה עם כל **האינדקסים** שבהם הוא נמצא (מ-0), ומדפיסה אותם. (בחוברת 10 מספרים — כאן כל כמות.)\n\n"
                      "לדוגמה: עבור הרשימה `2 1 8 6 4 8 8 16 24 8` ו-`x = 8` יודפס:\n```\nIn the array the positions of the element 8 are 2 5 6 9\n```\n"
                      "**קלט:** בשורה הראשונה המספרים מופרדים ברווחים, בשורה השנייה `x`.\n"
                      "**פלט:** `In the array the positions of the element <x> are` ואחריו האינדקסים מופרדים ברווחים — בשורה אחת. אם `x` לא ברשימה — הדפס `Not found`.",
            "starter": "a = list(map(int, input().split()))\nx = int(input())\n# כתוב כאן את הקוד\n",
            "hints": [
                "צריך את האינדקסים — לולאה על `range(len(a))` או `enumerate`.",
                "בנה `positions = []` עם `append(i)` לכל `a[i] == x`. אם בסוף היא ריקה — `Not found`.",
                "print('In the array the positions of the element', x, 'are', *positions)",
            ],
            "solution": "a = list(map(int, input().split()))\nx = int(input())\npositions = []\nfor i, v in enumerate(a):\n    if v == x:\n        positions.append(i)\nif len(positions) == 0:\n    print('Not found')\nelse:\n    print('In the array the positions of the element', x, 'are', *positions)\n",
            "explain": "`enumerate(a)` נותן גם אינדקס וגם ערך. בונים רשימת מיקומים, ואם היא ריקה — המספר לא נמצא. "
                       "`print` עם כמה ארגומנטים ו-`*positions` מדפיס הכול בשורה אחת עם רווחים.",
            "tests": [
                {"stdin": "2 1 8 6 4 8 8 16 24 8\n8\n", "out": "In the array the positions of the element 8 are 2 5 6 9"},
                {"stdin": "1 2 3\n7\n", "out": "Not found"},
                {"stdin": "5\n5\n", "out": "In the array the positions of the element 5 are 0", "hidden": True},
                {"stdin": "-1 0 -1\n-1\n", "out": "In the array the positions of the element -1 are 0 2", "hidden": True},
            ],
        },
    ],
}
