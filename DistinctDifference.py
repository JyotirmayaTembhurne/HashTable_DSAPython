class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = list()
        length = len(nums)
        for i in range(length):
            diff.append(len(set(nums[i::-1])) - len(set(nums[i + 1 :])))
        return diff
