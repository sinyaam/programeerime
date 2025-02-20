from pykkar import *
from painter import left, func1, func2, func3, func4, func5, func6, func7

# Создание мира с двумя комнатами слева
create_world("""
###########################
#>     #      #     #     #
#      #      #     #     #
#                         #
#      #      #     #     #
#      #      #     #     #
###########################
""")

# Запуск функций
func1()
func2()
func3()
func2()
func3()
func4()
func1()
func2()
func3()
func2()
func3()
func4()
func5()
func2()
func2()
func6()
func7()
func5()
func2()
func2()
func6()
# Ожидание ввода для завершения
input("Нажмите Enter, чтобы завершить...")
