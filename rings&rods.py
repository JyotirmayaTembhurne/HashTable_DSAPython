class Solution:
    def countPoints(self, rings: str) -> int:
        pair = {}
        for i in range(1, len(rings), 2):
            if (rings[i]) in pair.keys():
                pair[(rings[i])].add(rings[i - 1])
            else:
                pair[(rings[i])] = set()
                pair[(rings[i])].add(rings[i - 1])
        count = 0
        for values in pair.values():
            if len(values) == 3:
                count += 1
        return count
