def razlika(l1, l2):
    return list(filter(lambda x: x not in l2, l1))


def objedini(l1, l2):
    vm = list(map(lambda x: x, (l1, l2) if len(l1) > len(l2) else (l2, l1)))
    vm[1].extend([0]*(len(vm[0]) - len([vm[1]])))
    return list(map(lambda x, y: ((x, y) if x < y else (y, x)), vm[0], vm[1]))


print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))
print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))
