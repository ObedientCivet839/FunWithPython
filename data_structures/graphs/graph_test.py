from graph import DirectedGraph

import unittest
from dataclasses import dataclass

class UnitTest(unittest.TestCase):
    def test_graph(self):
        @dataclass
        class TestData:
            name: str
            edges: list[tuple[int]]
            expected: str
        
        testcases = [
            # OUTPUT:
            # 0  ->  1, 2
            # 1  ->  2
            # 2  ->  0, 3
            # 3  ->  3
            # [2, 0, 3, 1]
            TestData(
                name="1",
                edges=[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)],
                expected="0 -> 1, 2\n1 -> 2\n2 -> 0, 3\n3 -> 3\n"
            )
        ]

        for tc in testcases:
            g = DirectedGraph()
            for e in tc.edges:
                g.addEdge(e[0], e[1])
            got = str(g)
            print(got)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()