import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub('[^a-z0-9]','',s.lower())
        return s_clean==s_clean[::-1]