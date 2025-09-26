class TestDecorator():
    def inst_method(self):
        return f'{self}'

    @classmethod
    def lol1(cls, test):
        return cls

    @staticmethod
    def lol2(a,b):
        res = a+b
        return res


a = TestDecorator()
print(a.inst_method())
print(a.lol1('hello world'))
print(a.lol2(2,6))

print('+++++++++++++++++++++++++++++++++++++')

def gen_function(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


for obj in gen_function(5):
    print(obj)




print('+++++++++++++++++++++++++++++++++++++')
def is_palindrome(text):
    start, finish = 0, len(text)-1
    while start<finish:
        if text[start].lower() != text[finish].lower():
            return False
        start += 1
        finish -= 1
    return True

print(is_palindrome('казак'))
print(is_palindrome('Python'))

print('+++++++++++++++++++++++++++++++++++++')


a=[1,2,3,4,5,6,7,8,9,10]
b=[1,1,9,7,5,6,7,8,9,10]
c=[1,1,1,1,1,1,1,1,9,10]


def collection(l:list):
    dictionary = {}
    for obj in l:
        if obj not in  dictionary:
            dictionary[obj] = 1
        else:
            dictionary[obj] += 1
    return dictionary

print(collection(a))
print(collection(b))
print(collection(c))


import asyncio, aiohttp
async def foo():
    print("Начало foo")
    await asyncio.sleep(1)
    print("Конец foo")

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(foo())
    await task1
    await task2

asyncio.run(main())


l = [number for number in range(0, 101)]

async def async_def(l):
    i = 0
    new_list = []
    new_list.append(l[i])
    return new_list

a = async_def(l)
print(a)






