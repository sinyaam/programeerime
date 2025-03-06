# main.py

from grades_manager import add_student, view_students, calculate_average_grade, find_student_by_name

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить студента и его оценки")
        print("2. Просмотр всех студентов и их оценок")
        print("3. Вычислить среднюю оценку студента")
        print("4. Найти студента по имени")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            name = input("Введите имя студента: ")
            grades = input("Введите оценки через запятую (например, 5, 4, 3): ").split(",")
            grades = [int(grade.strip()) for grade in grades]  # Преобразуем в список целых чисел
            add_student(name, grades)

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Введите имя студента для вычисления средней оценки: ")
            average = calculate_average_grade(name)
            if average is not None:
                print(f"Средняя оценка студента {name}: {average:.2f}")

        elif choice == "4":
            name = input("Введите имя студента для поиска: ")
            student = find_student_by_name(name)
            if student:
                print(student)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
