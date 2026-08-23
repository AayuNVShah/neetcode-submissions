class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for i in range(len(nums)):
            if nums[i] in ht:
                return True
            ht[nums[i]]=1
        return False
        