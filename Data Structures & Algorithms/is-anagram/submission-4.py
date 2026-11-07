class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = dict()

        for c in s:
            h[c] = h.get(c, 0) + 1

        for c in t:
            h[c] = h.get(c, 0) - 1

        for v in h.values():
            if v != 0:
                return False

        return True