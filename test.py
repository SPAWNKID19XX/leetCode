'''file = 'two_sum.py'
for x in open(file, 'r'):
    print(x)'''

'''class A():
    def __init__(self, v=2 ) -> None:
        self.v = v

    def set(self, v=1) -> int:
        self.v = v
        return self.v
    
a = A()
print(a.v)
b = a
print(a.v, b.v)
b.set()
print(a.v, b.v) '''

'''x = "\\\\"
print(len(x))'''

'''class A:
    A=1
    def __init__(self) -> None:
        self.a = 0

    print(hasattr(A, 'a'))'''

'''def g(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in g(2):
    print(x, end='')'''


'''input_num = input()
try:
    if input_num > 1:
        print('TRY 1')
    else:
        print('TRY 0')
except:
    if int(input_num) > 1:
        print('E1')
    else:
        print('E0')'''
'''s = open("two_sum.py", 'r')
print(s.read(1))

A = 1
a = 0

print(A,a)'''
'''try:
    raise Exception(1,2,3)

except Exception as e:
    print(len(e.args))'''


print(__name__)
numbers_with_sum_1 = []

for i in range(1, 1001):
    # Разбиваем число на цифры и суммируем их
    digit_sum = sum(map(int, str(i)))
    
    # Если сумма цифр равна 1, добавляем число в список
    if digit_sum == 1:
        numbers_with_sum_1.append(i)

print(numbers_with_sum_1)

numbers_with_sum_2 = []

for i in range(1, 1001):
    # Разбиваем число на цифры и суммируем их
    digit_sum = sum(map(int, str(i)))
    
    # Если сумма цифр равна 2, добавляем число в список
    if digit_sum == 2:
        numbers_with_sum_2.append(i)

print(numbers_with_sum_2)
