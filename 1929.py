from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


solution = Solution()

print(solution.getConcatenation([1, 2, 1]))
print(solution.getConcatenation([1, 3, 2, 1]))
