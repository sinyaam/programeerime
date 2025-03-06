# file_handler.py

def load_grades(filename="grades.txt"):
    """Загружает все данные об оценках студентов из файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
        students = content.split("\n---\n") if content else []
        return students
    except FileNotFoundError:
        return []

def save_grades(students, filename="grades.txt"):
    """Сохраняет данные об оценках студентов в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            file.write(student + "\n---\n")
        if students:
            file.truncate()  # Убираем лишний разделитель в конце
