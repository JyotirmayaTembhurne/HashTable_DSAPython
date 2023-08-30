class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        import string

        alphabet_dist = dict()
        sLen = len(s)
        pair = dict()
        stack = list()
        for i in range(26):
            alphabet_dist[list(string.ascii_lowercase)[i]] = distance[i]
        for i in range(sLen):
            if s[i] not in stack:
                if i + 1 <= sLen:
                    pair[s[i]] = len(s[i + 1 : s.index(s[i], i + 1)])
                stack.append(s[i])
        pairLen = len(pair)
        for key, value in pair.items():
            if pair[key] != alphabet_dist[key]:
                return False
        return True
