# Output= False
# num[0] = '1'. The digit 0 occurs 1ce in num.
# num[1] = '2'. The digit 1 occurs twice in num.
# num[2] = '1'. The digit 2 occurs once in num.
# num[3] = '0'. The digit 3 occurs zero times in num.
# The condition holds true for every index in "1210", so return true.
length = len(num)
result = True
for i in range(length):
    digit_count = num.count(str(i))
    expected_count = int(num[i])
    print(expected_count, digit_count)
    if digit_count != expected_count:
        result = False
print(result)
