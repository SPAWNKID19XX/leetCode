'''

Все натуральные числа от 1 до 1000 включительно выписали в следующем порядке: сначала были выписаны в порядке возрастания числа с суммой цифр 1, 
затем в порядке возрастания числа с суммой цифр 2, потом в порядке возрастания числа с суммой цифр 3 и т. д. На каком месте оказалось число 996?


All natural numbers from 1 to 1000 inclusive were written in the following order: first, numbers were written in ascending order with a digit sum of 1, 
then in ascending order with a digit sum of 2, 
then in ascending order with a digit sum of 3, and so on. At which position did the number 996 appear?

'''


full_list = []
for i in range(1, 11):
    for j in range(1,11):
        print(i, j)