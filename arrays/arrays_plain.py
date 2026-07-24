"""Plain-Python version of arrays.py (marimo notebook)."""


# ============================================================
# Sum all digits in a number
# ============================================================

def digit_sum(N):
    total = 0
    while N > 0:         # loops once per digit
        total += N % 10  # grab last digit
        N //= 10         # drop last digit
    return total


# ============================================================
# Find Maximum
# ============================================================

def findMax(arr: list[int]):
    max_val = -9999999
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val


# ============================================================
# Find Occurrences
# Count how many times a target value appears in an array.
# ============================================================

def findOccurences(arr: list[int], key):
    occ = 0
    for i in arr:
        if i == key:
            occ += 1
    return occ


# ============================================================
# Remove Element
# Remove all instances of a target value from an array.
# ============================================================

# Time:  O(n)  - one pass; append is amortized O(1)
# Space: O(n)  - builds a separate result list (up to n elements)
def removeInstances(arr: list[int], key):
    res: list[int] = []
    for i in arr:
        if i != key:
            res.append(i)
    return res


# Time:  O(n^2) - each arr.remove() scans + shifts O(n); up to n removals
# Space: O(1)   - no extra structure
# NOTE: BUGGY - mutating a list while iterating over it skips elements
#               (the loop walks an index; remove() shifts everything left,
#               so the element that slid into the just-vacated slot is
#               skipped on the next iteration).
def removeInstancesBuggy(arr: list[int], key):
    for i in arr:
        if i == key:
            arr.remove(i)
    return arr


# Time:  O(n^2) - arr.remove() is O(n); called up to n times
# Space: O(n)   - arr[:] creates a snapshot copy to iterate over
# Fixes the bug above by iterating over a copy while mutating the original.
def removeInstances2(arr: list[int], key):
    for i in arr[:]:        # arr[:] is a snapshot copy
        if i == key:
            arr.remove(i)
    return arr


# Time:  O(n)  - one comprehension pass + O(n) slice assignment
# Space: O(n)  - comprehension builds a temporary list before assigning
#
# Breakdown of:  arr[:] = [i for i in arr if i != key]
#
# RHS - list comprehension:
#   [i for i in arr if i != key]
#   shorthand for:
#       result = []
#       for i in arr:
#           if i != key:
#               result.append(i)
#   Builds a NEW list containing only the elements we want to keep.
#
# LHS - slice assignment:
#   arr[:] = ...   replaces the CONTENTS of the existing list object
#                  in place (same object, new elements). Caller sees
#                  their list mutated.
#   arr    = ...   would only rebind the local name to a new list,
#                  leaving the caller's list untouched.
#
# Net effect: same behavior as arr.remove() in a loop, but O(n) instead
# of O(n^2), because we do a single linear pass instead of repeated shifts.
def removeInstances3(arr: list[int], key):
    arr[:] = [i for i in arr if i != key]   # mutates in place
    return arr


# Time:  O(n)  - single comprehension pass
# Space: O(n)  - returns a new list
# Most Pythonic when the caller doesn't need their original list mutated.
def removeInstances4(arr, key):
    return [i for i in arr if i != key]


# ============================================================
# Rotate Array
# Rotate an array k positions to the right.
# ============================================================

# Time:  O(n)  - two slices + concatenation each copy n elements
# Space: O(n)  - returns a new list
#
# Idea: rotating right by k is the same as cutting the last k elements
# off and putting them in front.
#   arr[-k:]   = last k elements   (the part that wraps to the front)
#   arr[:-k]   = everything else   (the part that shifts right)
#
# k %= len(arr) handles k >= len(arr) (e.g. rotating len 3 by 4 == by 1).
# The `if k else arr[:]` guard avoids arr[-0:] / arr[:-0] surprises when
# k normalizes to 0.
def rotateArray(arr: list[int], k: int):
    if not arr:
        return arr
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]


# Buggy reference implementation - kept for comparison.
def rotateArray1(arr: list[int], k: int):
    if k == 0:
        return arr
    if k > len(arr):
        k = len(arr) - 2

    a = arr[k + 1:len(arr):1]
    b = arr[0:k + 1:1]
    return a + b


# ============================================================
# Demo / smoke tests
# ============================================================

def main():
    print("digit_sum(1234) =", digit_sum(1234))

    print("findMax =", findMax([2, 21, -9, 8, 11]))

    print("findOccurences =", findOccurences([2, 21, -9, 8, 11, 21, 21], 21))

    print("removeInstances      =", removeInstances([2, 21, -9, 8, 11, 21, 21], 21))
    print("removeInstancesBuggy =", removeInstancesBuggy([2, 21, -9, 8, 11, 21, 21], 21))
    print("removeInstances2     =", removeInstances2([2, 21, -9, 8, 11, 21, 21], 21))
    print("removeInstances3     =", removeInstances3([2, 21, -9, 8, 11, 21, 21], 21))
    print("removeInstances4     =", removeInstances4([2, 21, -9, 8, 11, 21, 21], 21))

    print("rotateArray([1,2,3,4,5], 2) =", rotateArray([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
    print("rotateArray([1,2,3], 4)     =", rotateArray([1, 2, 3], 4))        # [3, 1, 2]
    print("rotateArray([1,2,3,4], 0)   =", rotateArray([1, 2, 3, 4], 0))     # [1, 2, 3, 4]
    print("rotateArray([], 3)          =", rotateArray([], 3))               # []


if __name__ == "__main__":
    main()
