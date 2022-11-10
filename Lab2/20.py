def izracunaj(l1, fun):
    return [fun(l1[i], l1[i+1], l1[i+2]) for i in range(len(l1)-2)]


print(izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z))
