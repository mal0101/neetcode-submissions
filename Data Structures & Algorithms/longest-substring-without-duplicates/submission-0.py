class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = []
        max_len = 0
        for c in s:
            if c not in s_list:
                s_list.append(c)
            else:
                s_list = s_list[s_list.index(c) + 1:]
                s_list.append(c)
            if len(s_list) > max_len:
                max_len = len(s_list)
        return max_len