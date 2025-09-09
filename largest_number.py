'''
Task
Implement the function find_largest(numbers) that returns the largest number from the list numbers.
    The input numbers is a list of integers.
    The list always contains at least one element.
'''
from redis.commands.search.reducers import count
from reportlab.lib.utils import rawBytes


class Solution():
    def find_largest(self, arr: list) -> int:
        max_number = arr[0]
        for i in range(1, len(arr)):
            if max_number < arr[i]:
                max_number = arr[i]

        return max_number
res = Solution()
print(res.find_largest([2,4,6,9,1,44,5]))