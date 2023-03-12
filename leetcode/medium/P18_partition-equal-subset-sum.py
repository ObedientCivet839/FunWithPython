### PROBLEM STATEMENT
# https://leetcode.com/problems/partition-equal-subset-sum

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        s = int(sum_nums / 2)
        # Create a matrix M[i][j]
        # i: store the index of the element in the list
        # j: store the sum at that position
        C = s + 1
        R = len(nums) + 1
        M = [[ False for c in range(C) ] for r in range(R) ]
        # set the 1st column to True
        # i.e. for sum of 0, any index would work
        for r in range(R):
            M[r][0] = True

        for i in range(1, R):
            for j in range(1, C):
                # We can either take the item or not
                # BUG 1: If I don't set this, then it might not set if the condition is not met
                M[i][j] = M[i-1][j]
                if j - nums[i - 1] >= 0:
                    M[i][j] = M[i][j] or M[i-1][j - nums[i - 1]]
        
        # We just need to find a subset that sums to half a sum,
        # because it's guaranteed that the rest will sum to half.
        return M[R-1][C-1]

# M2: DFS with cache
class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        target = sum(nums) // 2
        @cache
        def dfs(i : int, pathsum : int) -> bool:
            nonlocal target
            if pathsum == target:
                return True
            if i == len(nums) - 1 or pathsum > target:
                return False
            result = (dfs(i+1, pathsum + nums[i+1]) or dfs(i+1, pathsum))
            return result
        
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(0, 0)

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
            expected: bool

        testcases = [
            TestCase(
                name="a",
                nums=[1,5,10,6],
                expected=True,
            ),
            TestCase(
                name="0",
                nums = [1,2,3],
                expected = True,
            ),
            TestCase(
                name="1",
                nums = [1,5,11,5],
                expected = True,
            ),
            TestCase(
                name="2",
                nums = [1,2,3,5],
                expected = False,
            ),
            TestCase(
                name="3",
                nums=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97],
                expected=False,
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.canPartition(tc.nums)
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