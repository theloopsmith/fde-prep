# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 04 · Removing elements

    Write a function that removes all instances of a target value from an
    array. Five variants walk from the classic **mutate-while-iterating bug**,
    through the O(n²) `.remove()`-in-a-loop versions, to the O(n) comprehension
    idioms — and show `arr[:] = ...` (mutate in place) vs `return [...]` (copy).
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


if __name__ == "__main__":
    app.run()
