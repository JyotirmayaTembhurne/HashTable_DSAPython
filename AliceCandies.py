class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = frozenset(nums[i])
        intersection = list(frozenset.intersection(*nums))
        return sorted(intersection)
