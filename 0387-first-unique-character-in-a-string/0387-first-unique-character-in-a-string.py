from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        char_count = Counter(s)

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1
