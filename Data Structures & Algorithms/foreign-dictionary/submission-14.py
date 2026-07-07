class Solution:

    def compare(self, word1: str, word2: str, indegree: List[int], graph: List[Set[int]]):
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                u = ord(word1[i]) - ord('a')
                v = ord(word2[j]) - ord('a')

                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[v] += 1

                break

            i += 1
            j += 1

    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        present = [0] * 26
        for word in words:
            for ch in word:
                present[ord(ch) - ord('a')] = 1

        indegree = [0] * 26
        graph = [set() for _ in range(26)]

        for i in range(1, n):
            prev_word = words[i - 1]
            curr_word = words[i]

            if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                return ""

            self.compare(prev_word, curr_word, indegree, graph)

        heap = []
        for i in range(26):
            if present[i] == 1 and indegree[i] == 0:
                heapq.heappush(heap, chr(i + ord('a')))

        res = ""

        while heap:
            ch = heapq.heappop(heap)
            res += ch

            u = ord(ch) - ord('a')
            for neigh in graph[u]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    heapq.heappush(heap, chr(neigh + ord('a')))

        count = sum(present)

        if len(res) == count:
            return res

        return ""