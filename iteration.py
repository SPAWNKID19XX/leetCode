from datetime import datetime, timedelta
import time
l = ["a","b","c","d","e"]


def my_iteration(it: list):
    a = iter(it)
    print(a)
    try:
        while True:
            print(next(a))
    except StopIteration:
        print("finished".upper())
            
    

my_iteration(l)


    

class Car:

    w = 4
    
    def __init__(self, br):
        self.br = br
        
    @staticmethod
    def run():
        return "brrrrrrrr"
    
    @classmethod
    def set_w(cls, w):
        cls.w = w

    
    def __str__(self):
        return f"Brand: {self.br}, wheels: {self.w}"


car1 = Car('BMW')
print(car1, car1.run())
car2 = Car("Audi")
print(car2, car2.run())
Car.set_w(1)
car3 = Car('Kia')
print(car3)
print(car1, car1.run())


def my_decorator(func):
    def main_func():
        s = datetime.now()
        print('start func ot', s)
        func()
        time.sleep(2)
        print('finish func')
        f = datetime.now()
        print(f"{f-s} sec")
        return func() 
    return main_func


@my_decorator
def test_func():
    print("hello")

test_func()

def my_args_decorator(sec):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            s = datetime.now()
            print('start func ot', s)
            func(*args, **kwargs)
            print(f"sleeping {sec} seconds before call func")
            time.sleep(sec)

            print('finish func')
            f = datetime.now()
            print(f"{f-s} sec")
            return func()  
        return wrapper
    return my_decorator


@my_args_decorator(5)
def test1():
    print("hello test2")

test1()