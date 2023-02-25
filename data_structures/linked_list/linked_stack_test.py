from linked_stack import LinkedStack

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):
    def test_len(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: bool
        
        testcases = [
            TestData(
                name="1",
                elems=[1,2,3,4],
                expected=4,
            ),
            TestData(
                name="2",
                elems=[],
                expected=0,
            ),
            TestData(
                name="3",
                elems=None,
                expected=0,
            ),
        ]

        for tc in testcases:
            stack = LinkedStack.from_array(tc.elems)
            print("stack: ", stack)
            got = len(stack)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_push(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            push: list[int]
            expected: bool
        
        testcases = [
            TestData(
                name="1",
                elems=[1,2,3,4],
                push=[5,6],
                expected=6,
            ),
            TestData(
                name="2",
                elems=[],
                push=[1],
                expected=1,
            ),
            TestData(
                name="3",
                elems=None,
                push=[],
                expected=0,
            ),
        ]

        for tc in testcases:
            stack = LinkedStack.from_array(tc.elems)
            print("stack (before): ", stack)
            for i in tc.push:
                stack.push(i)
            print("stack (after): ", stack)                
            got = len(stack)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()