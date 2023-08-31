class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = int(len(candyType) / 2)
        len2 = len(set(candyType))
        if len2 <= 1:
            return 1
        if len2 < limit:
            return len2
        else:
            return limit
