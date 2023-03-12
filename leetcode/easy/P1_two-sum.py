### PROBLEM STATEMENT
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

### MAIN FUNCTIONS

def main():
    s = Solution()
    nums = [2,7,11,15]
    targets = 9
    res = s.twoSum(nums, targets)
    print(res)


import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_two_sum(self):
        @dataclass
        class TestCase:
            name: str
            nums: list[int]
            targets: int
            expected: list[int]

        testcases = [
            TestCase(
                name="1",
                nums = [2,7,11,15],
                targets = 9,
                expected = [0, 1]
            ),
            TestCase(
                name="2",
                nums = [3, 2, 4],
                targets = 6,
                expected = [1, 2]
            ),
            TestCase(
                name="3",
                nums = [3, 3],
                targets = 6,
                expected = [0, 1]
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.twoSum(tc.nums, tc.targets)
            self.assertListEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

if __name__ == '__main__':
    main()
    unittest.main()