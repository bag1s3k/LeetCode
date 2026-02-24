from time import time

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        t1 = time()
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1+1:]):
                if n1 + n2 == target:
                    return [i1, i2+i1+1]
        return []

    def twoSun2ndVersion(self, nums: list[int], target: int) -> list[int]:
        ...



solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3,3], 6))
print(solution.twoSum([3,2,3], 6))