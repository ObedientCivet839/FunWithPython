### PROBLEM STATEMENT
# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution_M1:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda a: a[0])
        # print(intervals)
        if len(intervals) == 1:
            return intervals
        
        result = []
        while len(intervals) > 1:
            a = intervals[0]                
            b = intervals[1]
            if self.overlap(a, b):
                # if the intervals overlap, append the new interval back to the list
                intervals.pop(0)
                intervals.pop(0)
                c = [a[0], max(a[1],b[1])]
                intervals.insert(0, c)
            else:
                # skip a
                intervals.pop(0)
                result.append(a)
        result.extend(intervals)
        return result

    def overlap(self, a: list[int], b: list[int]) -> bool:
        """Returns True if a overlaps with b. Assume that a is BEFORE b."""
        return a[1] >= b[0]

# https://www.geeksforgeeks.org/merging-intervals/
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort the array on the basis of start values of intervals.
        intervals.sort()
        stack = []
        # insert first interval into stack
        stack.append(intervals[0])
        for i in intervals[1:]:
            # Check for overlapping interval,
            # if interval overlap
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                # Change the element in place
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)    
        return stack

### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: int
            intervals: list[list[int]]
            expected: list[list[int]]

        testcases = [
            TestCase(
                name=1,
                intervals = [[1,3],[2,6],[8,10],[15,18]],
                expected = [[1,6],[8,10],[15,18]]
            ),
            TestCase(
                name=2,
                intervals=[[1,4],[4,5]],
                expected = [[1,5]]
            ),
            TestCase(
                name=3,
                intervals=[[1,3],[4,5]],
                expected = [[1,3], [4,5]]
            ),
            TestCase(
                name=4,
                intervals=[[4,5]],
                expected = [[4,5]]
            ),
            TestCase(
                name=5,
                intervals=[[1,10], [4,5]],
                expected = [[1,10]]
            ),
            TestCase(
                name=6,
                intervals=[[1,4],[0,4]],
                expected = [[0,4]]
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.merge(tc.intervals)
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