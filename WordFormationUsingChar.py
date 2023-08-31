words = ["cat", "bt", "hat", "tree"]
chars = "atach"
Output = 6
result = list()
for word in words:
    for char in word:
        equal_count = True
        if word.count(char) > chars.count(char):
            equal_count = False
            break
    if equal_count:
        result.append(len(word))
print(sum(result) == Output)
