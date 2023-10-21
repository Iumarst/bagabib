def sieve(ussr):
    x = []
    [x.append(item) for item in reversed(ussr) if item not in x]
    return tuple(x)
print(sieve([0, 2, 3, 2, 8, 7.34]))
print(sieve([2, 6, 7, 2, 3, 12, 5, 1, 9, 0]))
print(sieve((1, 2, 10, 6, 3, 9, 7.98, 4, 6, 14)))
print(sieve((1, 9, 5, 10, 4, 9, 3.79, 17,)))