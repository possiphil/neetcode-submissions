class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = i = 0

        while i < len(s):

            if s[i] == ' ':

                while i < len(s) and s[i] == ' ':
                    i += 1
                
                if i == len(s):
                    return cnt
                
                cnt = 0

            else:

                cnt += 1
                i += 1

        return cnt