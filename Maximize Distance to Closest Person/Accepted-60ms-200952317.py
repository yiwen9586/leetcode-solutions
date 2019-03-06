# 
# Generated by fetch-leetcode-submission project on GitHub.
# https://github.com/gitzhou/fetch-leetcode-submission
# Contact Me: aaron67[AT]aaron67.cc
# 
# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# 

class Solution(object):    
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxDis = 0
        size = len(seats)
        list = []
        list.append(0)
        count = 0
        for i in range(0, size):            
            if seats[i] == 1:
                count += 1
                list.append(i)
                if count == 1:
                    maxDis = i
                else:
                    maxDis = max((list[count]-list[count-1])//2, maxDis)

        maxDis = max(size-1-list[count], maxDis)

        if maxDis == 0:
            return 1
        else:
            return maxDis
        
