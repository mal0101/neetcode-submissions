class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, val in c.items():
            if val != 1:
                return key