import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):
    def test_graph(self):
        @dataclass
        class TestData:
            name: str
            expected: str
        
        testcases = [
            TestData(
                name="1",
                edges=[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)],
                expected="0 -> 1, 2\n1 -> 2\n2 -> 0, 3\n3 -> 3\n"
            )
        ]

        for tc in testcases:
            got = str(g)
            print(got)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()