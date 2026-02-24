class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        return (high + 1) // 2 - (low // 2)

solution = Solution()
print(solution.countOdds(3, 7))
print(solution.countOdds(8, 9))