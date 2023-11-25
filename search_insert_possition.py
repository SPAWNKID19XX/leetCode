'''

35. Search Insert Position
Solved
Easy
Topics
Companies

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



'''

from ast import List


class Solution:
    def searchInsert(self, nums, target) -> int:
        start_search = 0
        finish_search = len(nums)-1
        if target in nums:
            return nums.index(target)
        else:
            while finish_search - start_search > 1:
                midle = (finish_search + start_search) // 2
                print(midle)
                if target < nums[midle]:
                    finish_search = midle
                else:
                    start_search = midle
                print(start_search, finish_search)
            
            if target < nums[start_search]:
                return start_search
            elif target > nums[start_search] and target < nums[finish_search]:
                return finish_search
            else: 
                return finish_search + 1

a = Solution()
res = a.searchInsert([1,3,5,6], 7)
print('---',res)
res = a.searchInsert([1,3,5,6], 2)
print('---',res)
res = a.searchInsert([1,3,5,6], 5)
print('---',res)