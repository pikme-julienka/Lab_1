# Лабораторна робота 1

Дисципліна «Високорівнева розробка програмного забезпечення»
## Структура

| Папка | Зміст |
|---|---|
| `part1/` | Встановлення Python 2.7, 3.12, 3.13 (Windows) та способи запуску: `python`, `py`, IDLE, shebang |
| `part2/` | Віртуальні середовища venv, virtualenv, conda (Windows); `py2_vs_py3.py` — 10 відмінностей Python 2 і 3 |
| `part3/` | Ubuntu (WSL): pyenv (3.8 / 3.10 / 3.12), uv (3.13 free-threaded), venv + rich |
| `part4/` | `student_stats.py` — обробка оцінок студентів (словники, списки, умови, цикли) |
| `student_marks/` | Вхідні дані для частини 4 |

Скріншоти виконання кожної частини лежать у `partN/screenshots/`.

## Запуск

```bash
# Частина 1
py -2.7 part1/which_python.py
py -3.12 part1/which_python.py
py part1/shebang_py2.py

# Частина 2 (одна й та сама програма в обох версіях)
py -2.7 part2/py2_vs_py3.py
py -3.12 part2/py2_vs_py3.py

# Частина 3 (Ubuntu)
pyenv global 3.8.18 && python part3/version_test.py

# Частина 4
python part4/student_stats.py
```

## Примітки

- Частину 3 виконано у WSL (Ubuntu 26.04 LTS).
- `part3/pyenv_bashrc.txt` — фрагмент, доданий до `~/.bashrc` для роботи pyenv.
- У консолі Windows вивід кирилиці з Python 2 потребує `chcp 65001`.
