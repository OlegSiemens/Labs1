from math import tan, acos, pi , sin , atan

import math

a = float(input('Введите а: '))
xMax = int(input('Введите максимальное значение x: '))
xMin = int(input('Введите минимальное значение x: '))
stepCount = int(input('Введите количество шагов для вычисления функции: '))

x1 = []
y1 = []

if xMin >= xMax:
    print('Максимальное значение {0} больше или равно минимальному {1}'.format(xMax, xMin))
    exit()

n = int(input('Выберите функцию для вычисления: \n   1 - функция g \n   2 - функция f \n   3 - функция y\nНомер: '))


def calc(a, x):
    if 1 <= n <= 3:
        if n == 1:
            g = 5 * ((10 * a ** 2 ) + (31 * a * x) + (15 * x ** 2)) / ((20 * a ** 2) + (23 * a * x) + (6 * x ** 2))
            x1.append(x)
            y1.append(g)
        elif n == 2:
            try:
                x1.append(x)
                y1.append(3 ** (a ** 2) + (3 * a * x) + ( 2 * x ** 2))
            except ValueError:
                pass
        elif n == 3:
            try:
                x1.append(x)
                y1.append( math.acosh((-a ** 2) + (2 * a * x) + (3 * x ** 2 + 1)))
            except ValueError:
                pass
    else:
        print('Такой функции не найдено')
        pass


count = 0
while count < stepCount:
    x = xMin + count / 10
    if x <= xMax:
        calc(a, x)
        count += 1
    else:
        break

for result in zip(x1, y1):
    print('{0:.3f}  {1:.3f}'.format(*result), sep='    ')

print('Максимальное значение функции: ' + str(max(y1)))
print('Минимальное значение функции: ' + str(min(y1)))