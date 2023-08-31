class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        length = len(emails)
        pair = dict()
        sum = int()
        for i in range(length):
            emails[i] = emails[i].replace(".com", "")
            if "+" in emails[i]:
                emails[i] = emails[i].replace(
                    emails[i][emails[i].index("+") : emails[i].index("@")], ""
                )
            temp = emails[i].split("@")
            temp[0] = temp[0].replace(".", "")
            if temp[1] in pair:
                pair[temp[1]].add(temp[0])
            else:
                pair[temp[1]] = set()
                pair[temp[1]].add(temp[0])
            temp = None
        for value in pair.values():
            sum += len(value)
        return sum
