class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        if len(setnums) == len(nums):
            return False
        return True