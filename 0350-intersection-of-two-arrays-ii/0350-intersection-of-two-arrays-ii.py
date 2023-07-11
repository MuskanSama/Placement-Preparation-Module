from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        freq = defaultdict(int)  # Dictionary to store the frequency of elements in nums1

        # Count the frequency of elements in nums1
        for num in nums1:
            freq[num] += 1

        result = []

        # Check if each element in nums2 exists in freq and add it to the result
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result
        