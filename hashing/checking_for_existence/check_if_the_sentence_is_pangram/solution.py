class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Important: I can also use Set instead of Dictionary because it has the same time complexity as Dict.
        """
        characters = set()
        for s in sentence:
            characters.add(s)

        # print(characters)
        if len(characters) == 26:
            return True
        return False
