import os

# Папка з файлами оцінок (лежить поруч із папкою part4)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "student_marks")

SUBJECT_FILES = {
    "math": "math.txt",
    "statistics": "statistics.txt",
    "physics": "physics.txt",
}
NAMES_FILE = "student_names.txt"


# ---------- 1. Зчитування файлів ----------
files_in_dir = os.listdir(DATA_DIR)
required_files = list(SUBJECT_FILES.values()) + [NAMES_FILE]

print("Файли в папці:", files_in_dir)
for file_name in required_files:
    if file_name in files_in_dir:
        print("  [OK]", file_name, "знайдено")
    else:
        print("  [ПОМИЛКА]", file_name, "не знайдено")
        raise SystemExit(1)

# Оцінки: {предмет: [оцінка1, оцінка2, ...]}
marks = {}
for subject, file_name in SUBJECT_FILES.items():
    subject_marks = []
    with open(os.path.join(DATA_DIR, file_name), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                subject_marks.append(int(line))
    marks[subject] = subject_marks

# Список імен студентів
names = []
with open(os.path.join(DATA_DIR, NAMES_FILE), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            names.append(line)

for subject in marks:
    if len(marks[subject]) != len(names):
        print("Кількість оцінок з", subject, "не збігається з кількістю студентів")
        raise SystemExit(1)


# ---------- 2. Обробка даних ----------
# {ім'я студента: {предмет: оцінка}}
students = {}
for i in range(len(names)):
    subject_dict = {}
    for subject in marks:
        subject_dict[subject] = marks[subject][i]
    students[names[i]] = subject_dict

# Середня оцінка кожного студента
averages = {}
for name, subject_dict in students.items():
    total = 0
    for mark in subject_dict.values():
        total += mark
    averages[name] = total / len(subject_dict)


# ---------- 3. Виведення результатів ----------
print()
print("=== Середня оцінка кожного студента ===")
for name in students:
    print(f"студент: {name}, середня оцінка: {averages[name]:.2f}")

print()
print("=== Топ-3 студенти за середньою оцінкою ===")
ranking = sorted(averages.items(), key=lambda item: item[1], reverse=True)
for place in range(3):
    name, avg = ranking[place]
    print(f"{place + 1}. {name} ({avg:.2f})")

print()
print("=== Статистика по предметах ===")
print("Загальна кількість студентів:", len(students))
print()
for subject, subject_marks in marks.items():
    avg = sum(subject_marks) / len(subject_marks)
    print(f"предмет: {subject}, середня оцінка: {avg:.2f}, "
          f"min оцінка: {min(subject_marks)}, max оцінка: {max(subject_marks)}")

print()
print("=== Найкращий студент з кожного предмету ===")
for subject in marks:
    best_mark = max(marks[subject])
    # Найвищий бал можуть мати кілька студентів - виводимо всіх
    best_names = []
    for name, subject_dict in students.items():
        if subject_dict[subject] == best_mark:
            best_names.append(name)
    print(f"{subject} | студент: {', '.join(best_names)}, оцінка: {best_mark}")

print()
print("=== Студенти із середньою оцінкою нижче 50 ===")
low_students = []
for name, avg in averages.items():
    if avg < 50:
        low_students.append(name)

print("Кількість студентів з оцінкою нижче 50:", len(low_students))
for name in low_students:
    print(f"{name} ({averages[name]:.2f})")
