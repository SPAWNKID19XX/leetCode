from xxlimited_35 import error


import pytest


class A:
    def add_a(self, s, f, l=[]):
        for x in range(s, f):
            l.append(str(x))

    def print_a(self):
        l = []
        self.add_a(1, 3, l)
        print(l)
        self.add_a(5, 8, l)
        return ' '.join(l)


a = A()
print(a.print_a())

logs = ["error", "info", "warning", "error", "debug", "info", "error"]


def get_logs_counter(logs: list) -> dict:
    res = {}
    for obj in logs:
        if obj not in res:
            res[obj] = 1
        else:
            res[obj] += 1
    return res


print(get_logs_counter(logs))


class Calc:
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("b should't be equal 0")


@pytest.fixture
def calc():
    return Calc()


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (2, 10, 0.2),
        (20**200, 2, error),
        ("a", 2, TypeError),
        (10, "a", TypeError),
        (0, 2, 0),
        (-1, 2, -0.5),
        (1, 2, 0.5),
        (10, 0, ZeroDivisionError),
        (10, -2, -5),
        (2, -10, -0.2),
    ]
)
def test_div(calc, a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc.div(a, b)
    else:
        assert calc.div(a, b) == pytest.approx(expected)


u_list = [
  {"id": 1, "name": "Alice", "age": 30},
  {"id": 2, "name": "Bob", "age": 25},
  {"id": 3, "name": "Charlie", "age": 35}
]

def g30_list(u_list: list)-> list:
    return [user['name'] for user in u_list if user['age']>30]


print(g30_list(u_list))