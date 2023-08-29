class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        untypeable = list()
        typeable = list()
        for word in text:
            is_untypeable = False
            for char in brokenLetters:
                if char in word:
                    untypeable.append(word)
                    is_untypeable = True
                    break
            if not is_untypeable:
                typeable.append(word)
        return len(typeable)
