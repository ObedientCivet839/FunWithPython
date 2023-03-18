### PROBLEM STATEMENT
# https://leetcode.com/problems/gas-station/

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


# Method 1: Greedy + linear time
# 
# Idea: Since we guarantee to have a single solution, we just need to find the first position
# that the total fuel for the rest of the array is not negative.
#
# Runtime: O(N)
#
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Make sure that total gas is greater than total cost
        if sum(gas) < sum(cost):
            return -1

        # Guarantee that there's EXACTLY one solution from this point
        res = 0
        fuel = 0
        for i in range(len(gas)):
            # Use greedy algorithm
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0 # reset total fuel
                res = i + 1  # starting position will be the next index
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
            gas: list[int]
            cost: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                gas=[1,2,3,4,5],
                cost=[3,4,5,1,2],
                expected = 3
            ),
            TestCase(
                name="2",
                gas=[2,3,4],
                cost=[3,4,3],
                expected = -1
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.canCompleteCircuit(tc.gas, tc.cost)
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