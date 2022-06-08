def main(n):
    if n == 0:
        return 0.22
    elif n == 1:
        return -0.07
    elif n >= 2:
        return main(n-1)**3 + main(n-2)/61


print(main(1))