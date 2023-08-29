s = "xyzzaz"
# Output: 1
gstring = list()
length = len(s)
for i in range(length - 2):
    if len(set(s[i : i + 3])) == 3:
        gstring.append(s[i : i + 3])
print(gstring, len(gstring))
