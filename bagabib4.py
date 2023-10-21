def del_from_tuple(x, v):
    ussr = list(x)
    if v in x:
        ussr.remove(v)
    return tuple(ussr)
print(del_from_tuple((4, 5, 3), 8))
print(del_from_tuple((3, 9, 8, 4.54, 6), 7))
print(del_from_tuple((1, 3, 10, 6.9, 9, 3), 8))
print(del_from_tuple((0, 12.7, 6, 19, 0, 7), 0))