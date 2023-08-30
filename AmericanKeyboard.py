string1 = "qwertyuiop"
string2 = "asdfghjkl"
string3 = "zxcvbnm"
words = [
    "asdfghjkla",
    "qwertyuiopq",
    "zxcvbnzzm",
    "asdfghjkla",
    "qwertyuiopq",
    "zxcvbnzzm",
]
expected = [
    "asdfghjkla",
    "qwertyuiopq",
    "zxcvbnzzm",
    "asdfghjkla",
    "qwertyuiopq",
    "zxcvbnzzm",
]
string1 = set(string1)
string2 = set(string2)
string3 = set(string3)
words_length = len(words)
pair = list()
valid = list()
for i in range(words_length):
    pair.append([words[i], set(words[i].lower())])
pair_length = len(pair)
for i in range(pair_length):
    if pair[i][1].issubset(string1):
        valid.append(pair[i][0])
    if pair[i][1].issubset(string2):
        valid.append(pair[i][0])
    if pair[i][1].issubset(string3):
        valid.append(pair[i][0])
print(valid == expected)
