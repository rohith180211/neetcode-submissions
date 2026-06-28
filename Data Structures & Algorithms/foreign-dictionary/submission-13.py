import heapq
from typing import List, Set

class Solution:
    def compare(self, word1: str, word2: str, indegree: List[int], ls: List[Set[str]]) -> None:
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                u = ord(word1[i]) - ord('a')
                v = ord(word2[j]) - ord('a')

                if word2[j] not in ls[u]:
                    ls[u].add(word2[j])
                    indegree[v] += 1

                break

            i += 1
            j += 1

    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        present = [0] * 26
        indegree = [0] * 26

        for word in words:
            for ch in word:
                present[ord(ch) - ord('a')] = 1

        ls = [set() for _ in range(26)]

        for i in range(1, n):
            if len(words[i - 1]) > len(words[i]) and words[i - 1].startswith(words[i]):
                return ""

            self.compare(words[i - 1], words[i], indegree, ls)

        heap = []

        for i in range(26):
            if indegree[i] == 0 and present[i] == 1:
                heapq.heappush(heap, chr(i + ord('a')))

        res = ""

        while heap:
            ch = heapq.heappop(heap)
            res += ch

            for neigh in ls[ord(ch) - ord('a')]:
                indegree[ord(neigh) - ord('a')] -= 1

                if indegree[ord(neigh) - ord('a')] == 0:
                    heapq.heappush(heap, neigh)

        count = 0
        for i in range(26):
            if present[i] == 1:
                count += 1

        if len(res) < count:
            return ""

        return res