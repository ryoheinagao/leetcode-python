#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (36.64%)
# Total Accepted:    250.9K
# Total Submissions: 684.8K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0
        for i in range(max(len(a), len(b))):
            v1 = int(a[len(a)-i-1]) if len(a) > i else 0
            v2 = int(b[len(b)-i-1]) if len(b) > i else 0
            s = carry+v1+v2
            if s == 3:
                res.append(1)
                carry = 1
            elif s == 2:
                res.append(0)
                carry = 1
            elif s == 1:
                res.append(1)
                carry = 0
            elif s == 0:
                res.append(0)
                carry = 0
        res.append(carry)
        if res[-1] == 0:
            res.pop()
        res.reverse()
        return ''.join(map(str, res))
