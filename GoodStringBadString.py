s = "abacbc"
# output = true
string = set(s)
print(string)
char_count = set()
for i in string:
    char_count.add(s.count(i))
print(len(char_count) == 1)
