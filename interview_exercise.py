def foo(num:int) -> list:
    res = [x for x in range(0, num, 2) ]
    print(res)
    return res


def test(a:int, b:list):
    if a in b:
        print('True')
        return True
    else:
        print('False')
        return False

test(2, foo(12) )