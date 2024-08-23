class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        sum = 0
        maxLargest = -1
        length = len(nums[0])
        for i in range(length):
            maxLargest = 0
            for num in nums:
                num.sort()
                maxLargest = max(maxLargest, num.pop())
            sum += maxLargest
        return sum
            