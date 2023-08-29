lowLimit = 1234
highLimit = 1240
# Output: 1
string = list()
pair = dict()
result = list()
for i in range(lowLimit, highLimit + 1):
    if len(str(i)) == 1:
        string.append(i)
    else:
        digits = list()
        for char in str(i):
            digits.append(int(char))
        string.append(sum(digits))
boxes = list(set(string))
length = len(boxes)
for i in range(length):
    pair[i + 1] = string.count(boxes[i])
max_count = max(pair.values())
# print(pair)
print(max_count)
