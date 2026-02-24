from typing import List

class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0

        while True:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left + 1, right + 1]
            elif sum_ < target:
                left += 1
            elif sum_ > target:
                right -= 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            compliment = target - numbers[l] - numbers[r]

            if compliment > 0:
                l += 1
            elif compliment < 0:
                r -= 1
            else:
                return [l + 1, r + 1]
            
        return []


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))