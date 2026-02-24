from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while True:
            if len(nums) < i+2:
                return j

            if nums[i] == nums[i+1]:
                nums.pop(i)
                continue
            else:
                j += 1
                i += 1
        

solution = Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))