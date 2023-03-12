### PROBLEM STATEMENT
# https://leetcode.com/problems/redundant-connection/

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# Method 1: Nice try :)
# 
# Idea:
# - The problem here is the graph already has cycles before it's fully connected.
# - The count of the edges was still smaller than vertices but it already has
# cycles.
# 
#
# Runtime: O(???)
# 
#
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        vertices = set()
        numEdges = 0
        for edge in edges:
            a, b = edge
            numEdges += 1
            vertices.add(a)
            vertices.add(b)
            if len(vertices) == numEdges:
                return edge
        return None

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        graph = {}
        for e in edges:
            print("e:", e)
            self.addEdge(graph, e)
            if self.hasCycle(graph):
                return e

    def addEdge(self, graph, edge):
        a, b = edge
        if a not in graph:
            graph[a] = set([b])
        else:
            graph[a].add(b)
        if b not in graph:
            graph[b] = set([a])
        else:
            graph[b].add(a)
    
    def hasCycle(self, graph):
        for v in graph:
            if self.hasVertexCycle(graph, v, set()):
                return True
        return False

    def hasVertexCycle(self, graph, v, visited):
        """Check that the graph has a cycle starts at vertex v."""
        # Return True if v is already visited
        if v in visited:
            return True
        print("v:", v)
        print("graph:", graph)
        for n in graph[v]:
            print("n:", n)
            visited.add(v)
            graph[n].remove(v) # remove the path from v <-> n
            if self.hasVertexCycle(graph, n, visited):
                return True
            graph[n].add(v)
            visited.remove(v)
        return False



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
                nums = 
                expected = 
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