class Solution(object):
    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[0]

        # Move slow and fast pointers to detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Reset fast to the first element
        fast = nums[0]

        # Move fast and slow pointers to find the repeated number
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
