class Solution(object):
    def reversePairs(self, nums):
        def mergeAndCount(left, right):
            i, j = 0, 0
            merged = []
            count = 0

            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    count += len(left) - i
                    j += 1
                else:
                    i += 1

            merged.extend(sorted(left + right))

            return merged, count

        def mergeSortAndCount(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2
            left, countLeft = mergeSortAndCount(nums[:mid])
            right, countRight = mergeSortAndCount(nums[mid:])
            merged, countMerge = mergeAndCount(left, right)

            return merged, countLeft + countRight + countMerge

        _, count = mergeSortAndCount(nums)
        return count
