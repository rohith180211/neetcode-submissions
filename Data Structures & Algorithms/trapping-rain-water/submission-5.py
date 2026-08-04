from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        st = []
        res = 0

        for i in range(n):
            while st and height[i] > height[st[-1]]:
                curr = st.pop()

                if not st:
                    break

                nge = i
                pge = st[-1]

                width = nge - pge - 1
                bheight = min(height[nge], height[pge]) - height[curr]

                res += width * bheight

            st.append(i)

        return res