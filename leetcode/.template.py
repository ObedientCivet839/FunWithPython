### PROBLEM STATEMENT

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class Solution:
    pass

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
                nums = [0],
                expected = 0
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