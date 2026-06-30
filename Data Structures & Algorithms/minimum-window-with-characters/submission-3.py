from collections import defaultdict
import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""

        mp = defaultdict(int)

        for ch in t:
            mp[ch] += 1

        i = 0
        count = 0
        minLen = sys.maxsize
        sIndex = 0
        m = len(t)

        for j in range(len(s)):
            mp[s[j]] -= 1

            if mp[s[j]] >= 0:
                count += 1

            while count == m:
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    sIndex = i

                mp[s[i]] += 1

                if mp[s[i]] > 0:
                    count -= 1

                i += 1

        if minLen == sys.maxsize:
            return ""

        return s[sIndex:sIndex + minLen]