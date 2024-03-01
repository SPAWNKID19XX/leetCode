class Paginator():
    def __init__(self, current_page=1, total_pages=1, boundaries=0, around=0) -> None:
        if not isinstance(current_page, int):
            self.current_page = 1
        else:
            self.current_page = current_page
        if not isinstance(total_pages, int):
            self.total_pages = self.current_page + 1
        else:
            self.total_pages = int(total_pages)
        if not isinstance(boundaries, int):
            self.boundaries = 1
        else:
            self.boundaries = int(boundaries)

        if not isinstance(around, int):
            self.around = 1
        else:
            self.around = int(around)

    def print_paginator(self):
        res = []
        for i, obj in enumerate(range(1, self.total_pages + 1)):
            # case description to append values to list
            if (
                    obj == 1 or
                    obj == self.total_pages or
                    obj <= self.boundaries or
                    obj > self.total_pages - self.boundaries or
                    obj == self.current_page or
                    (obj < self.current_page and obj >= self.current_page - self.around) or
                    (obj > self.current_page and obj <= self.current_page + self.around)
            ):
                res.append(str(obj))
            else:
                # add ... if it necessary
                if res[-1] != '...':
                    res.append('...')
        return ' '.join(res)


pgntor1 = Paginator(4, 5, 1, 0)
print(pgntor1.print_paginator())

pgntor2 = Paginator(4, 10, 2, 2)
print(pgntor2.print_paginator())

# adicional tests
pgntor3 = Paginator(10, 25, 5, 2)
print(pgntor3.print_paginator())

pgntor4 = Paginator()
print(pgntor4.print_paginator())

import unittest


class TestPaginator(unittest.TestCase):
    # SetUp
    def setUp(self):
        self.paginator = Paginator('a', 5.5, 1, '/')

    # Input Existense
    def test_four_values_exist(self):
        self.assertIsNotNone(self.paginator.current_page)
        self.assertIsNotNone(self.paginator.total_pages)
        self.assertIsNotNone(self.paginator.boundaries)
        self.assertIsNotNone(self.paginator.around)

    # Input Validator
    def test_args_equal_O(self):
        self.assertNotEqual(self.paginator.current_page, 0)
        self.assertNotEqual(self.paginator.total_pages, 0)

    def test_not_int_char(self):
        self.assertIsInstance(self.paginator.current_page, int)
        self.assertIsInstance(self.paginator.around, int)
        self.assertIsInstance(self.paginator.total_pages, int)
        self.assertIsInstance(self.paginator.boundaries, int)

    def test_total_less_curent(self):
        self.assertGreater(self.paginator.total_pages, self.paginator.current_page)


if __name__ == '__main__':
    unittest.main()