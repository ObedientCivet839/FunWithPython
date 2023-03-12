### PROBLEM STATEMENT
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Method 1:
# 
# Idea:
# 
#
# Runtime: O(???)
# 
#
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        word += "#"
        self.root.insert(word)

    def printWD(self):
        self.root.printNode()

    def search(self, word: str) -> bool:
        word += "#"
        return self.root.search(word)

    def autocomplete(self, w):
        if not self.root.search(w):
            print("Prefix not found")
            return
        return self.root.autocomplete(w)

class Node:
    def __init__(self):
        self.cm = {} # character map
    
    def insert(self, s):
        if not s:
            return
        c = s[0]
        # print("c:", c)
        if c not in self.cm:
            self.cm[c] = Node()
        self.cm[c].insert(s[1:])
    
    def printNode(self):
        print(self.cm.keys())
        for m in self.cm.values():
            m.printNode()
    
    def search(self, s):
        # support dot (wildcard) search
        if not s:
            return True
        c = s[0]
        if c != ".":
            if c not in self.cm:
                return False
            return self.cm[c].search(s[1:])
        else:
            for n in self.cm.values():
                if n.search(s[1:]):
                    return True
            return False
    
    def substrings(self):
        res = []
        for k, v in self.cm.items():
            if k == "#":
                res.extend([""])
            else:
                words = v.substrings()
                res.extend([str(k) + w for w in words])
        return res

    def autocomplete(self, s):
        if not s:
            return [""]
        node = self
        for c in s:
            node = node.cm[c]
        ss = node.substrings()
        return [s + str(ps) for ps in ss]
    

# cat
# car
# c -> a -> t
#        -> r
        


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
                nums = 0,
                expected = 0,
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
    # s = Solution()
    # print(s)

    d = WordDictionary()
    d.addWord("cat")
    # d.printWD()
    d.addWord("car")
    # d.printWD()
    d.addWord("class")
    # d.printWD()
    d.addWord("clash")
    d.addWord("clashes")
    d.printWD()

    assert d.search("cat") == True
    assert d.search("car") == True
    assert d.search("cato") == False

    print(d.search("class"))
    print(d.search("ca")) # BUG: Not in dictionary
    print(d.search("cla.."))
    print(d.search("......"))

    print(d.autocomplete("ca"))
    print(d.autocomplete("cla"))


if __name__ == '__main__':
    main()
    # unittest.main()