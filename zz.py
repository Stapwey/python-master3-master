import math


def main(a, b, n):
    result = 0
    result1 = 1
    result2 = 0
    for j in range(1, n + 1):
        for c in range(1, b + 1):
            for i in range(1, a + 1):
                result2 += 76 * (c ** 2 + i ** 3) ** 7 + 52 *\
                    (math.sqrt(i ** 3 + 1 + 99 * j) ** 6)
            result1 *= result2
            result2 = 0
        result += result1
        result1 = 1
    return result


print(main(7, 2, 5))
main(6, 8, 6)