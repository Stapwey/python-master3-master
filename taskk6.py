
map = {"i":1, 1985:{"i":2, 2003:{
    "i":0, 1964:0, 2019:1, 1996:2}, 2015:3},1989:4,
       2005:{"i":0, 1964:{"i":3, "DYLAN":5, "SAGE":6}, 2019:7, 1996:{"i":2, 2003:8, 2015:9}}}


def main(arr):
    current = map[arr[1]]
    while (type(current) != int):
        current = current[arr[current["i"]]]
    return current


print(main([1964, 2005, 2003, 'SAGE']))
print(main([1964, 2005, 2015, 'DYLAN']))
print(main([1996, 1985, 2003, 'SAGE']))
print(main([2019, 1985, 2015, 'SAGE']))
