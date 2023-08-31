class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return -1
        else:
            potential_nums = set()
            for i in range(length):
                if -nums[i] in nums:
                    potential_nums.add(abs(nums[i]))
            if len(potential_nums) == 0:
                return -1
            else:
                return max(potential_nums)
