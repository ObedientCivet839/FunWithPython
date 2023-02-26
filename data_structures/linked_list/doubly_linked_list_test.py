from doubly_linked_list import LinkedDeque

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):
    def test_len(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: int
        
        testcases = [
            TestData(
                name="1",
                elems=[1,2,3,4],
                expected=4
            ),
            TestData(
                name="2",
                elems=[3,4],
                expected=2
            ),
            TestData(
                name="3",
                elems=[1],
                expected=1
            ),
            TestData(
                name="4",
                elems=[],
                expected=0
            ),
        ]

        for tc in testcases:
            ld = LinkedDeque()
            for e in tc.elems:
                ld.insert_first(e)
            got = len(ld)
            # print(ld)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_delete(self):
        @dataclass
        class TestData:
            name: str
            elems: list[int]
            expected: int
        
        testcases = [
            TestData(
                name="1",
                elems=[1,2,3,4],
                expected=2
            ),
            TestData(
                name="2",
                elems=[3,4],
                expected=0
            ),
        ]

        for tc in testcases:
            ld = LinkedDeque()
            for e in tc.elems:
                ld.insert_first(e)
            print(ld)                
            print(ld.delete_first())
            print(ld.delete_last())
            got = len(ld)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()