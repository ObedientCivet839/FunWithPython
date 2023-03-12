### PROBLEM STATEMENT
# https://leetcode.com/problems/insert-interval/


# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Method 1:
# 
# Idea:
# Find the intervals that overlaps with the new intervals.
# Merge them all together.
#
# Runtime: O(???)
# 
#
class Solution_M1:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        merged = False
        noOverlap = True
        for inv in intervals:
            if self.overlap(newInterval, inv):
                # merge the overlapped intervals
                newInterval[0] = min(newInterval[0], inv[0])
                newInterval[1] = max(newInterval[1], inv[1])
                merged = True
                noOverlap = False
            else:
                # Not very great here.
                if merged:
                    res.append(newInterval)
                    merged = False
                res.append(inv)
        # If merged until the end of the list
        if merged or noOverlap:
            if noOverlap and len(res) > 0 and newInterval[0] < res[0][0]:
                res.insert(0, newInterval)
            else:
                res.append(newInterval)
        return res
    
    # as --> ae
    # bs --> be
    def overlap(self, a: list[int], b: list[int]) -> bool:
        if a[0] <= b[0] and b[0] <= a[1] or b[0] <= a[0] and a[0] <= b[1]:
            return True
        return False

# M2: Just find the postion and insert the element.
# Then keep running until merge all the intervals using a stack.
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        target = len(intervals) # insert at the end of the list
        for i, n in enumerate(intervals):
            if newInterval[0] < n[0]:
                target = i
                break
        print("before:", intervals)
        intervals.insert(target, newInterval)
        print("after:", intervals)
        return self.merge(intervals)
    
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        while len(intervals) > 1:
            # pop one intervals from the front
            a = intervals.pop(0)
            b = intervals[0]
            if self.overlap(a, b):
                # merge
                b[0] = min(a[0], b[0])
                b[1] = max(a[1], b[1])
            else:
                res.append(a)
        res.extend(intervals)
        return res
    
    def overlap(self, a: list[int], b: list[int]) -> bool:
        if a[0] <= b[0] and b[0] <= a[1] or b[0] <= a[0] and a[0] <= b[1]:
            return True
        return False


### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            invs: list[list[int]]
            ni: list[int]
            expected: list[list[int]]

        testcases = [
            TestCase(
                name="1",
                invs=[[1,3],[6,9]],
                ni=[2,5],
                expected = [[1,5],[6,9]]
            ),
            TestCase(
                name="2",
                invs=[[1,2],[3,5],[6,7],[8,10],[12,16]],
                ni=[4,8],
                expected = [[1,2],[3,10],[12,16]]
            ),
            TestCase(
                name="3",
                invs=[[1,3],[4,6]],
                ni=[2,5],
                expected = [[1,6]]
            ),
            TestCase(
                name="4",
                invs=[],
                ni=[5,7],
                expected = [[5,7]]
            ),
            TestCase(
                name="5",
                invs=[[1,5]],
                ni=[5,7],
                expected = [[1,7]]
            ),
            TestCase(
                name="6",
                invs=[[1,5]],
                ni=[6,8],
                expected = [[1,5],[6,8]]
            ),
            TestCase(
                name="7",
                invs=[[1,5]],
                ni=[0,0],
                expected = [[0,0],[1,5]]
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.insert(tc.invs, tc.ni)
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