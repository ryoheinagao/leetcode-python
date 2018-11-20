#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.36%)
# Total Accepted:    190.9K
# Total Submissions: 697.8K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#
import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=[]

        if n < 2:
            return 0

        for i in range(2, n):
            isPrime = False
            if not primes:
                primes.append(i)
                continue
            
            for prime in primes:
                if i % prime == 0:
                    isPrime = False
                    break
                elif prime > math.sqrt(i):
                    isPrime = True
                    break
            
            if isPrime:
                primes.append(i)

        return len(primes) 