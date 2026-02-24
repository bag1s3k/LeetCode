from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            for index_j, j in enumerate(nums[index + 1:]):
                if i + j == target:
                    return [index, index_j + index + 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, value in enumerate(nums):
            sub = target - value

            if sub in hashmap and hashmap[sub] != index:
                return [index, hashmap[sub]]
            hashmap[value] = index
            
        return []

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
