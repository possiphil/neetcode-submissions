class Solution:
    def anagram(self, s: str) -> List[int]:
        res = [0] * 26

        for c in s:
            res[ord(c) - ord('a')] += 1

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            map[tuple(self.anagram(s))].append(s)

        return list(map.values())
        