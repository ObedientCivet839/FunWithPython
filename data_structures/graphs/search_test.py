import unittest
from dataclasses import dataclass

from graph import DirectedGraph
from search import GraphSearch

class UnitTest(unittest.TestCase):
    def test_graph(self):
        @dataclass
        class TestData:
            name: str
            edges: list[tuple[int]]
            start: int
            expected: list[int]
        
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
                start=2,
                expected=[2, 0, 3, 1]
            )
        ]

        for tc in testcases:
            g = DirectedGraph()
            for e in tc.edges:
                g.addEdge(e[0], e[1])
            print(g)
            s = GraphSearch(g)
            got = s.BFS(tc.start)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()