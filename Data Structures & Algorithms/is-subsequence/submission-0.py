class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s):
            skip = False

            while j < len(t):
                if s[i] == t[j]:
                    i+=1
                    j+=1
                    skip = True
                    break
                else:
                    j+=1

            if not skip:
                return False

        return True
        