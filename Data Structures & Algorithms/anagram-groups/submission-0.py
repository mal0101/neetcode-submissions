class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashagram = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            hashagram[sorted_s].append(s)
        return list(hashagram.values())