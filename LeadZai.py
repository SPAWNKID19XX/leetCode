class Paginator():
    def __init__(self, current_page = 0, total_pages=0, boundaries=0, around=0 ) -> None:
        self.current_page = current_page
        self.total_pages=total_pages
        self.boundaries=boundaries
        self.around=around

    def __str__(self, arr=[]):
        return self.current_page, self.total_pages, self.boundaries, self.around 
    
    def calc_paginator(self):
        res = []
        for i, obj in enumerate(range(1, self.total_pages+1)):
            #case description to append values to list
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
                #add ... if it necessary
                if res[-1] != '...':
                    res.append('...')             
        return res
    

pgntor1 = Paginator(4, 5, 1, 0)
print(' '.join(pgntor1.calc_paginator()))

pgntor2 = Paginator(4,10,2,2)
print(' '.join(pgntor2.calc_paginator()))

#adicional test
pgntor3 = Paginator(10,25,5,2)
print(' '.join(pgntor3.calc_paginator()))



import unittest

class TestPaginator(unittest.TestCase):
    #SetUp
    def setUp(self):
        self.current_page = 4
        self.total_pages = 5
        self.boundaries = 1
        self.around = 0

    
    #Input Existense
    def test_current_page_Exist(self):
        self.assertIsNotNone(self.current_page)
    
    def test_total_pages_Exist(self):
        self.assertIsNotNone(self.total_pages)

    def test_boundaries_Exist(self):
        self.assertIsNotNone(self.boundaries)

    def test_around_Exist(self):
        self.assertIsNotNone(self.around)

    #Input Validator
    def test_curent_page_is_valid(self):
        return self.assertIsInstance(self.current_page, int)
    
    def test_total_pages_is_valid(self):
        self.assertIsInstance(self.total_pages,  int)

    def test_boundaries_is_valid(self):
        self.assertIsInstance(self.boundaries, int)

    def test_around_is_valid(self):
        self.assertIsInstance(self.around, int)
        # 0
    def test_curent_page_greater_O(self):
        self.assertGreater(self.current_page, 0)

    def test_total_pages_greater_O(self):
        self.assertGreater(self.total_pages, 0)
        
        
        #less or equal
    def test_curent_page_less_equal_total_page(self):
        self.assertLessEqual(self.current_page, self.total_pages)


#if __name__ == '__main__':
#    unittest.main()

