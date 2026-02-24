class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 1:
            return strs[0]
        if len(strs[0]) == 0:
            return ""

        i = 0
        while True:
            tmp = []
            for thing in strs:
                if len(thing) < 1 or len(thing) <= i:
                    return result
                tmp.append(thing[i])
            if len(set(tmp)) > 1:
                return result
            else:
                result += tmp[0]
            i += 1

        return result
                
        

solution = Solution()
print(f"{solution.longestCommonPrefix(["flower","flow","flight"])!r}")
print(f"{solution.longestCommonPrefix(["dog","racecar","car"])!r}")
print(f"{solution.longestCommonPrefix(["a"])!r}")
print(f"{solution.longestCommonPrefix(["", ""])!r}")
print(f"{solution.longestCommonPrefix(["a", ""])!r}")
print(f"{solution.longestCommonPrefix(["ab", "a"])!r}")
print(f"{solution.longestCommonPrefix(["flower","flower","flower","flower"])!r}")