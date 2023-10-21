x = 0
B = -1
def slicer(a, b):
    v = ussr = x   
    if b in a:
        v = a.index(b)
    if a.count(b) > 1:
        ussr = a.index(b, v + 1) + 1
    else:
        ussr = B
    return a[v:ussr]
print(slicer((1, 2, 4), 10))
print(slicer((1, 8, 3, 6, 8, 5, 7, 4), 13))
print(slicer((1, 2, 8, 9, 1, 4, 8), 10))