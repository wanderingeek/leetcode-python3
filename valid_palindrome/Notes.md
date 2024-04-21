Original: https://leetcode.com/problems/valid-palindrome/solutions/5056369/simple-2-line-python3-solution-beats-91-on/

# Intuition
We simply remove the unwanted characters from the string, convert to lowercase, and reverse the string and then compare to the original.

# Approach
- Import the Python Regex module
- Convert input string to lowercase
- Use it remove the unwanted characters, which are all characters excluding letters and numbers
- Now that we have the *cleaned* input string, compare it to the reversed version of itself, and return the result.

# Complexity
- Time complexity:
    $$O(n)$$
    Note: This excludes the time taken by the Python Regex module(`re`) to match and substitute the unwanted characters from the input string.
    This [StackOverflow answer](https://stackoverflow.com/a/21702/2627137) says its $$O(2^m + n)$$, where m is length of regex string, and n is length of input string

    Reversing the string is an O(n) operation. And so is string comparison.
    Therefore overall complexity exhibits linear growth along with size of input.

- Space complexity:
    $$O(n)$$

# Code
```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub('[^a-z0-9]','',s.lower())
        return s_clean==s_clean[::-1]
```