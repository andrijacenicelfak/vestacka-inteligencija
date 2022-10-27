def izmeni(l1):
    l2 = l1.copy()
    for x in range(len(l2)):
        if (x == 0):
            continue
        else:
            l2[x] = l2[x-1] + l2[x]
    return l2


print(izmeni([1, 2, 3, 4, 5]))
