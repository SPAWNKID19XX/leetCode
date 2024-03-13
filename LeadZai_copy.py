'''
First Review
DONE - ⭐⭐⭐⭐★ Algorithm adequacy: Code returns incorrect values for a few edge cases.

Here is an example of unexpected behaviour we discovered:

Paginator(current_page=5, total_pages=10, boundaries=0, around=1).print_paginator() returns "1 ... 4 5 6 ... 10" instead of returning "... 4 5 6 ..."

DONE - ⭐⭐★★★ Algorithm efficiency: very inefficient

Code requires extremely large amounts of memory for large values of total_pages, despite being explicitly requested to make sure it runs efficiently regardless of the total pages’ number.

DONE - ⭐⭐⭐⭐★ Code readability: Mostly intuitive algorithm.

The majority of the algorithm is reasonably simple and intuitive.

Almost all variable and function names are self-explanatory.

“res“ and “obj“ variable names can lead to confusion, try to find a name that properly reflects its contents

When using typing, remember to add functions return types and its arguments types.

DONE - ⭐⭐★★★ Unit testing: Some edge cases were tested

Although some tests were written for the main functionality, very few edge cases were tested, which may result in some bugs not being discovered. Care was not taken to test the examples described in the exercise.

Tests have multiple asserts in the same test function. Should the code fail, the programmer will receive the feedback of all failures grouped in an unintuitive, hard-to-read way, that makes them difficult to understand.

Note that, when printing your function results at runtime will not assert your function’s correct behaviour
'''

class Paginator():
    def __init__(self, current_page: int = 1, total_pages: int = 1, boundaries: int = 0, around: int = 0) -> None:
        if not isinstance(current_page, int):
            self.current_page = 1
        else:
            self.current_page = current_page
        if not isinstance(total_pages, int):
            self.total_pages = self.current_page + 1
        else:
            if total_pages < current_page:
                self.total_pages = self.current_page + 1
            else:
                self.total_pages = total_pages
        if not isinstance(boundaries, int):
            self.boundaries = 0
        else:
            self.boundaries = int(boundaries)
        if not isinstance(around, int):
            self.around = 0
        else:
            self.around = int(around)
    
    def add_points(self, pages=[]):
        for index in range(len(pages)-1):
            try:
                if int(pages[index+1]) - int(pages[index]) == 1:
                    pass
                else:
                    pages.insert(index + 1, '...')  # Insert '...' when pages are not consecutive
            except ValueError:
                pass

    def add_pages(self, start_page, finish_page, pages =  []):
        for page in range(start_page, finish_page+1):
            if not str(page) in pages:
                pages.append(str(page))
        
    def print_paginator(self):
        pages = []
        
        if self.boundaries > 0:
            if self.boundaries * 2 >= self.total_pages:
                self.add_pages(1, self.total_pages, pages)
                return ' '.join(pages)            
            #add pages at the beginning
            self.add_pages(1, min(self.boundaries, self.total_pages), pages)
            #add current page + arround
            self.add_pages(self.current_page - self.around, self.current_page + self.around, pages)
            #add pages to end
            self.add_pages(self.total_pages-self.boundaries+1, self.total_pages, pages)            
            self.add_points(pages)
        else:
            if self.current_page == 1 and self.total_pages == 1:
                pages.append(str(self.current_page))
            else:
                pages.append('...')
                self.add_pages(self.current_page - self.around, self.current_page + self.around, pages)
                pages.append('...')        
        return ' '.join(pages)



pgntor = Paginator(4, 5, 1, 0)
print(pgntor.print_paginator()) # 1 ... 4 5

pgntor = Paginator(4, 10, 2, 2)
print(pgntor.print_paginator()) # 1 2 3 4 5 6 ... 9 10

# adicional tests
pgntor = Paginator(10, 25, 5, 2)
print(pgntor.print_paginator())

pgntor = Paginator(5, 10, 0, 1)
print(pgntor.print_paginator())

pgntor = Paginator(1, 10, 5, 2)
print(pgntor.print_paginator())

pgntor = Paginator()
print(pgntor.print_paginator())

import unittest

class TestPaginator(unittest.TestCase):
    # SetUp
    def setUp(self):
        self.paginator = Paginator(4,5,1,0)

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

    def test_total_greater_curent(self):
        self.assertGreaterEqual(self.paginator.total_pages, self.paginator.current_page)

    # LeadZai Tests
    def test_4_5_1_0(self):
        self.assertEqual(self.paginator.print_paginator(), "1 ... 4 5")
    
    def test_4_10_2_2(self):
        self.paginator = Paginator(4,10,2,2)
        self.assertEqual(self.paginator.print_paginator(), "1 2 3 4 5 6 ... 9 10")
    
    def test_5_10_0_1(self):
        self.paginator = Paginator(5, 10, 0, 1)
        self.assertEqual(self.paginator.print_paginator(), "... 4 5 6 ...")
    
    #My tests
    def test_8_10_1_2(self):
        self.paginator = Paginator(8, 10, 1, 2)
        self.assertEqual(self.paginator.print_paginator(), "1 ... 6 7 8 9 10")

    
    def test_1_10_5_2(self):
        self.paginator = Paginator(1, 10, 5, 2)
        self.assertEqual(self.paginator.print_paginator(), "1 2 3 4 5 6 7 8 9 10")


if __name__ == '__main__':
    unittest.main()
