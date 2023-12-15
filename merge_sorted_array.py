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
        
        for i in range(1, len(nums2)+1):
            if nums1[-i] == 0:
                if len(nums2)  < 1:
                    return sorted(nums1)
                nums1[-i] = max(nums2)
                nums2.remove(max(nums2))
        return sorted(nums1)
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1

        if p1 < 0:
            p1 = 0
        while p1 >= 0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2-=1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            print(nums1)
            p2 -= 1
            p -= 1
        return nums1



nums1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 0
nums2 = [-50,-50,-48,-47,-44,-44,-37,-35,-35,-32,-32,-31,-29,-29,-28,-26,-24,-23,-23,-21,-20,-19,-17,-15,-14,-12,-12,-11,-10,-9,-8,-5,-2,-2,1,1,3,4,4,7,7,7,9,10,11,12,14,16,17,18,21,21,24,31,33,34,35,36,41,41,46,48,48]
n = 63

        
res = Solution()
print(res.merge(nums1,m,nums2, n))
#print(res.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
#print(res.merge([4,0,0,0,0,0],1, [1,2,3,5,6],5))
#print(res.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
#print(res.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
#print(res.merge([1,2,3,0,0,0], 3, [2,5,6], 3))