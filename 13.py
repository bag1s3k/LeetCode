class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_key = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1_000
        }

        sum: int = 0
        last = roman_key["M"]
        for c in s:
            if roman_key[c] > last:
                sum += roman_key[c] - last*2
            else:
                sum += roman_key[c]
            last = roman_key[c]
        return sum

solution = Solution()
print(f"{solution.romanToInt("III")} - 3")
print(f"{solution.romanToInt("LVIII")} - 58")
print(f"{solution.romanToInt("MCMXCIV")} - 1994")