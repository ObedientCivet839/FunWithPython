import unittest
from dataclasses import dataclass

from graph import DirectedGraph
from search import GraphSearch

class UnitTest(unittest.TestCase):
    def test_bfs(self):
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

    def test_dfs(self):
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
            TestData(
                name="1",
                edges=[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)],
                start=2,
                expected=[2, 3, 0, 1]
            )
        ]

        for tc in testcases:
            g = DirectedGraph()
            for e in tc.edges:
                g.addEdge(e[0], e[1])
            print(g)
            s = GraphSearch(g)
            got = s.DFS(tc.start)
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

    def test_detect_cycle(self):
        @dataclass
        class TestData:
            name: str
            edges: list[tuple[int]]
            expected: bool
        
        testcases = [
            # OUTPUT:
            # 0  ->  1
            # 1  ->  2
            # 2  ->  0
            TestData(
                name="1",
                edges=[(0, 1), (1, 2), (2, 0)],
                expected=True
            ),
            TestData(
                name="2",
                edges=[(0, 1), (1, 2)],
                expected=False
            ),
            TestData(
                name="3",
                edges=[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)],
                expected=True
            )
        ]

        for tc in testcases:
            g = DirectedGraph()
            for e in tc.edges:
                g.addEdge(e[0], e[1])
            print(g)
            s = GraphSearch(g)
            got = s.detectCycle()
            self.assertEqual(
                tc.expected,
                got,
                "Test {} failed. Expected {}, actual {}".format(tc.name, tc.expected, got)
            )

if __name__ == "__main__":
    unittest.main()