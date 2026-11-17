class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i in range(len(words)):
            w1 = words[i]

            for j in range(len(words)):
                if j == i:
                    continue

                w2 = words[j]

                for k in range(len(w2)):
                    if w2[k:k+len(w1)] == w1:
                        res.add(w1)

        return list(res)
