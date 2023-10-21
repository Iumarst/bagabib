def tpl_sort(x):
    for f in x:
        if not isinstance(f, int):
            return ()
    return tuple(sorted(x))
print(tpl_sort((6, 21, 5, 2, 7.345)))
print(tpl_sort((8, 5.7, 5, 3.79, 18)))