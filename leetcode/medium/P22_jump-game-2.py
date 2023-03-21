### PROBLEM STATEMENT
# https://leetcode.com/problems/jump-game-ii/description/

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Method 1:
# 
# Idea:
# - Use dynamic programming
# - Store a steps array that stores the minimum steps required from that index to the end.
# - steps[i] = min(A[i, nums[i]])
#
# Runtime: O(N*max_val)
# 
#
class Solution:
    def jump(self, nums: list[int]) -> int:
        N = len(nums)
        steps = [0] * N
        for i in range(N-2, -1, -1):
            # Check the case if nums[i] is 0
            if nums[i] == 0:
                steps[i] = 10000 # set to a very large value
                continue
            end = min(i + nums[i], N - 1)
            print("num:", nums[i], "i:", i, "end:", end)
            print("nums:", nums[i+1:end+1])
            steps[i] = min(steps[i+1:end+1]) + 1
        print("steps:", steps)
        return steps[0]

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
                nums = [2,3,1,1,4],
                expected = 2
            ),
            TestCase(
                name="2",
                nums = [2,3,0,1,4],
                expected = 2
            ),
            TestCase(
                name="3",
                nums = [1,2,3],
                expected=2
            )
        ]

        s = Solution()
        for tc in testcases:
            got = s.jump(tc.nums)
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