class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        len1 = len(arr1)
        if len1 == 1:
            return arr1
        else:
            len2 = len(arr2)
            arr1.sort()
            arr3 = list()
            pair = dict()
            for i in range(len2):
                pair[arr2[i]] = arr1.count(arr2[i])
            for key, value in pair.items():
                i = 0
                while i < value:
                    arr3.append(key)
                    i += 1
            for i in range(len1):
                if arr1[i] not in arr3:
                    j = 0
                    while j < arr1.count(arr1[i]):
                        arr3.append(arr1[i])
                        j += 1
            return arr3
