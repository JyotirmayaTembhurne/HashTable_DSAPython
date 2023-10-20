from operator import itemgetter

nums = [2, 3, 1, 3, 2]
Output = [1, 3, 3, 2, 2]
# Explanation: '3' has a frequency of 1,
# '1' has a frequency of 2, and
# '2' has a frequency of 3.
nums.sort(reverse=True)
numsLen = len(nums)
pair = dict()
result = list()
for i in range(numsLen):
    pair[nums[i]] = nums.count(nums[i])
pair = sorted(pair.items(), key=itemgetter(1))
pairLen = len(pair)
for item in pair:
    for i in range(item[1]):
        result.append(item[0])
print(result)
