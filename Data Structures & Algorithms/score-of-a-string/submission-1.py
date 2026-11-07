class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[x]) - ord(s[x-1])) for x in range(1,len(s)))
        