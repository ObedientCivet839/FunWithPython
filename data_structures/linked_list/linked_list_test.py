from linked_list import LinkedList

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
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list: ", linked_list)
            got = len(linked_list)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_append(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            push: list[int]
            expected: bool
        
        testcases = [
            TestData(
                name="append_1",
                elems=[1,2,3,4],
                push=[5,6],
                expected=6,
            ),
            TestData(
                name="append_2",
                elems=[],
                push=[1],
                expected=1,
            ),
            TestData(
                name="append_3",
                elems=None,
                push=[],
                expected=0,
            ),
        ]

        for tc in testcases:
            print(tc.name)
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list (before): ", linked_list)
            for i in tc.push:
                linked_list.append(i)
            print("linked_list (after): ", linked_list)                
            got = len(linked_list)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_prepend(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            push: list[int]
            expected: bool
        
        testcases = [
            TestData(
                name="prepend_1",
                elems=[1,2,3,4],
                push=[5,6],
                expected=6,
            ),
            TestData(
                name="prepend_2",
                elems=[],
                push=[1],
                expected=1,
            ),
            TestData(
                name="prepend_3",
                elems=None,
                push=[],
                expected=0,
            ),
        ]

        for tc in testcases:
            print(tc.name)
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list (before): ", linked_list)
            for i in tc.push:
                linked_list.prepend(i)
            print("linked_list (after): ", linked_list)                
            got = len(linked_list)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_remove(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: int
        
        testcases = [
            TestData(
                name="1",
                elems=[1,2,3,4],
                expected=1,
            ),
            TestData(
                name="2",
                elems=[3],
                expected=3,
            ),
        ]

        for tc in testcases:
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list (before): ", linked_list)
            got = linked_list.remove_front()
            print("linked_list (after): ", linked_list)                
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_reverse(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: str
        
        testcases = [
            TestData(
                name="reverse_1",
                elems=[1, 2, 3, 4],
                expected="4 -> 3 -> 2 -> 1",
            ),
            TestData(
                name="reverse_2",
                elems=[],
                expected="",
            ),
            TestData(
                name="reverse_3",
                elems=[1],
                expected="1",
            ),
        ]

        for tc in testcases:
            print(tc.name)
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list (before): ", linked_list)
            linked_list.reverse()
            print("linked_list (after): ", linked_list)                
            got = str(linked_list)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_reverse_recursive(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: str
        
        testcases = [
            TestData(
                name="rreverse_1",
                elems=[1, 2, 3, 4],
                expected="4 -> 3 -> 2 -> 1",
            ),
            TestData(
                name="rreverse_2",
                elems=[],
                expected="",
            ),
            TestData(
                name="rreverse_3",
                elems=[1],
                expected="1",
            ),
        ]

        for tc in testcases:
            print(tc.name)
            linked_list = LinkedList.from_array(tc.elems)
            print("linked_list (before): ", linked_list)
            linked_list.reverse_recursive()
            print("linked_list (after): ", linked_list)                
            got = str(linked_list)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()