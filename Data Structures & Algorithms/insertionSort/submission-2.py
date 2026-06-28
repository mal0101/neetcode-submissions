# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
         l = len(pairs)
         if l == 0:
            return []
         intermediate_states = [list(pairs)]
         for i in range(1,l):
            temp = pairs[i]
            j = i - 1
            while (j >= 0 and pairs[j].key > temp.key):
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = temp
            intermediate_states.append(list(pairs))
         return intermediate_states