from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = defaultdict(int)

        for c in s:
            h[c] += 1

        for c in t:
            h[c] -= 1

        for v in h.values():
            if v != 0:
                return False

        return True