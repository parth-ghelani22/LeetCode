from math import log

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        while states ** pigs < buckets:
            pigs += 1
        return pigs