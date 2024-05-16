class Paginator:
    
    def __init__(self, current_page, total_pages, boundaries, around):
        self.current_page = current_page if current_page > 0 else 1
        self.total_pages = total_pages if total_pages > 0 else 1
        self.boundaries = boundaries if boundaries >= 0 else 0
        self.around = around if around >= 0 else 0
        
    
    def get_main_pages_list(self):
        main_pages_list_res = set()
        for page in range(self.current_page - self.around, self.current_page + self.around + 1 ):
            if page > 0 and page <= self.total_pages :
                main_pages_list_res.add(page)
        return  main_pages_list_res 
    
    def get_boundaries_to_list(self):
        main_boundaries_list = set()
        for page in range(1, self.boundaries+1):
            main_boundaries_list.add(page)
        for page in range(self.total_pages - self.boundaries+1, self.total_pages +1):
            main_boundaries_list.add(page)
        return  main_boundaries_list 
    
    def get_final_list(self):
        return self.get_boundaries_to_list().union(self.get_main_pages_list())
         
    
    def __str__(self) -> str:
        get_final_list = list(self.get_final_list())
        if get_final_list[0] != 1:
            get_final_list.insert(0,'...')
        
        for index in range(len(get_final_list)-1):
            if get_final_list[index] != '...':
                is_correct = get_final_list[index] + 1 == get_final_list[index+1]
                if not is_correct:
                    get_final_list.insert(index+1, '...')
        
        if get_final_list[-1] != self.total_pages:
            get_final_list.append('...')

        res = ' '.join(map(str,get_final_list)).replace(' ... ', '...').replace(' ...', '...').replace('... ', '...')
        
        return res
                    
        

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
    assert paginator.get_main_pages_list() == {1,2,3,4}

def test_length_of_main_page_list_on_midle():
    paginator = Paginator(10,15,0,2)
    assert paginator.get_main_pages_list() == {8,9,10,11,12}     

def test_length_of_main_page_list_on_finish():
    paginator = Paginator(14,15,1,2)
    assert paginator.get_main_pages_list() == {12,13,14,15}   

def test_get_boundaries():
    paginator = Paginator(3,15,1,2)
    assert paginator.get_boundaries_to_list() == {1,15}  

def test_get_final_list():
    paginator = Paginator(3,15,1,2)
    assert paginator.get_final_list() == {1,2,3,4,5,15} 

def test_final_res():
    paginator = Paginator(2,10,0,1)
    assert paginator.__str__() == "1 2 3..."

def test_start_points():
    paginator = Paginator(5,10,0,1)
    assert paginator.__str__() == "...4 5 6..."

def test_final_points():
    paginator = Paginator(2,10,0,1)
    assert paginator.__str__() == "1 2 3..."




paginator = Paginator(9,10,4,1)
main_pages_list = paginator.__str__()
print(main_pages_list)

paginator = Paginator(5,10,0,1)
main_pages_list = paginator.__str__()
print(main_pages_list)