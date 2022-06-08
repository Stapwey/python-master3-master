import math


def main(n):
    res = 0
    for i in range(1, len(n)+1):
        b1 = 71 * (n[math.ceil(i/3)]) ** 2
        b2 = 69 * (n[len(n)-math.ceil(i/3)]) ** 3
        res = res + (0.01-b1-b2)**2
    return (29 * res)


print(main([0.52, -0.24, 0.48, 0.22, -0.52, -0.78, 0.87, 0.6]))



