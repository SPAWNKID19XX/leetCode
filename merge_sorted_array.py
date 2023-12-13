'''class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return sorted(list(x for x in (nums1 + nums2) if x != 0))
    
'''

class Solution:
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(1, len(nums2)+1):
            if nums1[-i] == 0:
                if len(nums2)  < 1:
                    return sorted(nums1)
                nums1[-i] = max(nums2)
                nums2.remove(max(nums2))
        return sorted(nums1)
        
res = Solution()
#print(res.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
print(res.merge([1,2,3,0,0,0], 3, [2,5,6], 3))