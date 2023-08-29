class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        pair1 = dict()
        pair2 = dict()
        length1 = len(nums1)
        length2 = len(nums2)
        keys1 = pair1.keys()
        keys2 = pair2.keys()
        result = list()
        for i in range(length1):
            if nums1[i][0] in keys1:
                pair1[nums1[i][0]].append(nums1[i][1])
            else:
                pair1[nums1[i][0]] = list()
                pair1[nums1[i][0]].append(nums1[i][1])
        for i in range(length2):
            if nums2[i][0] in keys2:
                pair1[nums2[i][0]].append(nums2[i][1])
            else:
                pair2[nums2[i][0]] = list()
                pair2[nums2[i][0]].append(nums2[i][1])
        for key, value in pair2.items():
            if key in keys1:
                pair1[key].append(value[0])
            else:
                pair1[key] = list()
                pair1[key].append(value[0])
        for key, value in pair1.items():
            pair1[key] = sum(value)
        pair1 = sorted(pair1.items())
        for i in pair1:
            result.append(list(i))
        return result
