def main(a, b, x):
    res1 = 1
    temp = 0
    for k in range(1, b+1):
        for i in range(1, a+1):
            temp1 = 1 - 40*(k**4)
            temp2 = (x**2)/95
            temp3 = 38*i
            temp4 = 23*(temp2+temp3)**2
            temp5 = temp1 - temp4
            temp += temp5
        res1 *= temp
        temp = 0
        res = res1
    return res


print(main(8, 7, 0.91))

