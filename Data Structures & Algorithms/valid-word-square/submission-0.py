class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            row = words[i]
            col = ""

            for j in range(len(words)):
                if i < len(words[j]):
                    col += words[j][i]

            if row != col:
                return False

        return True
