### PROBLEM STATEMENT
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Method 1: Bruteforce
# 
# Idea:
# Merge the 2 lists together. Then find the median of the combined list.
#
# Runtime: O(m+n)
# - O(m+n) for the merge of the 2 arrays
# - O(1) for getting the median
#
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    merged = mergeLists(nums1, nums2)
    print("Merged list: ", merged)
    mps = getMedianPositions(len(merged))
    print("Median positions: ", mps)
    res = sum([merged[i] for i in mps]) * 1.0 / len(mps)
    print("Median: ", res)
    return res

### TEST UTILITIES
import random

# generate random list of integers with given length
def randList(ln: int) -> list[int]:
    # BUG: Can return the same integers
    return random.sample(range(1, 100), ln)

# sort list
def randSortedList(ln: int) -> list[int]:
    l = randList(ln)
    l.sort()
    return l

# merge lists merges 2 sorted lists
def mergeLists(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    while len(nums1) >= 0 and len(nums2) >= 0:
        # print(res)
        if len(nums1) == 0:
            res.extend(nums2)
            break
        if len(nums2) == 0:
            res.extend(nums1)
            break
        # if front of L1 < front of L2
        if nums1[0] < nums2[0]:
            res.append(nums1.pop(0))
        else:
            res.append(nums2.pop(0))
    return res

# Returns the positions of the median of a list of length l
def getMedianPositions(l: int) -> list[int]:
    # If s is odd, returns the middle index of the 2 lists
    mid = int(l / 2)
    if l % 2 == 1:
        # for example, [1,2,3] -> l = 3, mid = 1, median index is 1
        return [mid]
    else:
        # for example, [1,2,3,4] -> l = 4, mid = 2, median indices are 1 and 2
        return [mid - 1, mid]

### MAIN FUNCTIONS
def testRandSortedList():
    lA = randSortedList(10)
    lB = randSortedList(8)
    print(lA)
    print(lB)
    lAB = mergeLists(lA, lB)
    print(lAB)

def main():
    res = findMedianSortedArrays([1,2], [3])
    assert res == 2, "Test failed"
    res = findMedianSortedArrays([1,2], [3, 4])
    assert res == 2.5, "Test failed"

    listA = randSortedList(10)
    listB = randSortedList(8)
    print(listA)
    print(listB)
    res = findMedianSortedArrays(listA, listB)
    print(res)

main()