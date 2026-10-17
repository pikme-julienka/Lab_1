# -*- coding: utf-8 -*-
# 10 основних відмінностей між Python 2 і Python 3.
# Один і той самий файл запускається в обох версіях, і вивід відрізняється.
from __future__ import print_function  # щоб print() як функція працював і в Python 2

import sys

PY2 = sys.version_info[0] == 2

print("=" * 60)
print("Python", sys.version.split()[0], "|", sys.executable)
print("=" * 60)


def title(n, text):
    print()
    print("{0}. {1}".format(n, text))


# 1. print: у Python 2 це оператор, у Python 3 - функція
title(1, "print - оператор (Py2) чи функція (Py3)")
try:
    # dont_inherit=True: не переносити print_function з цього файлу
    compile('print "hello"', "<test>", "exec", 0, True)
    print("   print \"hello\" без дужок - працює (оператор)")
except SyntaxError:
    print("   print \"hello\" без дужок - SyntaxError, потрібно print(\"hello\")")

# 2. Ділення цілих чисел
title(2, "Ділення цілих чисел 7 / 2")
print("   7 / 2  =", eval("7 / 2"), "  (Py2: цілочисельне, Py3: дробове)")
print("   7 // 2 =", 7 // 2, "  (цілочисельне в обох версіях)")

# 3. Рядки: байти чи Unicode
title(3, "Тип рядкового літерала 'abc'")
print("   type('abc')  =", type("abc"))
print("   type(u'abc') =", type(u"abc"))
print("   (Py2: str - це байти, Unicode окремо; Py3: str - це завжди Unicode)")

# 4. range / xrange
title(4, "range() - список чи ленивий об'єкт")
r = range(5)
print("   range(5) =", r, "| тип:", type(r).__name__)
try:
    xrange
    print("   xrange існує")
except NameError:
    print("   xrange не існує (NameError)")

# 5. input / raw_input
title(5, "input() та raw_input()")
try:
    raw_input
    print("   raw_input існує, а input() виконує введене як код (eval)")
except NameError:
    print("   raw_input не існує, input() завжди повертає рядок")

# 6. Методи словника
title(6, "dict.keys() - список чи view")
d = {"a": 1, "b": 2}
print("   type(d.keys()) =", type(d.keys()).__name__)
print("   has_key є?", hasattr(d, "has_key"), "  ('key in d' працює в обох)")

# 7. map / filter / zip повертають список чи ітератор
title(7, "map() - список чи ітератор")
m = map(lambda x: x * 2, [1, 2, 3])
print("   map(...) =", m)

# 8. Цілі числа: int і long
title(8, "Великі цілі числа: int та long")
big = 2 ** 70
print("   type(2**70) =", type(big).__name__)
print("   (Py2: окремий тип long; Py3: є тільки int довільної довжини)")

# 9. Синтаксис обробки винятків
title(9, "except Exception, e")
try:
    compile("try:\n    pass\nexcept Exception, e:\n    pass\n", "<test>", "exec")
    print("   'except Exception, e' - дозволено (Py2)")
except SyntaxError:
    print("   'except Exception, e' - SyntaxError, тільки 'except Exception as e'")

# 10. Округлення
title(10, "round(2.5) та round(3.5)")
print("   round(2.5) =", round(2.5), "| round(3.5) =", round(3.5))
print("   (Py2: від нуля -> 3.0, 4.0; Py3: банківське до парного -> 2, 4, і повертає int)")

print()
print("=" * 60)
