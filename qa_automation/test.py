a = [10,11,12]

def add(l: list) -> list:
    a.append(11)
    return a

g = add(a)
print(g)

