class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checkset = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in checkset:
                length = 0
                while (n + length) in checkset:
                    length += 1

                longest = max(length, longest)

        return longest