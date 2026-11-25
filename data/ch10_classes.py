# Reference classes, reused in the part-2 starters/solutions (the student's code must contain the class too).

HOTEL = '''class Hotel:
    def __init__(self, name="NA", city="NA", rooms=0, free=0):
        self.name = name
        self.city = city
        self.rooms = rooms
        self.free = free

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_rooms(self):
        return self.rooms

    def get_free(self):
        return self.free

    def set_free(self, free):
        self.free = free

    def set_data(self, name, city, rooms, free):
        self.name = name
        self.city = city
        self.rooms = rooms
        self.free = free

    def print_info(self):
        print(self.name, self.city, self.rooms - self.free, self.free)
'''

SHOP = '''class Shop:
    def __init__(self, name="NA", banana=0, apple=0, orange=0):
        self.name = name
        self.banana = banana
        self.apple = apple
        self.orange = orange

    def get_name(self):
        return self.name

    def get_banana(self):
        return self.banana

    def get_apple(self):
        return self.apple

    def get_orange(self):
        return self.orange

    def set_data(self, name, banana, apple, orange):
        self.name = name
        self.banana = banana
        self.apple = apple
        self.orange = orange

    def print_info(self):
        print(self.name, self.banana, self.apple, self.orange)
'''

ITEM = '''class Item:
    def __init__(self, catalog=0, name="NA", price=0):
        self.catalog = catalog
        self.name = name
        self.price = price

    def get_catalog(self):
        return self.catalog

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_data(self, catalog, name, price):
        self.catalog = catalog
        self.name = name
        self.price = price

    def print_info(self):
        print(self.catalog, self.name, self.price)

    def cost(self, n):
        return n * self.price
'''

CHECK = '''class Check:
    def __init__(self, ch_number="UNKNOWN", bname="UNKNOWN", dep_number=0, amount=0):
        self.ch_number = ch_number
        self.bname = bname
        self.dep_number = dep_number
        self.amount = amount

    def get_ch_number(self):
        return self.ch_number

    def get_bname(self):
        return self.bname

    def get_dep_number(self):
        return self.dep_number

    def get_amount(self):
        return self.amount

    def set_data(self, ch_number, bname, dep_number, amount):
        self.ch_number = ch_number
        self.bname = bname
        self.dep_number = dep_number
        self.amount = amount

    def print_info(self):
        print(self.ch_number, self.bname, self.dep_number, self.amount)
'''

FILM = '''class Film:
    def __init__(self, name="NA", director="NA", copies=0):
        self.name = name
        self.director = director
        self.copies = copies

    def get_name(self):
        return self.name

    def get_director(self):
        return self.director

    def get_copies(self):
        return self.copies

    def set_data(self, name, director, copies):
        self.name = name
        self.director = director
        self.copies = copies

    def print_info(self):
        print(self.name, self.director, self.copies)

    def insert(self):
        self.copies += 1

    def check(self):
        return self.copies > 0

    def remove(self):
        self.copies -= 1
'''

TOY = '''class Toy:
    def __init__(self, code=0, group="NA", manufact="NA", year=0):
        self.code = code
        self.group = group
        self.manufact = manufact
        self.year = year

    def get_code(self):
        return self.code

    def get_group(self):
        return self.group

    def get_manufact(self):
        return self.manufact

    def get_year(self):
        return self.year

    def set_data(self, code, group, manufact, year):
        self.code = code
        self.group = group
        self.manufact = manufact
        self.year = year

    def print_info(self):
        print(self.code, self.group, self.manufact, self.year)
'''

CONV = ("**מוסכמה בפרק הזה:** שמות שיטות באותיות קטנות עם קו תחתון (`get_name()`, `set_data(...)`, `print_info()`), "
        "בדיוק כפי שמופיעים כאן — הבדיקות קוראות להן בשמות האלה.")

PASTE = ("**שים לב:** הבדיקות יוצרות אובייקטים מהמחלקה, ולכן הקוד שלך חייב להכיל אותה. "
         "בעורך כבר מופיעה מחלקה מוכנה מחלק 1 — אפשר להשאיר אותה או להדביק במקומה את המחלקה שכתבת. כתוב את הפונקציה מתחתיה.")


def _class_starter(name):
    return f"class {name}:\n    # כתוב כאן את המחלקה\n    pass\n"


CHAPTER = {
    "id": "classes",
    "title": "מחלקות ואובייקטים",
    "icon": "🏗️",
    "summary": "class, __init__, self, שיטות, ערכי ברירת מחדל, רשימות של אובייקטים, ירושה",
    "learn": [
        {"title": "מחלקה ואובייקט",
         "text": "**מחלקה** (`class`) היא תבנית שמתארת סוג של דבר — אילו נתונים יש לו ומה אפשר לעשות איתו. **אובייקט** הוא מופע אחד של המחלקה.\n\nיוצרים אובייקט ע\"י קריאה לשם המחלקה כמו לפונקציה: `h = Hotel(\"Hilton\", \"Eilat\", 100, 14)`.",
         "code": "class Dog:\n    def __init__(self, name):\n        self.name = name\n\nd1 = Dog(\"Rex\")\nd2 = Dog(\"Luna\")\nprint(d1.name, d2.name)"},
        {"title": "__init__ ו-self",
         "text": "`__init__` היא **הבנאי** — היא רצה אוטומטית כשיוצרים אובייקט, ותפקידה לשמור את הנתונים.\n\n`self` הוא האובייקט עצמו. `self.name = name` שומר את הפרמטר `name` כ**תכונה** (attribute) של האובייקט, כך ששאר השיטות יוכלו להשתמש בה.\n\n`self` הוא תמיד הפרמטר הראשון של כל שיטה, אבל לא מעבירים אותו בקריאה.",
         "code": "class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\np = Point(3, 4)\nprint(p.x, p.y)  # 3 4"},
        {"title": "ערכי ברירת מחדל במקום שני בנאים",
         "text": "ב-C++ כותבים בנאי עם פרמטרים ובנאי בלי פרמטרים. בפייתון יש **בנאי אחד** עם ערכי ברירת מחדל: מי שלא מעביר ערך — מקבל `\"NA\"` או `0`.",
         "code": "class Film:\n    def __init__(self, name=\"NA\", copies=0):\n        self.name = name\n        self.copies = copies\n\na = Film(\"Up\", 3)\nb = Film()\nprint(a.name, a.copies)  # Up 3\nprint(b.name, b.copies)  # NA 0"},
        {"title": "שיטות: get, set והדפסה",
         "text": "**שיטה** (method) היא פונקציה בתוך המחלקה. היא מקבלת `self` ויכולה לקרוא ולשנות את התכונות.\n\n- `get_...` מחזירה ערך של תכונה (`return`).\n- `set_...` משנה תכונה.\n- `print_info()` מדפיסה את הנתונים.\n\nקוראים לשיטה עם נקודה: `h.get_free()`.",
         "code": "class Counter:\n    def __init__(self, value=0):\n        self.value = value\n\n    def get_value(self):\n        return self.value\n\n    def add(self):\n        self.value += 1\n\nc = Counter()\nc.add()\nc.add()\nprint(c.get_value())  # 2"},
        {"title": "רשימה של אובייקטים",
         "text": "במקום \"מערך של 30 אובייקטים\" בפייתון משתמשים ב**רשימה** של אובייקטים. עוברים עליה בלולאה וקוראים לשיטות של כל אובייקט.",
         "code": "class Toy:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\ntoys = [Toy(\"car\", 3), Toy(\"lego\", 6), Toy(\"ball\", 3)]\nfor t in toys:\n    if t.age == 3:\n        print(t.name)"},
        {"title": "__str__ — איך האובייקט מודפס",
         "text": "אם מגדירים שיטה `__str__` שמחזירה מחרוזת, אז `print(obj)` ידפיס אותה. (בפרק הזה התרגילים משתמשים ב-`print_info()`, אבל כדאי להכיר.)",
         "code": "class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __str__(self):\n        return f\"({self.x}, {self.y})\"\n\nprint(Point(1, 2))  # (1, 2)"},
        {"title": "ירושה ו-super()",
         "text": "`class NewItem(Item):` — המחלקה `NewItem` **יורשת** מ-`Item`: יש לה את כל התכונות והשיטות של `Item`, ואפשר להוסיף חדשות או **לדרוס** (override) שיטה קיימת ע\"י כתיבה מחדש באותו שם.\n\nבבנאי של המחלקה היורשת קוראים לבנאי של ההורה עם `super().__init__(...)` כדי לאתחל את התכונות שלו.",
         "code": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def sound(self):\n        return \"...\"\n\nclass Cat(Animal):\n    def __init__(self, name, lives=9):\n        super().__init__(name)\n        self.lives = lives\n\n    def sound(self):\n        return \"Meow\"\n\nc = Cat(\"Tom\")\nprint(c.name, c.lives, c.sound())  # Tom 9 Meow"},
    ],
    "pitfalls": [
        "שכחת `self` כפרמטר ראשון בשיטה (`def get_name():`) — מקבלים `TypeError` כשקוראים לה.",
        "כתיבת `name = name` במקום `self.name = name` בבנאי — הערך לא נשמר באובייקט.",
        "`get_...` צריכה **להחזיר** (`return`) ולא להדפיס. `print_info()` מדפיסה.",
        "קריאה לשיטה בלי סוגריים: `h.get_free` (בלי `()`) מחזיר את השיטה עצמה, לא את הערך.",
        "בירושה — שכחת `super().__init__(...)` בבנאי של המחלקה היורשת, ואז לתכונות של ההורה אין ערך.",
        "שם `__init__` עם **שני** קווים תחתונים מכל צד.",
    ],
    "exercises": [
        # ---------- Question 1: Hotel ----------
        {
            "id": "classes-01a",
            "num": "1 (חלק 1)",
            "title": "מחלקת מלון",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "הגדר מחלקה `Hotel` שמייצגת בית מלון, עם התכונות:\n- `name` — שם המלון (למשל `\"Hilton\"`)\n- `city` — העיר (למשל `\"Eilat\"`)\n- `rooms` — מספר החדרים הכולל (למשל `1000`)\n- `free` — מספר החדרים הפנויים (למשל `14`)\n\n**בנאי:** `Hotel(name, city, rooms, free)`. אם לא מעבירים ערכים — המחרוזות יהיו `\"NA\"` והמספרים `0` (בנאי אחד עם ערכי ברירת מחדל).\n\n**שיטות:**\n- `get_name()`, `get_city()`, `get_rooms()`, `get_free()` — מחזירות את ערך התכונה.\n- `set_free(n)` — מעדכנת את מספר החדרים הפנויים.\n- `set_data(name, city, rooms, free)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת, מופרדים ברווח: שם, עיר, **מספר החדרים התפוסים** (`rooms - free`) ומספר החדרים הפנויים. למשל: `Hilton Eilat 986 14`.\n\n" + CONV,
            "starter": _class_starter("Hotel"),
            "hints": [
                "התחל מ-`def __init__(self, name=\"NA\", city=\"NA\", rooms=0, free=0):` ושמור כל פרמטר ב-`self`.",
                "כל `get_...` היא שורה אחת: `return self.xxx`. ב-`set_data` מעדכנים את ארבע התכונות.",
                "def print_info(self):\n    print(self.name, self.city, self.rooms - self.free, self.free)",
            ],
            "solution": HOTEL,
            "explain": "הבנאי שומר את הנתונים בתכונות של האובייקט (`self.xxx`), וערכי ברירת המחדל מחליפים את \"הבנאי בלי פרמטרים\". מספר החדרים התפוסים לא נשמר כתכונה — מחשבים אותו בזמן ההדפסה מ-`rooms - free`.",
            "tests": [
                {"setup": "h = Hotel('Hilton', 'Eilat', 1000, 14)", "call": "h.get_free()", "expect": "14"},
                {"setup": "h = Hotel('Hilton', 'Eilat', 1000, 14)", "call": "h.print_info()", "out": "Hilton Eilat 986 14"},
                {"setup": "h = Hotel()", "call": "(h.get_name(), h.get_city(), h.get_rooms(), h.get_free())", "expect": "('NA', 'NA', 0, 0)", "hidden": True},
                {"setup": "h = Hotel('Dan', 'Haifa', 50, 10)\nh.set_free(3)", "call": "h.get_free()", "expect": "3", "hidden": True},
                {"setup": "h = Hotel()\nh.set_data('Isrotel', 'Tel Aviv', 200, 20)", "call": "h.print_info()", "out": "Isrotel Tel Aviv 180 20", "hidden": True},
                {"setup": "h = Hotel('Dan', 'Haifa', 50, 10)", "call": "(h.get_name(), h.get_city(), h.get_rooms())", "expect": "('Dan', 'Haifa', 50)", "hidden": True},
            ],
        },
        {
            "id": "classes-01b",
            "num": "1 (חלק 2)",
            "title": "מלונות פנויים בעיר",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "כתוב פונקציה `free_hotels(hotels, city)` שמקבלת רשימה של אובייקטים מסוג `Hotel` (מחלק 1) ושם של עיר, ומחזירה **רשימה של שמות** כל המלונות שנמצאים בעיר הזו ויש בהם לפחות חדר פנוי אחד — לפי הסדר ברשימה.\n\nאם אין כאלה — מחזירים רשימה ריקה `[]`.\n\nבתרגיל המקורי התוכנית הראשית קולטת את המלונות מהמשתמש; כאן מספיק לכתוב את הפונקציה (תוכנית ראשית אפשר להוסיף תחת `if __name__ == \"__main__\":`).\n\n" + PASTE + "\n\n**החזר:** רשימת שמות.",
            "starter": HOTEL + "\n\ndef free_hotels(hotels, city):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על הרשימה בלולאה `for h in hotels:` ובדוק שני תנאים לכל מלון.",
                "התנאים: `h.get_city() == city` וגם `h.get_free() > 0`. אם שניהם מתקיימים — הוסף את `h.get_name()` לרשימת התוצאה.",
                "result = []\nfor h in hotels:\n    if h.get_city() == city and h.get_free() > 0:\n        result.append(h.get_name())\nreturn result",
            ],
            "solution": HOTEL + "\n\ndef free_hotels(hotels, city):\n    result = []\n    for h in hotels:\n        if h.get_city() == city and h.get_free() > 0:\n            result.append(h.get_name())\n    return result\n",
            "explain": "רשימה של אובייקטים עובדת כמו כל רשימה: הלולאה נותנת אובייקט אחד בכל פעם, ועליו קוראים לשיטות `get_...`. זה \"סינון\" רגיל — אוספים לרשימה חדשה רק את מה שעונה על התנאי.",
            "tests": [
                {"setup": "hs = [Hotel('Hilton', 'Eilat', 100, 14), Hotel('Dan', 'Haifa', 50, 5), Hotel('Isrotel', 'Eilat', 80, 0), Hotel('Royal', 'Eilat', 30, 2)]", "call": "free_hotels(hs, 'Eilat')", "expect": "['Hilton', 'Royal']"},
                {"setup": "hs = [Hotel('Hilton', 'Eilat', 100, 14), Hotel('Dan', 'Haifa', 50, 5)]", "call": "free_hotels(hs, 'Haifa')", "expect": "['Dan']"},
                {"setup": "hs = [Hotel('Hilton', 'Eilat', 100, 14)]", "call": "free_hotels(hs, 'Jerusalem')", "expect": "[]", "hidden": True},
                {"setup": "hs = [Hotel('A', 'Eilat', 10, 0), Hotel('B', 'Eilat', 10, 0)]", "call": "free_hotels(hs, 'Eilat')", "expect": "[]", "hidden": True},
                {"call": "free_hotels([], 'Eilat')", "expect": "[]", "hidden": True},
            ],
        },
        # ---------- Question 2: Shop ----------
        {
            "id": "classes-02a",
            "num": "2 (חלק 1)",
            "title": "מחלקת חנות",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "הגדר מחלקה `Shop` שמייצגת חנות ואת מחירי הפירות בה (לק\"ג), עם התכונות:\n- `name` — שם החנות (למשל `\"Mega\"`)\n- `banana` — מחיר ק\"ג בננות (למשל `5.9`)\n- `apple` — מחיר ק\"ג תפוחים (למשל `3.8`)\n- `orange` — מחיר ק\"ג תפוזים (למשל `2.5`)\n\n**בנאי:** `Shop(name, banana, apple, orange)`, וברירת מחדל: שם `\"NA\"` ומחירים `0`.\n\n**שיטות:**\n- `get_name()`, `get_banana()`, `get_apple()`, `get_orange()` — מחזירות את הערך.\n- `set_data(name, banana, apple, orange)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת: שם ושלושת המחירים, מופרדים ברווח. למשל: `Mega 5.9 3.8 2.5`.\n\n" + CONV,
            "starter": _class_starter("Shop"),
            "hints": [
                "`def __init__(self, name=\"NA\", banana=0, apple=0, orange=0):` ושמירת כל פרמטר ב-`self`.",
                "ארבע שיטות `get_...` שכל אחת מחזירה תכונה אחת, ו-`set_data` שמעדכנת את כולן.",
                "def print_info(self):\n    print(self.name, self.banana, self.apple, self.orange)",
            ],
            "solution": SHOP,
            "explain": "המבנה זהה לכל מחלקת נתונים: בנאי ששומר תכונות עם ערכי ברירת מחדל, שיטות `get` שמחזירות, `set_data` שמעדכנת ו-`print_info` שמדפיסה. מחירים הם מספרים עשרוניים (`float`) — פייתון לא דורש להצהיר על הטיפוס.",
            "tests": [
                {"setup": "s = Shop('Mega', 5.9, 3.8, 2.5)", "call": "s.get_banana()", "expect": "5.9"},
                {"setup": "s = Shop('Mega', 5.9, 3.8, 2.5)", "call": "s.print_info()", "out": "Mega 5.9 3.8 2.5"},
                {"setup": "s = Shop()", "call": "(s.get_name(), s.get_banana(), s.get_apple(), s.get_orange())", "expect": "('NA', 0, 0, 0)", "hidden": True},
                {"setup": "s = Shop()\ns.set_data('Rami', 6, 4.5, 3)", "call": "(s.get_name(), s.get_apple(), s.get_orange())", "expect": "('Rami', 4.5, 3)", "hidden": True},
                {"setup": "s = Shop()\ns.set_data('Rami', 6, 4.5, 3)", "call": "s.print_info()", "out": "Rami 6 4.5 3", "hidden": True},
            ],
        },
        {
            "id": "classes-02b",
            "num": "2 (חלק 2)",
            "title": "החנות הזולה ביותר",
            "kind": "function",
            "difficulty": 3,
            "exam": True,
            "prompt": "כתוב פונקציה `cheapest(shops, kg_banana, kg_apple, kg_orange)` שמקבלת רשימה של אובייקטים מסוג `Shop` (מחלק 1) ואת הכמויות (בק\"ג) של בננות, תפוחים ותפוזים שרוצים לקנות.\n\nלכל חנות מחשבים את עלות הסל: `kg_banana * banana + kg_apple * apple + kg_orange * orange`.\n\nהפונקציה **מדפיסה** בשורה אחת את שם החנות הזולה ביותר ואת עלות הסל בה, מופרדים ברווח. אם יש כמה חנויות זולות באותה מידה — את הראשונה ברשימה. אפשר להניח שהרשימה לא ריקה.\n\nלדוגמה, עבור חנות `Mega` (5.9, 3.8, 2.5) ו-`Rami` (6, 3, 2) עם 1 ק\"ג מכל פרי: ב-Mega העלות 12.2 וב-Rami 11, ולכן יודפס `Rami 11`.\n\n" + PASTE,
            "starter": SHOP + "\n\ndef cheapest(shops, kg_banana, kg_apple, kg_orange):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "זה חיפוש מינימום: שמור את החנות הטובה ביותר עד עכשיו ואת העלות שלה.",
                "התחל מהחנות הראשונה (`best = shops[0]`) ועבור על כל החנויות. אם העלות **קטנה ממש** מהמינימום — עדכן.",
                "best = shops[0]\nbest_cost = kg_banana * best.get_banana() + kg_apple * best.get_apple() + kg_orange * best.get_orange()\nfor s in shops:\n    c = ...  # אותו חישוב עבור s\n    if c < best_cost:\n        best = s\n        best_cost = c\nprint(best.get_name(), best_cost)",
            ],
            "solution": SHOP + "\n\ndef cheapest(shops, kg_banana, kg_apple, kg_orange):\n    best = None\n    best_cost = 0\n    for s in shops:\n        c = kg_banana * s.get_banana() + kg_apple * s.get_apple() + kg_orange * s.get_orange()\n        if best is None or c < best_cost:\n            best = s\n            best_cost = c\n    print(best.get_name(), best_cost)\n",
            "explain": "חיפוש מינימום ברשימת אובייקטים: שומרים גם את האובייקט הטוב ביותר וגם את הערך שלו. ההשוואה `<` (ולא `<=`) מבטיחה שבמקרה של שוויון נשארת החנות הראשונה. בסוף מדפיסים פעם אחת, אחרי הלולאה.",
            "tests": [
                {"setup": "ss = [Shop('Mega', 5.9, 3.8, 2.5), Shop('Rami', 6, 3, 2)]", "call": "cheapest(ss, 1, 1, 1)", "out": "Rami 11"},
                {"setup": "ss = [Shop('Mega', 5.9, 3.8, 2.5), Shop('Rami', 6, 3, 2), Shop('Shufersal', 4, 5, 3)]", "call": "cheapest(ss, 2, 0, 0)", "out": "Shufersal 8"},
                {"setup": "ss = [Shop('A', 1, 1, 1), Shop('B', 1, 1, 1)]", "call": "cheapest(ss, 1, 2, 3)", "out": "A 6", "hidden": True},
                {"setup": "ss = [Shop('Only', 2.5, 4, 1)]", "call": "cheapest(ss, 2, 1, 0)", "out": "Only 9", "hidden": True},
                {"setup": "ss = [Shop('A', 10, 1, 1), Shop('B', 1, 10, 10), Shop('C', 3, 3, 3)]", "call": "cheapest(ss, 0, 1, 1)", "out": "A 2", "hidden": True},
            ],
        },
        # ---------- Question 3: Item / NewItem ----------
        {
            "id": "classes-03a",
            "num": "3 (חלק 1)",
            "title": "מחלקת מוצר",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "מפעל מייצר מוצרים. הגדר מחלקה `Item` שמייצגת מוצר, עם התכונות:\n- `catalog` — מספר קטלוגי (מספר שלם)\n- `name` — שם המוצר\n- `price` — מחיר ליחידה\n\n**בנאי:** `Item(catalog, name, price)`, וברירת מחדל: `0` למספרים ו-`\"NA\"` לשם.\n\n**שיטות:**\n- `get_catalog()`, `get_name()`, `get_price()` — מחזירות את הערך.\n- `set_data(catalog, name, price)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת: מספר קטלוגי, שם ומחיר, מופרדים ברווח. למשל: `1001 Chair 120`.\n- `cost(n)` — מקבלת כמות `n` ומחזירה את המחיר הכולל של `n` יחידות.\n\n(את ההרס מ-C++ לא צריך — בפייתון אין צורך לשחרר זיכרון.)\n\n" + CONV,
            "starter": _class_starter("Item"),
            "hints": [
                "`def __init__(self, catalog=0, name=\"NA\", price=0):`",
                "`cost` היא שיטה שמשתמשת בתכונה של האובייקט: `return n * self.price`.",
                "def print_info(self):\n    print(self.catalog, self.name, self.price)\n\ndef cost(self, n):\n    return n * self.price",
            ],
            "solution": ITEM,
            "explain": "השיטה `cost` מראה ששיטה יכולה לקבל פרמטרים נוספים מלבד `self` ולחשב בעזרת התכונות של האובייקט. בחלק 2 נדרוס את השיטה הזו במחלקה יורשת.",
            "tests": [
                {"setup": "it = Item(1001, 'Chair', 120)", "call": "it.cost(3)", "expect": "360"},
                {"setup": "it = Item(1001, 'Chair', 120)", "call": "it.print_info()", "out": "1001 Chair 120"},
                {"setup": "it = Item()", "call": "(it.get_catalog(), it.get_name(), it.get_price())", "expect": "(0, 'NA', 0)", "hidden": True},
                {"setup": "it = Item()\nit.set_data(7, 'Lamp', 2.5)", "call": "(it.get_catalog(), it.get_name(), it.get_price(), it.cost(4))", "expect": "(7, 'Lamp', 2.5, 10.0)", "hidden": True},
                {"setup": "it = Item(5, 'Desk', 300)", "call": "it.cost(0)", "expect": "0", "hidden": True},
            ],
        },
        {
            "id": "classes-03b",
            "num": "3 (חלק 2)",
            "title": "מוצר מיוחד בירושה",
            "kind": "function",
            "difficulty": 3,
            "exam": True,
            "prompt": "המפעל מוסיף מוצרים מיוחדים עם הנחת כמות. הגדר מחלקה `NewItem` ש**יורשת** מ-`Item` (מחלק 1) ומוסיפה תכונה:\n- `bonus` — אחוז ההנחה (מספר שלם, למשל `10` = 10%)\n\n**בנאי:** `NewItem(catalog, name, price, bonus)` עם ברירות מחדל `0`, `\"NA\"`, `0`, `0`. השתמש ב-`super().__init__(...)` כדי לאתחל את התכונות של `Item`.\n\n**שיטות:**\n- `set_bonus(b)` — מעדכנת את אחוז ההנחה.\n- `get_bonus()` — מחזירה אותו.\n- `cost(n)` — **דורסת** את השיטה של `Item`: 100 היחידות הראשונות במחיר המלא, וכל יחידה מעבר ל-100 במחיר מוזל ב-`bonus` אחוזים, כלומר `price * (100 - bonus) / 100`.\n\nלדוגמה, `NewItem(1, 'Pen', 10, 20).cost(150)` → `100*10 + 50*8 = 1400`.\n\nכל השיטות של `Item` (`get_name()` וכו') צריכות לעבוד גם על `NewItem` — בזכות הירושה, בלי לכתוב אותן שוב.\n\n" + PASTE,
            "starter": ITEM + "\n\nclass NewItem(Item):\n    # כתוב כאן את המחלקה\n    pass\n",
            "hints": [
                "הבנאי: `def __init__(self, catalog=0, name=\"NA\", price=0, bonus=0):` ובתוכו `super().__init__(catalog, name, price)` ואז `self.bonus = bonus`.",
                "ב-`cost(n)`: אם `n <= 100` המחיר הוא `n * self.price`. אחרת — 100 במחיר מלא ועוד `n - 100` במחיר המוזל.",
                "def cost(self, n):\n    if n <= 100:\n        return n * self.price\n    discount_price = self.price * (100 - self.bonus) / 100\n    return 100 * self.price + (n - 100) * discount_price",
            ],
            "solution": ITEM + "\n\nclass NewItem(Item):\n    def __init__(self, catalog=0, name=\"NA\", price=0, bonus=0):\n        super().__init__(catalog, name, price)\n        self.bonus = bonus\n\n    def get_bonus(self):\n        return self.bonus\n\n    def set_bonus(self, b):\n        self.bonus = b\n\n    def cost(self, n):\n        if n <= 100:\n            return n * self.price\n        discount_price = self.price * (100 - self.bonus) / 100\n        return 100 * self.price + (n - 100) * discount_price\n",
            "explain": "`class NewItem(Item)` נותן ל-`NewItem` את כל מה שיש ל-`Item`. `super().__init__` מאתחל את התכונות של ההורה, ואחריו מוסיפים את התכונה החדשה. כשכותבים שוב `cost` באותו שם — זו **דריסה**: לאובייקט `NewItem` תיקרא הגרסה החדשה, ולאובייקט `Item` הישנה.",
            "tests": [
                {"setup": "p = NewItem(1, 'Pen', 10, 20)", "call": "p.cost(150)", "expect": "1400"},
                {"setup": "p = NewItem(1, 'Pen', 10, 20)", "call": "(p.get_name(), p.get_price(), p.cost(50))", "expect": "('Pen', 10, 500)"},
                {"setup": "p = NewItem(2, 'Cup', 5, 50)", "call": "isinstance(p, Item)", "expect": "True", "hidden": True},
                {"setup": "p = NewItem(2, 'Cup', 5, 50)\np.set_bonus(10)", "call": "(p.get_bonus(), p.cost(1000))", "expect": "(10, 4550.0)", "hidden": True},
                {"setup": "p = NewItem()", "call": "(p.get_catalog(), p.get_name(), p.get_price(), p.get_bonus())", "expect": "(0, 'NA', 0, 0)", "hidden": True},
                {"setup": "p = NewItem(3, 'Box', 4, 25)", "call": "p.cost(100)", "expect": "400", "hidden": True},
                {"setup": "a = Item(9, 'Bag', 10)", "call": "a.cost(150)", "expect": "1500", "hidden": True},
            ],
        },
        # ---------- Question 4: Check ----------
        {
            "id": "classes-04a",
            "num": "4 (חלק 1)",
            "title": "מחלקת המחאה",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "הגדר מחלקה `Check` שמתארת המחאה (צ'ק), עם התכונות:\n- `ch_number` — מספר ההמחאה (מחרוזת, למשל `\"A100\"`)\n- `bname` — שם הבנק (מחרוזת)\n- `dep_number` — מספר הסניף (מספר שלם)\n- `amount` — סכום ההמחאה (מספר)\n\n**בנאי:** `Check(ch_number, bname, dep_number, amount)`. אם לא מעבירים ערכים — המחרוזות יהיו `\"UNKNOWN\"` והמספרים `0`.\n\n**שיטות:**\n- `get_ch_number()`, `get_bname()`, `get_dep_number()`, `get_amount()` — מחזירות את הערך.\n- `set_data(ch_number, bname, dep_number, amount)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת: מספר המחאה, בנק, סניף וסכום, מופרדים ברווח. למשל: `A100 Leumi 12 500.5`.\n\n" + CONV,
            "starter": _class_starter("Check"),
            "hints": [
                "שים לב שכאן ברירת המחדל למחרוזות היא `\"UNKNOWN\"` (ולא `\"NA\"`).",
                "`def __init__(self, ch_number=\"UNKNOWN\", bname=\"UNKNOWN\", dep_number=0, amount=0):`",
                "def print_info(self):\n    print(self.ch_number, self.bname, self.dep_number, self.amount)",
            ],
            "solution": CHECK,
            "explain": "אותו מבנה כמו בשאר המחלקות — בנאי עם ערכי ברירת מחדל, שיטות `get`, `set_data` ו-`print_info`. ב-C++ היה כאן גם הרס; בפייתון הזיכרון משתחרר אוטומטית ולכן אין צורך בו.",
            "tests": [
                {"setup": "c = Check('A100', 'Leumi', 12, 500.5)", "call": "c.get_amount()", "expect": "500.5"},
                {"setup": "c = Check('A100', 'Leumi', 12, 500.5)", "call": "c.print_info()", "out": "A100 Leumi 12 500.5"},
                {"setup": "c = Check()", "call": "(c.get_ch_number(), c.get_bname(), c.get_dep_number(), c.get_amount())", "expect": "('UNKNOWN', 'UNKNOWN', 0, 0)", "hidden": True},
                {"setup": "c = Check()\nc.set_data('B7', 'Hapoalim', 600, 99)", "call": "c.print_info()", "out": "B7 Hapoalim 600 99", "hidden": True},
                {"setup": "c = Check('Z1', 'Discount', 3, 10)", "call": "(c.get_ch_number(), c.get_bname(), c.get_dep_number())", "expect": "('Z1', 'Discount', 3)", "hidden": True},
            ],
        },
        {
            "id": "classes-04b",
            "num": "4 (חלק 2)",
            "title": "חיפוש המחאה",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "כתוב פונקציה `search(checks, target)` שמקבלת רשימה של אובייקטים מסוג `Check` (מחלק 1) ואובייקט `Check` נוסף בשם `target`.\n\nהפונקציה בודקת אם ברשימה יש המחאה עם **אותו מספר המחאה** (`ch_number`) כמו של `target`:\n- אם כן — מדפיסה את נתוני ההמחאה **שנמצאה ברשימה** בעזרת `print_info()` (הראשונה אם יש כמה).\n- אם לא — מדפיסה `Check not exist`.\n\n(ב-C++ היה כאן מצביע ו-`new`; בפייתון פשוט יוצרים אובייקט: `target = Check(\"A100\")`.)\n\n" + PASTE,
            "starter": CHECK + "\n\ndef search(checks, target):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על הרשימה והשווה `c.get_ch_number()` ל-`target.get_ch_number()`.",
                "כשמצאת — הדפס עם `c.print_info()` וצא מיד מהפונקציה עם `return`. אם הלולאה הסתיימה בלי למצוא — הדפס את ההודעה.",
                "for c in checks:\n    if c.get_ch_number() == target.get_ch_number():\n        c.print_info()\n        return\nprint(\"Check not exist\")",
            ],
            "solution": CHECK + "\n\ndef search(checks, target):\n    for c in checks:\n        if c.get_ch_number() == target.get_ch_number():\n            c.print_info()\n            return\n    print(\"Check not exist\")\n",
            "explain": "זה חיפוש ברשימה: משווים תכונה אחת של כל אובייקט לתכונה של אובייקט המטרה. ה-`return` עוצר את החיפוש אחרי ההתאמה הראשונה, ולכן ההודעה `Check not exist` מודפסת רק אם הלולאה עברה על הכול ולא מצאה.",
            "tests": [
                {"setup": "cs = [Check('A1', 'Leumi', 12, 100), Check('B2', 'Hapoalim', 5, 250.5)]", "call": "search(cs, Check('B2'))", "out": "B2 Hapoalim 5 250.5"},
                {"setup": "cs = [Check('A1', 'Leumi', 12, 100), Check('B2', 'Hapoalim', 5, 250.5)]", "call": "search(cs, Check('C3', 'Leumi', 12, 100))", "out": "Check not exist"},
                {"setup": "cs = [Check('A1', 'Leumi', 12, 100), Check('A1', 'Discount', 1, 7)]", "call": "search(cs, Check('A1', 'Other', 9, 9))", "out": "A1 Leumi 12 100", "hidden": True},
                {"call": "search([], Check('A1'))", "out": "Check not exist", "hidden": True},
            ],
        },
        # ---------- Question 5: Film ----------
        {
            "id": "classes-05a",
            "num": "5 (חלק 1)",
            "title": "מחלקת סרט",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "הגדר מחלקה `Film` שמייצגת סרט בספרייה, עם התכונות:\n- `name` — שם הסרט\n- `director` — הבמאי\n- `copies` — מספר העותקים שבספרייה כרגע (מספר שלם)\n\n**בנאי:** `Film(name, director, copies)`, וברירת מחדל: `\"NA\"` למחרוזות ו-`0` למספר.\n\n**שיטות:**\n- `get_name()`, `get_director()`, `get_copies()` — מחזירות את הערך.\n- `set_data(name, director, copies)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת: שם, במאי ומספר עותקים, מופרדים ברווח. למשל: `Up Docter 3`.\n- `insert()` — החזרת עותק לספרייה: מגדילה את `copies` ב-1.\n- `check()` — מחזירה `True` אם יש לפחות עותק אחד (אפשר להשאיל), אחרת `False`.\n- `remove()` — השאלת עותק: מקטינה את `copies` ב-1 (מי שקורא לה אחראי לבדוק קודם עם `check()`).\n\n" + CONV,
            "starter": _class_starter("Film"),
            "hints": [
                "`def __init__(self, name=\"NA\", director=\"NA\", copies=0):`",
                "`insert` ו-`remove` משנות את התכונה: `self.copies += 1` / `self.copies -= 1`. הן לא מחזירות כלום.",
                "def check(self):\n    return self.copies > 0",
            ],
            "solution": FILM,
            "explain": "שיטות כמו `insert` ו-`remove` משנות את **מצב** האובייקט — השינוי נשמר ב-`self.copies` ונראה בכל קריאה הבאה. `check` מחזירה ישירות את תוצאת ההשוואה `self.copies > 0`.",
            "tests": [
                {"setup": "f = Film('Up', 'Docter', 3)\nf.remove()", "call": "f.get_copies()", "expect": "2"},
                {"setup": "f = Film('Up', 'Docter', 3)", "call": "f.print_info()", "out": "Up Docter 3"},
                {"setup": "f = Film()", "call": "(f.get_name(), f.get_director(), f.get_copies(), f.check())", "expect": "('NA', 'NA', 0, False)", "hidden": True},
                {"setup": "f = Film()\nf.insert()", "call": "(f.get_copies(), f.check())", "expect": "(1, True)", "hidden": True},
                {"setup": "f = Film()\nf.set_data('Jaws', 'Spielberg', 1)\nf.insert()\nf.insert()", "call": "f.print_info()", "out": "Jaws Spielberg 3", "hidden": True},
            ],
        },
        {
            "id": "classes-05b",
            "num": "5 (חלק 2)",
            "title": "השאלה והחזרה",
            "kind": "function",
            "difficulty": 3,
            "exam": True,
            "prompt": "כתוב פונקציה `borrow_and_return(films, m, n)` שמקבלת רשימה של אובייקטים מסוג `Film` (מחלק 1) ושני אינדקסים `m` ו-`n`, ומבצעת לפי הסדר:\n\n1. **השאלה** של הסרט במקום `m`: אם `check()` מחזירה `True` — קוראים ל-`remove()`. אחרת מדפיסים `Not available` ולא משנים כלום.\n2. **החזרה** של הסרט במקום `n` — קוראים ל-`insert()`.\n3. מדפיסים את נתוני **כל** הסרטים, כל סרט בשורה בעזרת `print_info()`.\n\nלדוגמה, עבור `[Film('Up', 'Docter', 1), Film('Jaws', 'Spielberg', 0)]`, `m = 1`, `n = 1`: אין עותק של Jaws להשאלה → `Not available`, ואז מחזירים עותק שלו. יודפס:\n```\nNot available\nUp Docter 1\nJaws Spielberg 1\n```\n" + PASTE,
            "starter": FILM + "\n\ndef borrow_and_return(films, m, n):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "`films[m]` הוא אובייקט — אפשר לקרוא ישירות `films[m].check()`.",
                "קודם `if films[m].check(): films[m].remove()` עם `else` להודעה, אחר כך `films[n].insert()`, ובסוף לולאה על כל הסרטים.",
                "if films[m].check():\n    films[m].remove()\nelse:\n    print(\"Not available\")\nfilms[n].insert()\nfor f in films:\n    f.print_info()",
            ],
            "solution": FILM + "\n\ndef borrow_and_return(films, m, n):\n    if films[m].check():\n        films[m].remove()\n    else:\n        print(\"Not available\")\n    films[n].insert()\n    for f in films:\n        f.print_info()\n",
            "explain": "גישה לאובייקט ברשימה לפי אינדקס (`films[m]`) נותנת את האובייקט עצמו, ולכן שינוי דרכו משנה את הסרט שברשימה. הבדיקה עם `check()` לפני `remove()` מונעת מספר עותקים שלילי.",
            "tests": [
                {"setup": "fs = [Film('Up', 'Docter', 1), Film('Jaws', 'Spielberg', 0)]", "call": "borrow_and_return(fs, 1, 1)", "out": "Not available\nUp Docter 1\nJaws Spielberg 1"},
                {"setup": "fs = [Film('Up', 'Docter', 2), Film('Jaws', 'Spielberg', 0)]", "call": "borrow_and_return(fs, 0, 1)", "out": "Up Docter 1\nJaws Spielberg 1"},
                {"setup": "fs = [Film('A', 'X', 1), Film('B', 'Y', 5), Film('C', 'Z', 0)]", "call": "borrow_and_return(fs, 0, 0)", "out": "A X 1\nB Y 5\nC Z 0", "hidden": True},
                {"setup": "fs = [Film('A', 'X', 0), Film('B', 'Y', 5), Film('C', 'Z', 0)]", "call": "borrow_and_return(fs, 2, 1)", "out": "Not available\nA X 0\nB Y 6\nC Z 0", "hidden": True},
                {"setup": "fs = [Film('A', 'X', 3), Film('B', 'Y', 5)]\nborrow_and_return(fs, 1, 0)", "call": "fs[1].get_copies()", "expect": "4", "hidden": True},
            ],
        },
        # ---------- Question 6: Toy ----------
        {
            "id": "classes-06a",
            "num": "6 (חלק 1)",
            "title": "מחלקת צעצוע",
            "kind": "function",
            "difficulty": 1,
            "exam": True,
            "prompt": "הגדר מחלקה `Toy` שמייצגת צעצוע, עם התכונות:\n- `code` — קוד הצעצוע (מספר שלם, למשל `4511`)\n- `group` — קבוצה (למשל `\"Cars\"`)\n- `manufact` — שם היצרן (למשל `\"Lego\"`)\n- `year` — הגיל שאליו מיועד הצעצוע (מספר שלם, למשל `4`)\n\n**בנאי:** `Toy(code, group, manufact, year)`, וברירת מחדל: `0` למספרים ו-`\"NA\"` למחרוזות.\n\n**שיטות:**\n- `get_code()`, `get_group()`, `get_manufact()`, `get_year()` — מחזירות את הערך.\n- `set_data(code, group, manufact, year)` — מעדכנת את כל התכונות.\n- `print_info()` — מדפיסה בשורה אחת: קוד, קבוצה, יצרן וגיל, מופרדים ברווח. למשל: `4511 Cars Lego 4`.\n\n" + CONV,
            "starter": _class_starter("Toy"),
            "hints": [
                "`def __init__(self, code=0, group=\"NA\", manufact=\"NA\", year=0):`",
                "ארבע שיטות `get_...` (כל אחת `return self.xxx`), ו-`set_data` שמעדכנת את כולן.",
                "def print_info(self):\n    print(self.code, self.group, self.manufact, self.year)",
            ],
            "solution": TOY,
            "explain": "מחלקת נתונים קלאסית: הבנאי שומר ארבע תכונות עם ערכי ברירת מחדל, ושאר השיטות קוראות או משנות אותן דרך `self`.",
            "tests": [
                {"setup": "t = Toy(4511, 'Cars', 'Lego', 4)", "call": "t.get_manufact()", "expect": "'Lego'"},
                {"setup": "t = Toy(4511, 'Cars', 'Lego', 4)", "call": "t.print_info()", "out": "4511 Cars Lego 4"},
                {"setup": "t = Toy()", "call": "(t.get_code(), t.get_group(), t.get_manufact(), t.get_year())", "expect": "(0, 'NA', 'NA', 0)", "hidden": True},
                {"setup": "t = Toy()\nt.set_data(12, 'Dolls', 'Mattel', 6)", "call": "t.print_info()", "out": "12 Dolls Mattel 6", "hidden": True},
                {"setup": "t = Toy(1, 'Balls', 'Nike', 8)", "call": "(t.get_code(), t.get_group(), t.get_year())", "expect": "(1, 'Balls', 8)", "hidden": True},
            ],
        },
        {
            "id": "classes-06b",
            "num": "6 (חלק 2)",
            "title": "צעצועים לפי גיל",
            "kind": "function",
            "difficulty": 2,
            "exam": True,
            "prompt": "כתוב פונקציה `toys_for_age(toys, age)` שמקבלת רשימה של אובייקטים מסוג `Toy` (מחלק 1) וגיל של ילד, ו**מדפיסה** בעזרת `print_info()` את נתוני כל הצעצועים שמיועדים **בדיוק** לגיל הזה (`year == age`), כל צעצוע בשורה, לפי הסדר ברשימה.\n\nאם אין אף צעצוע מתאים — הדפס `Not found`.\n\n" + PASTE,
            "starter": TOY + "\n\ndef toys_for_age(toys, age):\n    # כתוב כאן את הקוד\n    pass\n",
            "hints": [
                "עבור על הרשימה ובדוק `t.get_year() == age`.",
                "כדי לדעת בסוף אם נמצא משהו, השתמש במשתנה דגל `found = False` שהופך ל-`True` כשמדפיסים צעצוע.",
                "found = False\nfor t in toys:\n    if t.get_year() == age:\n        t.print_info()\n        found = True\nif not found:\n    print(\"Not found\")",
            ],
            "solution": TOY + "\n\ndef toys_for_age(toys, age):\n    found = False\n    for t in toys:\n        if t.get_year() == age:\n            t.print_info()\n            found = True\n    if not found:\n        print(\"Not found\")\n",
            "explain": "כאן צריך להדפיס **את כל** ההתאמות, ולכן לא יוצאים מהלולאה אחרי הראשונה (בניגוד לחיפוש). משתנה הדגל `found` זוכר אם הודפס משהו, כדי להחליט אחרי הלולאה אם להדפיס `Not found`.",
            "tests": [
                {"setup": "ts = [Toy(4511, 'Cars', 'Lego', 4), Toy(12, 'Dolls', 'Mattel', 6), Toy(30, 'Blocks', 'Lego', 4)]", "call": "toys_for_age(ts, 4)", "out": "4511 Cars Lego 4\n30 Blocks Lego 4"},
                {"setup": "ts = [Toy(4511, 'Cars', 'Lego', 4), Toy(12, 'Dolls', 'Mattel', 6)]", "call": "toys_for_age(ts, 9)", "out": "Not found"},
                {"setup": "ts = [Toy(4511, 'Cars', 'Lego', 4), Toy(12, 'Dolls', 'Mattel', 6)]", "call": "toys_for_age(ts, 6)", "out": "12 Dolls Mattel 6", "hidden": True},
                {"call": "toys_for_age([], 3)", "out": "Not found", "hidden": True},
            ],
        },
    ],
}
