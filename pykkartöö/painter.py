from pykkar import *
def left():
    right()
    right()
    right()
    
def func1():
    for i in range(18):
        if not is_painted():  # Проверяем, покрашен ли текущий квадрат
            if is_wall():  # Если перед роботом стена
                right()  # Поворачиваем направо
            paint()  # Красим текущий квадрат
        step()  # Двигаемся вперед
def func2():
    for i in range(5):
        if is_painted():  # Проверяем, покрашен ли текущий квадрат
            right()  # Поворачиваем направо
            step()
        else:
            paint()
            step()        
def func3():
    for i in range(5):
        if is_painted():  # Проверяем, покрашен ли текущий квадрат
            right()
            right()
            right()
            step()
        else:
            paint()
            step()
def func4():
    right()
    right()
    step()
    left()
    step()
    right()
    step()
    left()
    step()
    paint()
    step()
    paint()
    left()
    step()
    paint()
    step()
    paint()
    right()
def func5():
    for i in range(14):
        if not is_painted():  # Проверяем, покрашен ли текущий квадрат
            if is_wall():  # Если перед роботом стена
                right()  # Поворачиваем направо
            paint()  # Красим текущий квадрат
        step()  # Двигаемся вперед
def func6():
    step()
    func2()
def func7():
    left()
    step()
    paint()
    step()
    paint()
    left()
    paint()
    step()
    paint()
    step()
    paint()
    right()