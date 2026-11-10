class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(": ")", "[": "]", "{": "}"}
        q = deque()

        for c in s:
            if c in mp.keys():
                q.append(c)
            else:
                if not q or mp[q.pop()] != c:
                    return False
                
        return not q

        