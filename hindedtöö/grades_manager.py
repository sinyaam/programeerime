# grades_manager.py

# grades_manager.py

from file_handler import load_grades, save_grades

def add_student(name, grades, filename="grades.txt"):
    """Добавляет нового студента и его оценки."""
    students = load_grades(filename)
    # Заменили map на список
    grades_str = ', '.join([str(grade) for grade in grades])  # Преобразуем оценки в строку
    new_student = f"Имя: {name}\nОценки: {grades_str}"
    students.append(new_student)
    save_grades(students, filename)
    print(f"Студент {name} добавлен с оценками: {grades}")




def view_students(filename="grades.txt"):
    """Просмотр всех студентов и их оценок."""
    students = load_grades(filename)
    if not students:
        print("Нет данных о студентах.")
    else:
        for student in students:
            print(student)
            print("\n---\n")

def calculate_average_grade(name, filename="grades.txt"):
    """Вычисляет среднюю оценку студента по имени."""
    students = load_grades(filename)
    for student in students:
        if student.startswith(f"Имя: {name}"):
            grades_str = student.split("\n")[1].replace("Оценки: ", "")
            grades = [int(grade.strip()) for grade in grades_str.split(", ")]  # Используем цикл for вместо map
            average = sum(grades) / len(grades)
            return average
    print(f"Студент с именем {name} не найден.")
    return None

def find_student_by_name(name, filename="grades.txt"):
    """Ищет студента по имени."""
    students = load_grades(filename)
    for student in students:
        if student.startswith(f"Имя: {name}"):
            return student
    print(f"Студент с именем {name} не найден.")
    return None
