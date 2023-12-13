a = [1,2,3,4,5,6,7,8,9,0]

print(list(x for x in a if x%2==0))

def f(a: list)->list:
    return list(x for x in a if x%2==0)

print(f(a))
