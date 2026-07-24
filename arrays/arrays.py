# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sum all digits in a number
    """)
    return


@app.cell
def _():
    def digit_sum(N):
        total = 0
        while N > 0:        # loops once per digit
            total += N % 10  # grab last digit
            N //= 10         # drop last digit
        return total

    print(digit_sum(1234))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Find Maximum
    """)
    return


@app.cell
def _():
    def findMax(arr: list[int]):
        max = -9999999
        for i in arr:
            if i > max:
                max = i
        return max  

    print(findMax([2,21,-9,8,11]))
    return


@app.cell
def _():
    ar = [0] * 5
    print(ar)
    print('ok')
    for i in range(1,5):
        print(ar[i])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Find occurences:
    Write a function that counts how many times a target value appears in an array of integers.
    """)
    return


@app.cell
def _():
    def findOccurences(arr: list[int], key):
        occ = 0
        for i in arr:
            if i == key:
                occ += 1
        return occ

    print(findOccurences([2,21,-9,8,11, 21, 21], 21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remove Element:
    Write a function that removes all instances of a target value from an array, returning a new array without those elements.
    """)
    return


@app.cell
def _():
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

    print(removeInstances([2,21,-9,8,11, 21, 21], 21))
    print(removeInstancesBuggy([2,21,-9,8,11, 21, 21], 21))
    print(removeInstances2([2,21,-9,8,11, 21, 21], 21))
    print(removeInstances3([2,21,-9,8,11, 21, 21], 21))
    print(removeInstances4([2,21,-9,8,11, 21, 21], 21))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Rotate Array
    Write a function that rotates an array k positions to the right.
    """)
    return


@app.cell
def _():
    # Time:  O(n)  - two slices + concatenation each copy n elements
    # Space: O(n)  - returns a new list
    #
    # Idea: rotating right by k is the same as cutting the last k elements
    # off and putting them in front.
    #   arr[-k:]   = last k elements   (the part that wraps to the front)
    #   arr[:-k]   = everything else   (the part that shifts right)
    #
    # k %= len(arr) handles k >= len(arr) (e.g. rotating len 3 by 4 == by 1)
    # and the `or arr` guard avoids arr[-0:] / arr[:-0] returning the empty
    # slice when k normalizes to 0.
    def rotateArray(arr: list[int], k: int):
        if not arr:
            return arr
        k %= len(arr)
        return arr[-k:] + arr[:-k] if k else arr[:]

    # Time:  O(n)  - two slices + concatenation each copy n elements
    # Space: O(n)  - returns a new list
    #
    # Rotate LEFT by k: elements move toward lower indices; the first k
    # elements wrap around to the back. Mirror image of rotateArray.
    #   arr[k:]   = everything from index k onward (shifts left to the front)
    #   arr[:k]   = the first k elements          (wrap around to the back)
    #
    # Note: for left rotation the `if k else` guard isn't strictly needed
    # (arr[0:] + arr[:0] == whole list + empty == whole list), but we keep
    # it for symmetry and to always return a fresh copy.
    def rotateLeft(arr: list[int], k: int):
        if not arr:
            return arr
        k %= len(arr)
        return arr[k:] + arr[:k] if k else arr[:]

    # Time:  O(n)  - delegates to a single slice-based rotation
    # Space: O(n)  - returns a new list
    #
    # Unified helper. direction="right" (default) or "left".
    # Identity used: rotating left by k == rotating right by (n - k),
    # so we normalize a left request into an equivalent right rotation
    # and reuse rotateArray for a single source of truth.
    def rotate(arr: list[int], k: int, direction: str = "right"):
        if not arr:
            return arr
        if direction == "left":
            k = -k
        elif direction != "right":
            raise ValueError("direction must be 'right' or 'left'")
        return rotateArray(arr, k % len(arr))

    print(rotateArray([1, 2, 3, 4, 5], 2))            # [4, 5, 1, 2, 3]
    print(rotateArray([1, 2, 3], 4))                  # [3, 1, 2]  (4 % 3 == 1)
    print(rotateArray([1, 2, 3, 4], 0))               # [1, 2, 3, 4]
    print(rotateArray([], 3))                         # []

    print(rotateLeft([1, 2, 3, 4, 5], 2))             # [3, 4, 5, 1, 2]
    print(rotateLeft([1, 2, 3], 4))                   # [2, 3, 1]  (4 % 3 == 1)

    print(rotate([1, 2, 3, 4, 5], 2))                 # [4, 5, 1, 2, 3]  (right)
    print(rotate([1, 2, 3, 4, 5], 2, "left"))         # [3, 4, 5, 1, 2]
    print(rotate([1, 2, 3, 4, 5], 3, "right"))        # [3, 4, 5, 1, 2]  (== left by 2)
    return


@app.cell
def _():
    k = [1,2,3,4,5,6,7]

    print(k[:])
    print(k[1:])
    print(k[2:-2:3])
    return


if __name__ == "__main__":
    app.run()
