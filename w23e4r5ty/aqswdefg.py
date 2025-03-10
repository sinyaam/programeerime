import os

# Функция для просмотра файлов в папке
def list_file(folder):
    if os.path.exists(folder):  # Проверка на существование папки
        filelist = os.listdir(folder)
        if filelist:
            print("Файлы в папке:")
            for elem in filelist:
                print(elem)
        else:
            print(f"Папка {folder} пуста.")
    else:
        print(f"Папка {folder} не существует.")

# Функция для создания папки
def makedirectory():
    directory_name = input("Milline kaust sul on vajalik (имя папки для создания)? ").strip()
    if not os.path.exists(directory_name):  # Проверка, если папка уже существует
        os.mkdir(directory_name)
        print(f"Kaust {directory_name} oli edukalt tehtud.")
    else:
        print(f"Kaust {directory_name} juba olemas.")
    return directory_name

# Функция для удаления папки
def deletefolder(folder):
    if os.path.exists(folder):  # Проверка на существование папки
        os.rmdir(folder)
        print(f"Kaust {folder} oli edukalt kustutatud.")
    else:
        print(f"Папка {folder} не существует, не могу удалить.")

# Запрос команды и выполнение действия
userinput = input("Mida sa tahad teha? (mkdir, ls, delete): ").strip()

if userinput == "mkdir":
    # Создаем папку
    makedirectory()
elif userinput == "ls":
    # Просмотр файлов в папке
    folder = input("Введите полный путь к папке для отображения: ").strip()
    list_file(folder)
elif userinput == "delete":
    # Удаление папки
    folder = input("Введите полный путь к папке для удаления: ").strip()
    deletefolder(folder)
else:
    print("Неизвестная команда.")