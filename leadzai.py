import pytest
class Paginator:
    def __init__(self, current_page, total_pages, boundaries, around):
        self.current_page = current_page if current_page > 0 else 1
        self.total_pages = total_pages if total_pages > 0 else 1
        self.boundaries = boundaries if boundaries >= 0 else 0
        self.around = around if around >= 0 else 0
        

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