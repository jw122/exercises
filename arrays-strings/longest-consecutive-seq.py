# From zuoyuan's blog
class Solution:
    def longestConsecutive(self, num):
        dict = {x: False for x in num} # False means not visited
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr = i+1; lenright = 0
                while curr in dict:
                    lenright += 1; dict[curr] = True; curr += 1
                curr = i-1; lenleft = 0
                while curr in dict:
                    lenleft += 1; dict[curr] = True; curr -= 1
                maxLen = max(maxLen, lenleft+1+lenright)
        return maxLen