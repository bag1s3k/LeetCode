from typing import List
from collections import Counter
import heapq

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for n in nums:
            if n not in hashmap:
                hashmap[n] = nums.count(n)

        print(hashmap)

        ks = sorted(hashmap.values(), reverse=True)[:k]
        print(ks)

        final = []
        for k,v in hashmap.items():
            if v in ks:
                final.append(k)

        return final

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        print(f"Count: {count}")
        

        for n, c in count.items():
            freq[c].append(n)
        print(f"Freq: {freq}")

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq. nlargest(k, count.keys(), key=count.get)

        
solution = Solution()

print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))