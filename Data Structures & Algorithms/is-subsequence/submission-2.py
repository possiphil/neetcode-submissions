class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = [[-1] * len(t) for _ in range(len(s))]

        def rec(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            if memo[i][j] != -1:
                return memo[i][j] == 1

            if s[i] == t[j]:
                memo[i][j] = 1 if rec(i+1, j+1) else 0
            else:
                memo[i][j] = 1 if rec(i, j+1) else 0
            
            return memo[i][j] == 1

        return rec(0, 0)
        