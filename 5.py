import math


def main(y):
    summa = 0
    for i in range(0, 8): #всего 8 элементов
        summa += (0.01 - 71 * (y[i//3])**2 - 69 * (y[7 - i // 3])**3)**2#8-1
    return summa * 29


print(main([-0.21, -0.97, 0.34, -0.03, -0.01, 0.86, -0.65, 0.65]))
