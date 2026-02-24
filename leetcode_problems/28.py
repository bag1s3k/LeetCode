class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        haystack = haystack.split(needle)
        if len(haystack) <= 1:
            return -1
        else:
            return len(haystack[0])

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))