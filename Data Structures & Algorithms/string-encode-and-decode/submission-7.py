from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[i] != "#":
                i += 1

            length = int(s[j:i])
            i += 1

            res.append(s[i:i + length])
            i += length

        return res