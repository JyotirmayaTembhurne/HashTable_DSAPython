class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hmap = dict()
        newmap = dict()
        temp = list()
        length = len(s)
        # Make an initial hmap
        for i in range(length):
            if s[i] in hmap.keys():
                hmap[s[i]].append(i)
            else:
                hmap[s[i]] = sorted(list())
                hmap[s[i]].append(i)
        # Now make a newmap to eliminate all entries with len(values)<1
        for key, value in hmap.items():
            if len(value) > 1:
                newmap[key] = value
        # Here, we are replacing the values with the second occurances of the respective keys
        for key, value in newmap.items():
            newmap[key] = value[1]
        occ = min(newmap.values())
        for key, value in newmap.items():
            if value == occ:
                return key
