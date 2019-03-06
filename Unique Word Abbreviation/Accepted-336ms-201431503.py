# 
# Generated by fetch-leetcode-submission project on GitHub.
# https://github.com/gitzhou/fetch-leetcode-submission
# Contact Me: aaron67[AT]aaron67.cc
# 
# Unique Word Abbreviation
# https://leetcode.com/problems/unique-word-abbreviation/
# 

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = {}
        self.list = {}
        for word in dictionary:
            N = len(word)
            if N > 2:
                abbr = word[0] + (str)(N - 2) + word[N-1]
            else:
                abbr = word
            self.dic.setdefault(abbr, []).append(word)
            self.list.setdefault(word, abbr)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) < 2:
            return True
        
        abbr = self.list.get(word, "")
        if abbr == "":
            N = len(word)
            abbr = word[0] + (str)(N - 2) + word[N-1]
            if abbr in self.dic:
                return False
            else:
                return True               
        else: 
            if len(self.dic.get(abbr)) > 1:
                return False
            else:
                return True
            


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
