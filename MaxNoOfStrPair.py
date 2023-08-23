words = ["aa", "ab"]
pair = {}
for i in range(len(words)):
    j = i + 1
    if j < len(words) and words[i][::-1] in words[j : len(words)]:
        pair[words[i]] = words[i][::-1]
print(len(pair.values()))
