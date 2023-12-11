'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

class Solution:
    def deleteDuplicates(self, head: list) -> list:
        return list(set(head))
    
res = Solution()
print(res.deleteDuplicates([1,1,2]))
print(res.deleteDuplicates([1,1,2,2,2,5,5,9]))