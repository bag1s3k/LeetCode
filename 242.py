from collections import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def counter(word):
            hash_table = dict()

            for char in word:
                if char not in hash_table:
                    hash_table[char] = 0
                hash_table[char] += 1

            return hash_table
        
        if counter(s) == counter(t):
            return True
        else:
            return False

        
    
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        sc = Counter(s)
        tc = Counter(t)

        return True if sc == tc else False
    
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
            
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        array = [0] * 26

        for char in s:
            index = ord(char) - ord("a")

            array[index] += 1
        
        for char in t:
            index = ord(char) - ord("a")

            array[index] -= 1

        if len(set(array)) == 1:
            return True
        else:
            return False

solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
