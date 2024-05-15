import pytest
class Paginator:
    def __init__(self, current_page, total_pages, boundaries, around):
        self.current_page = current_page
        self.total_pages = total_pages
        self.boundaries = boundaries
        self.around = around
        

def test_generate_paginator_existence():
    paginator = Paginator(4,5,1,0)
    assert paginator != None

