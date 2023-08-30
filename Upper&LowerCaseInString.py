s = "AbCdEfGhIjK"
Output = ""
valid = set()
if len(s) == 1:
    print("length of s is 1.")
else:
    for char in s:
        if char.lower() in s and char.upper() in s:
            valid.add(char.upper())
    if len(valid) == 0:
        print("Length of valid is 0.")
    else:
        print(max(valid), max(valid) == Output)
