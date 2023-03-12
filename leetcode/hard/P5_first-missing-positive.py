### PROBLEM STATEMENT
# https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# Attempt 1:
# Assumption: 231*2 is constant space
# First pass: min, max, ignore negatives
# Idea: Use bit array (bool)
# Second pass: Set array new_idx = A[i] - min
# B[new_index] = 1
# [min, ......, max]
# Third pass: Go over array, check missing 

# Attempt 2:
# Use nums.length < 105
# Array: bool[105], start with min value


# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#

# Input: nums = [1,2,3,5,7,9]
# Output: 4
# minVal = 1
# maxVal = 9
# B = [True,True,True,False,True,False,True,False,True]

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Return the first missing positive 
        for i in range(len(nums)): 
            if nums[i] > 0: 
                if nums[i] - 1 not in nums[:i]: 
                    return nums[i] - 1 
        return len(nums)

    def firstMissingPositive_2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 1
        minVal, maxVal = 1000, -1000
        for n in nums:
            if n <= 0:
                continue
            minVal = min(minVal, n)
            maxVal = max(maxVal, n)
        if minVal > 1 or minVal < 1:
            return 1
        B = [False] * (maxVal - minVal + 1)
        for n in nums:
            if n <= 0:
                continue
            B[n - minVal] = True
        for i in range(len(B)):
            if not B[i]:
                return minVal + i
        return maxVal + 1

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
                nums = [1,2,0],
                expected = 3
            ),
            TestCase(
                name="2",
                nums = [3,4,-1,1],
                expected = 2
            ),
            TestCase(
                name="3",
                nums = [7,8.9,11,12],
                expected = 1
            ),
            TestCase(
                name="4",
                nums = [2],
                expected = 1
            ),
            TestCase(
                name="5",
                nums = [0],
                expected = 1
            ),
            TestCase(
                name="6",
                nums = [0,1,2],
                expected = 3
            ),
            TestCase(
                name="7",
                nums = [1,2,3,10,2147483647,9],
                expected = 4
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.firstMissingPositive(tc.nums)
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
    # main()
    unittest.main()