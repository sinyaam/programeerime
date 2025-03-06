# notes_manager.py

from file_handler import load_notes, save_notes

def add_note(title, text, filename="notes.txt"):
    """Добавляет новую заметку."""
    notes = load_notes(filename)
    new_note = f"Заголовок: {title}\nТекст: {text}"
    notes.append(new_note)
    save_notes(notes, filename)

def view_notes(filename="notes.txt"):
    """Просмотр всех заметок."""
    notes = load_notes(filename)
    if not notes:
        print("Заметок нет.")
    else:
        for note in notes:
            print(note)
            print("\n---\n")

def delete_note_by_title(title, filename="notes.txt"):
    """Удаляет заметку по заголовку."""
    notes = load_notes(filename)
    notes_to_keep = []  # Новый список для хранения оставшихся заметок

    # Проходим по каждой заметке в списке
    for note in notes:
        # Убираем лишние пробелы перед проверкой
        if not note.strip().startswith(f"Заголовок: {title.strip()}"):
            notes_to_keep.append(note)  # Добавляем её в список оставшихся заметок
            print(notes_to_keep)
    if len(notes) == len(notes_to_keep):
        print("Заметка с таким заголовком не найдена.")
    else:
        save_notes(notes_to_keep, filename)
        print(f"Заметка с заголовком '{title}' удалена.")
