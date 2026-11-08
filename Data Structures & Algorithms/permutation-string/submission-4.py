class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1, c2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1

        m = 0
        for i in range(26):
            if c1[i] == c2[i]:
                m += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if m == 26:
                return True

            ri = ord(s2[r]) - ord('a')
            c2[ri] += 1
            if c1[ri] == c2[ri]:
                m += 1
            elif c1[ri] + 1 == c2[ri]:
                m -= 1

            li = ord(s2[l]) - ord('a')
            c2[li] -= 1
            if c1[li] == c2[li]:
                m += 1
            elif c1[li] - 1 == c2[li]:
                m -= 1

            l += 1

        return m == 26