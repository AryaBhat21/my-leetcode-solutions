class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        ans = []

        while k > 0:
            maximum = -1
            word = ""
            for w in d:

                if d[w] > maximum:
                    maximum = d[w]
                    word = w

                elif d[w] == maximum and w < word:
                    word = w

            ans.append(word)
            del d[word]
            k -= 1

        return ans