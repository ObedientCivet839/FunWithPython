### PROBLEM STATEMENT
# https://leetcode.com/problems/maximum-gap/

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

# Example 1:
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

# Example 2:
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

# Attempt 1: If the range of value is small, just create a boolean array of the value range
# Iterate through the input array and mark the value at each index.

# Attempt 2: Use HashMap or other data structures.
# This won't work since the best thing we can do is O(nlogn) performance for searching/sorting

# Solution:
# https://www.geeksforgeeks.org/maximum-adjacent-difference-array-sorted-form/
# https://www.geeksforgeeks.org/pigeonhole-sort/
#
# Idea:
# - (Similar to storing every item on a long array of with value range)
# - Find the new index in the bucket
# - Keep 2 buckets (max_bucket and min_bucket)
#   - max_bucket keeps the largest value in that bucket
#   - min_bucket keeps the smallest value in that bucket
# - The final result is the difference between the max of the previous bucket 
# and the min of the next bucket
#
# Runtime: O(N)
#   - Only store O(N)
#   - Run through multiple times, but only linear
import math

class Solution:
    def maximum_map(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            # No gaps for empty or single-item arrays
            return 0
        # math.inf
        N = len(nums)
        min_val, max_val = nums[0], nums[0]
        for v in nums:
            min_val = min(min_val, v)
            max_val = max(max_val, v)
        min_bucket = [math.inf] * N
        max_bucket = [-math.inf] * N
        val_range = max_val - min_val

        def bucket_index(v: int) -> int:
            # int is doing the flooring
            return int((v - min_val) / val_range * (N - 1))

        for n in nums:
            # New index
            ni = bucket_index(n)
            max_bucket[ni] = max(max_bucket[ni], n)
            min_bucket[ni] = min(min_bucket[ni], n)

        def fill_bucket(bucket: list[int]):
            prev_val = bucket[0]
            for i in range(1, len(bucket)):
                if bucket[i] == math.inf or bucket[i] == -math.inf:
                    bucket[i] = prev_val
                else:
                    prev_val = bucket[i]

        fill_bucket(min_bucket)
        fill_bucket(max_bucket)

        print(max_bucket)
        print(min_bucket)

        max_gap = 0
        for i in range(1, N):
            max_gap = max(max_gap, min_bucket[i] - max_bucket[i-1])
        return max_gap


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
                nums=[3,6,9,1],
                expected=3
            ),
            TestCase(
                name="2",
                nums=[10],
                expected=0
            ),
            TestCase(
                name="3",
                nums=[7, 64, 2, 10, 25, 30],
                expected=34
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.maximum_map(tc.nums)
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