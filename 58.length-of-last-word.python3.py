#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.05%)
# Total Accepted:    226.4K
# Total Submissions: 706.4K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        if not s or not l:
            return 0
        return len(l[-1])
        
