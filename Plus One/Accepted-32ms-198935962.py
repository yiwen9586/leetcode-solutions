# 
# Generated by fetch-leetcode-submission project on GitHub.
# https://github.com/gitzhou/fetch-leetcode-submission
# Contact Me: aaron67[AT]aaron67.cc
# 
# Plus One
# https://leetcode.com/problems/plus-one/
# 

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        leng = len(digits)
        if leng == 0:
            digits = [1]
        
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits += [0]
        else:
            digits[-1] += 1
        
        return digits


