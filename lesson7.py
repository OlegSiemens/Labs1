from math import tan, acos
import pickle

class ResultStorage:
    resultG = []
    resultF = []
    resultY = []

    def add_g(self, g):
        self.resultG.append(g)

    def add_f(self, f):
        self.resultF.append(f)

    def add_y(self, y):
        self.resultY.append(y)

    def clear(self):
        self.resultG = []
        self.resultF = []
        self.resultY = []

    def toString(self):
        print("\n")
        print("Массив значений функции G: \n" + str(self.resultG))
        print("Массив значений функции F: \n" + str(self.resultF))
        print("Массив значений функции Y: \n" + str(self.resultY))


a = float(input('Введите а: '))
xMax = int(input('Введите максимальное значение x: '))
xMin = int(input('Введите минимальное значение x: '))
stepCount = int(input('Введите количество шагов для вычисления функции: '))

storage = ResultStorage()

if xMin >= xMax:
    print('Максимальное значение {0} больше или равно минимальному {1}'.format(xMax, xMin))
    exit()


def calc(a, x):
    g = 5 * ((-9 * a ** 2) - (11 * a * x) + (14 * x ** 2)) / ((15 * a ** 2) + (49 * a * x) + (24 * x ** 2))
    storage.add_g(g)

    try:
        storage.add_f(tan((18 * a ** 2) + (29 * a * x) + (10 * x ** 2)))
    except ValueError or ZeroDivisionError:
        pass

    try:
        storage.add_y(acos((-7 * a ** 2) - (10 * a * x) + (8 * x ** 2) + 1))
    except ValueError or ZeroDivisionError:
        pass


count = 0
while count < stepCount:
    x = xMin + count / 10
    if x <= xMax:
        calc(a, x)
        count += 1
    else:
        break

# Открываем файл на запись
file = open(r'data.txt', 'wb')

# Записываем массивы в файл
pickle.dump(storage.resultG, file)
pickle.dump(storage.resultF, file)
pickle.dump(storage.resultY, file)
file.close()

# Очищаем объкт
storage.clear()

# Открываем файл на чтение
file = open(r'data.txt', 'rb')
storage.resultG = pickle.load(file)
storage.resultF = pickle.load(file)
storage.resultY = pickle.load(file)

# Выводим результат
print(storage.toString())
