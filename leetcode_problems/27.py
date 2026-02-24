from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for item in nums[:]:
            if item == val:
                nums.remove(item)
                nums.append("_")
            else:
                i += 1
        return i

solution = Solution()
print(solution.removeElement([3,2,2,3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))