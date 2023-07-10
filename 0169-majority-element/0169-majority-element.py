class Solution(object):
    def majorityElement(self, nums):
        
        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1

        return majority

        