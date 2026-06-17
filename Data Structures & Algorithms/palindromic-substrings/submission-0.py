class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Odd length palindromes
            low = i
            high = i

            while low >= 0 and high < len(s) and s[low] == s[high]:
                count += 1
                low -= 1
                high += 1

            # Even length palindromes
            low = i
            high = i + 1

            while low >= 0 and high < len(s) and s[low] == s[high]:
                count += 1
                low -= 1
                high += 1

        return count