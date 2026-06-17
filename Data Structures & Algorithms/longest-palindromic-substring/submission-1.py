class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        LPS = ""

        for i in range(len(s)):
            # Odd length palindrome
            low = i
            high = i

            while low >= 0 and high < len(s) and s[low] == s[high]:
                palindrome = s[low:high + 1]

                if len(palindrome) > len(LPS):
                    LPS = palindrome

                low -= 1
                high += 1

            # Even length palindrome
            low = i
            high = i + 1

            while low >= 0 and high < len(s) and s[low] == s[high]:
                palindrome = s[low:high + 1]

                if len(palindrome) > len(LPS):
                    LPS = palindrome

                low -= 1
                high += 1

        return LPS