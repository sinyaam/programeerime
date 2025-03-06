# main.py

from notes_manager import add_note, view_notes, delete_note_by_title

def show_menu():
    """Отображает главное меню."""
    print("\n--- Меню ---")
    print("1. Добавить заметку")
    print("2. Просмотреть все заметки")
    print("3. Удалить заметку по заголовку")
    print("4. Выйти")

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            text = input("Введите текст заметки: ")
            add_note(title, text)
            print("Заметка добавлена!")
        
        elif choice == "2":
            view_notes()
        
        elif choice == "3":
            title = input("Введите заголовок заметки для удаления: ")
            delete_note_by_title(title)
        
        elif choice == "4":
            print("Выход из программы...")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
main()

