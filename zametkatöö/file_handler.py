 # file_handler.py

def load_notes(filename="notes.txt"):
    """Загружает все заметки из файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
        notes = content.split("\n---\n") if content else []
        return notes
    except FileNotFoundError:
        return []

def save_notes(notes, filename="notes.txt"):
    """Сохраняет все заметки в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n---\n")
        if notes:
            file.truncate()  # Убираем лишний разделитель в конце
