class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        curr_streak = 1
        max_streak = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr_streak += 1
            else:
                max_streak = max(max_streak, curr_streak)
                curr_streak = 1
        return max(curr_streak, max_streak)
