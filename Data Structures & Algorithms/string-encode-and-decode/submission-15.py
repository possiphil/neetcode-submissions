class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""

        for s in strs:
            r += str(len(s)) + "!" + s

        return r

    def decode(self, s: str) -> List[str]:
        r = []

        i = 0
        while i < len(s):
            c = 0
            j = 0
            while s[i+j] != "!":
                c = c * 10 + int(s[i+j])
                j += 1
            
            r.append(s[i+1+j:i+1+j+c])
            i += c + 1 + j
            
        return r