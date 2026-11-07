class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        j = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                j = i + 1

        return len(s) - j