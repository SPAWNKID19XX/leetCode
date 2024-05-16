class Paginator:
    
    def __init__(self, current_page, total_pages, boundaries, around):
        self.current_page = current_page if current_page > 0 else 1
        self.total_pages = total_pages if total_pages > 0 else 1
        self.boundaries = boundaries if boundaries >= 0 else 0
        self.around = around if around >= 0 else 0
        self.main_pages_list_res = []
    
    def get_main_pages_list(self):
        
        for page in range(self.current_page - self.around, self.current_page + self.around+1 ):
            if page > 0 and page <= self.total_pages :
                self.main_pages_list_res.append(page)
        return  self.main_pages_list_res 
    
    def __str__(self) -> str:
        return f'{self.current_page} {self.total_pages} {self.boundaries} {self.around}'

def test_generate_paginator_existence():
    paginator = Paginator(4,5,1,0)
    assert paginator != None

def test_current_page_greatest_0():
    paginator = Paginator(0,5,1,0)
    assert paginator.current_page > 0

def test_total_pages_greatest_0():
    paginator = Paginator(4,0,1,0)
    assert paginator.total_pages > 0

def test_boundaries_greatest_0():
    paginator = Paginator(0,5,-1,0)
    assert paginator.boundaries >= 0

def test_around_greatest_0():
    paginator = Paginator(4,0,1,-1)
    assert paginator.around >= 0

def test_length_of_main_page_list_on_start():
    paginator = Paginator(1, 5,1,3)
    assert paginator.get_main_pages_list() == [1,2,3,4]

def test_length_of_main_page_list_on_midle():
    paginator = Paginator(10,15,0,2)
    assert paginator.get_main_pages_list() == [8,9,10,11,12]     

def test_length_of_main_page_list_on_finish():
    paginator = Paginator(14,15,1,2)
    assert paginator.get_main_pages_list() == [12,13,14,15]    

paginator = Paginator(1, 5,1,3)
main_pages_list = paginator.get_main_pages_list()
print(main_pages_list)