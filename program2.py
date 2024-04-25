class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total


solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("XIV"))   # Output: 14
print(solution.romanToInt("X"))   # Output: 10

