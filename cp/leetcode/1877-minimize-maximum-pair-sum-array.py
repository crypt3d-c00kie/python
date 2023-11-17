class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        nLen = len(nums)
        minmaxpairSum = 0

        for i in range(nLen // 2):
            currentpairSum = nums[i] + nums[nLen - 1- i]
            minmaxpairSum = max(minmaxpairSum, currentpairSum)

        return minmaxpairSum