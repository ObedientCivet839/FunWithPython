### PROBLEM STATEMENT
# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        N = len(nums)
        # check minimum length
        if N <= 3:
            return sum(nums)
        nums = sorted(nums)
        
        # check if target is smaller than smallest elements or larger than the largest elements
        if sum(nums[:3]) > target:
            return sum(nums[:3])
        if sum(nums[-3:]) < target:
            return sum(nums[-3:])
        
        res = sum(nums[:3])
        
        for i in range(N-2):
            s, e = i + 1, N - 1
            while s < e:
                curr = nums[i] + nums[s] + nums[e]
                if abs(target - curr) < abs(target - res):
                    res = curr
                if curr == target:
                    return target
                if curr < target:
                    s += 1
                else:
                    e -= 1
        return res


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
            target: int
            expected: int

        testcases = [
            TestCase(
                name="1",
                nums = [-1,2,1,-4],
                target=1,
                expected =2 
            ),
            TestCase(
                name="2",
                nums = [0,0,0],
                target=1,
                expected=0
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.threeSumClosest(tc.nums, tc.target)
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