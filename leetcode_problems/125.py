class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        s = s.lower()

        for i in range(len(s)):
            if s[i] != s[(i * -1) - 1]:
                return False
            
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        s = s.lower()

        return s == s[::-1]

solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))