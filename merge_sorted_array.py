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
        l1 = m - 1
        l2 = n - 1
        k = n + m - 1
        #insert a
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[k] = nums1[l1]
                l1 -= 1
            else:
                nums1[k] = nums2[l2]
                l2 -= 1
            k -= 1

        while l2 >= 0:
            nums1[k] = nums2[l2]
            k -= 1
            l2 -= 1

        return nums1


res = Solution()
print(res.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
print(res.merge([4,0,0,0,0,0],1, [1,2,3,5,6],5))
print(res.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(res.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
