class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        while val in nums:
            if val == nums[index]:
                nums.pop(index)
            else:
                index += 1
        print(nums, val)

a = Solution()
a.removeElement([2, 2, 2], 2)
