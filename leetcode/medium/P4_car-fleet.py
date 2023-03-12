### PROBLEM STATEMENT
# https://leetcode.com/problems/car-fleet/?fbclid=IwAR3rIVSIa5O9_1xCBp_uaE-g-eNxzPak2l40WpZBS1xSagiP5ppK68E133Y

# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.

# XXX     XX                   X                  XXX|||
# XXX     XX                   X|||
# XXXXX|||


# Example 1:
# Car:      1  2  3  4  5
# Position: 0  3  5  8  10 ... 12
# Speed:    1  3  1  4  2

# position: [10,8,0,5,3]
# 10 -> 0
# 8 -> 1
# 0 -> 2
# 5 -> 3
# 3 -> 4
# speed: [2,4,1,1,3]

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1
# Explanation: There is only one car, hence there is only one fleet.

# Example 3:
# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1
# Explanation:
# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
# Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        L = len(position)
        if L <= 1:
            return 1
        stack = self.sortPositions(position, speed)        
        canMerge= True
        while canMerge:
            print("stack:", stack)
            merge = False
            newStack = []
            while len(stack) > 0:
                print("newStack:", newStack)
                if len(stack) == 1:
                    newStack.append(stack.pop(0))
                    break

                starter = stack[0]
                cur = stack[1]
                t1 = self.timeToTarget(target, starter[0], starter[1])
                t2 = self.timeToTarget(target, cur[0], cur[1])
                if t1 <= t2:
                    print("merge")
                    # merge cars
                    starter = stack.pop(0)
                    cur = stack.pop(0)            
                    stack.insert(0, (cur[0], min(starter[1], cur[1])))
                    merge = True
                    continue
                else:
                    print("skip")
                    # remove the first car
                    newStack.append(stack.pop(0))
            stack = newStack
            canMerge = merge == False
        print("final:", stack)
        return len(stack)
    
    def sortPositions(self, position: list[int], speed: list[int]) -> list[tuple]:
        L = len(position)
        # sort positions by distance
        m = {}
        stack = []
        for i in range(L):
            m[position[i]]= speed[i]
        position.sort()
        for i in range(L):
            speed[i] = m[position[i]]
        # print(position)
        # print(speed)
        for i in range(L):
            stack.append((position[i], speed[i]))
        return stack

    def timeToTarget(self, target: int, position: int, speed: int) -> float:
        return (target - position) / speed

# Leetcode Accepted solution
class Solution1:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) <= 1:
            return 1
        stack = self.sortPositions(position, speed)        
        canMerge= True
        oldLen = len(stack)
        newLen = 0
        while oldLen != newLen:
            oldLen = newLen
            newStack = []
            while len(stack) > 0:
                if len(stack) == 1:
                    newStack.append(stack.pop(0))
                    break

                starter = stack[0]
                cur = stack[1]
                t1 = self.timeToTarget(target, starter[0], starter[1])
                t2 = self.timeToTarget(target, cur[0], cur[1])
                if t1 <= t2:
                    # merge cars
                    starter = stack.pop(0)
                    cur = stack.pop(0)            
                    stack.insert(0, (cur[0], cur[1]))
                    continue
                else:
                    # remove the first car
                    newStack.append(stack.pop(0))
            stack = newStack
            newLen = len(stack)
        return len(stack)
    
    def sortPositions(self, position: list[int], speed: list[int]) -> list[tuple]:
        """Returns list of (position, speed) tuple (sorted by positions)."""
        L = len(position)
        # sort positions by distance
        m = {}
        stack = []
        for i in range(L):
            m[position[i]]= speed[i]
        position.sort()
        for i in range(L):
            speed[i] = m[position[i]]
        # print(position)
        # print(speed)
        for i in range(L):
            stack.append((position[i], speed[i]))
        return stack

    def timeToTarget(self, target: int, position: int, speed: int) -> float:
        return (target - position) / speed  
### TEST UTILITIES

### MAIN FUNCTIONS

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):

    def test_1(self):
        @dataclass
        class TestCase:
            name: str
            target: int
            position: list[int]
            speed: list[int]
            expected: int

        testcases = [
            TestCase(
                name="1",
                target=12,
                position=[10,8,0,5,3],
                speed=[2,4,1,1,3],
                expected=3
            ),
            TestCase(
                name="2",
                target=10,
                position=[3],
                speed=[3],
                expected=1
            ),
            TestCase(
                name="3",
                target=100,
                position=[0,2,4],
                speed=[4,2,1],
                expected=1
            ),
        ]

        s = Solution()
        for tc in testcases:
            got = s.carFleet(tc.target, tc.position, tc.speed)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(
                    tc.name, tc.expected, got
                ),
            )

def main():
    s = Solution()
    # s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
    # s.carFleet(10, [3], [3])
    s.carFleet(100, [0,2,4], [4,2,1])

if __name__ == '__main__':
    # main()
    unittest.main()