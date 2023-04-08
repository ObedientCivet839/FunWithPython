### PROBLEM STATEMENT
# https://leetcode.com/problems/path-with-minimum-effort/description/

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Method 1:
# 
# Idea: Didn't work
# Traverse the list but didn't use Memoization
#
# Runtime: O(???)
# 
#
class Solution1:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        self.R, self.C = len(heights), len(heights[0])
        self.H = heights
        self.global_max_gap = 1e7
        # self.count_paths = 0
        self.helper(0, 0, 0, set())
        # print('paths:', self.count_paths)
        return self.global_max_gap
    
    def helper(self, row, col, max_gap, visited):
        if max_gap > self.global_max_gap:
            return
        # TODO: Memoization
        if row == self.R-1 and col == self.C-1:
            self.global_max_gap = min(max_gap, self.global_max_gap)
            # self.count_paths += 1
            return
        dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        visited.add((row, col))
        for d in dirs:
            new_row = row + d[0]
            new_col = col + d[1]
            if (new_row, new_col) in visited:
                continue
            if 0 <= new_row < self.R and 0 <= new_col < self.C:
                new_val = self.H[new_row][new_col]
                new_gap = abs(self.H[row][col] - new_val)
                self.helper(new_row, new_col, max(max_gap, new_gap), visited)
        visited.remove((row, col))

# Method 2:
# 
# Idea: Dijkstra
#
# Runtime: O(???)
#
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        R, C = len(heights), len(heights[0])
        weights = [[-1e7 for i in range(C)] for j in range(R)]
        weights[0][0] = 0

        visited = set()
        row, col = 0, 0  # starting position
        queue = []
        queue.append((row, col))
        while not queue:  # if queue is not empty
            row, col = queue.pop(0)
            visited.add((row, col))        
            dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if (new_row, new_col) in visited:
                    continue
                # check inbound
                if 0 <= new_row < self.R and 0 <= new_col < self.C:
                    new_val = self.H[new_row][new_col]
                    new_gap = abs(weights[row][col] - new_val)
                    weights[new_row][new_col] = max(weights[row][col], new_gap)
        visited.remove((row, col))

        self.H = heights
        self.global_max_gap = 1e7
        self.helper(0, 0, 0, set())
        return self.global_max_gap
    

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
                nums = ,
                expected = 
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