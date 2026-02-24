from typing import List
from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            hashmap[key].append(string)

        return list(hashmap.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)

            if key not in ans:
                ans[key] = []

            ans[key].append(s)
        
        print(ans)
        return list(ans.values())

solution = Solution()

print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))