from typing import List, Tuple, Optional

### PROBLEM STATEMENT
# https://leetcode.com/problems/prime-in-diagonal/

# You are given a 0-indexed two-dimensional integer array nums.

# Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

# Note that:

# An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
# An integer val is on one of thediagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1]= val.

# In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

# Example 1:

# Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
# Output: 11
# Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
# Example 2:

# Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
# Output: 17
# Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.


# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            num = nums[i][i]
            if self.checkPrime(num):
                res = max(res, num)
        for i in range(N):
            num = nums[i][N-1-i]
            if self.checkPrime(num):
                res = max(res, num)
        return res
    
    # BUG 1: Need a faster way  to check sum
    def checkPrime1(self, num):
        if num <= 1:
            return False
        if num < 4:
            return True
        # IMPORTANT: only need to check to square root of x
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = len(nums)
        res = 0
        self.isPrime = {}
        for i in range(4):
            self.isPrime[i] = True
        
        diag = set()
        for i in range(N):
            diag.add(nums[i][i])
        for i in range(N):
            diag.add(nums[i][N-1-i])
        diag = sorted(list(diag), reverse=True)
        for num in diag:
            if self.checkPrime(num):
                return num
        return 0
    
    def checkPrime(self, num):
        if num <= 1:
            return False
        if num < 4:
            return True
        if num in self.isPrime:
            return self.isPrime[num]
        for i in range(2, num+1):
            if i in self.isPrime and not self.isPrime[i]:
                continue
            # fill all multiples of primes
            self.isPrime[i] = True
            for j in range(2, num//i + 1):
                self.isPrime[i * j] = False
        return self.isPrime[num]    
        
    

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            nums: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                nums = [0],
                expected = 0
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.X(tc.nums, tc.targets)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    print(s)

if __name__ == '__main__':
    main()
    unittest.main()