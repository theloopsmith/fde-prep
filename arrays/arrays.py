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
    # Arrays / lists — interview prep notebook

    A self-contained reference. Each section is a short markdown header
    followed by a runnable cell. Read top-to-bottom the first time; jump by
    section when revisiting.

    ## Table of contents
    **Part A — Fundamentals**
    1. Creating & indexing a list
    2. Slicing (`start:stop:step`)
    3. Mutate in place vs Rebind vs Copy

    **Part B — The performance trap**
    4. Removing elements: the mutate-while-iterating bug & O(n²) → O(n)

    **Part C — Core algorithms**
    5. Find the maximum
    6. Count occurrences of a target
    7. Rotate an array (right / left / unified)
    8. Sum the digits of a number (modulo/divide warm-up)

    **Appendix**
    - Slicing primer (`arr[start:stop:step]`, negatives, the copy idiom)

    ---
    **Recurring theme:** lists are mutable, so the key question for every
    operation is *does it mutate in place, rebind the name, or build a copy?*
    Getting that wrong causes the classic mutate-while-iterating bug (Part B).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part A — Fundamentals

    ### 1. Creating & indexing a list

    `[0] * n` builds a length-n list of zeros. Indexing is O(1). Note the loop
    below starts at index 1, so it intentionally skips `ar[0]`.
    """)
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
    ### 2. Slicing (`start:stop:step`)

    `arr[start:stop:step]` returns a NEW list. `stop` is exclusive; negative
    indices count from the end; `step` can skip or (when negative) reverse.
    See the Appendix for the full primer.
    """)
    return


@app.cell
def _():
    k = [1,2,3,4,5,6,7]

    print(k[:])
    print(k[1:])
    print(k[2:-2:3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Mutate in place vs Rebind vs Copy

    The mental model that decides whether the *caller* sees your change. This
    is the crux of the remove-element bug in Part B.

    ```
      name  = value      -> REBIND: local name points at a new list;
                            the caller's original list is UNTOUCHED.
      name[:] = value    -> MUTATE IN PLACE: same list object, new contents;
                            the caller SEES the change.
      value[:] / list(value) / value.copy()
                         -> COPY: an independent list.

      a = [9, 9]         # rebind local name only (caller unaffected)
      a[:] = [9, 9]      # mutate caller's list in place (caller sees it)
      b = a              # ALIAS: same list -> mutating one shows in both
      b = a[:]           # COPY: independent list (also list(a) / a.copy())

    SHALLOW vs DEEP (nested lists):
      a[:], list(a), a.copy()  -> shallow: outer copied, inner shared
      copy.deepcopy(a)         -> fully independent (inner objects copied)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part B — The performance trap

    ### 4. Removing elements

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part C — Core algorithms

    ### 5. Find the maximum

    One linear pass tracking the running max.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. Count occurrences of a target

    Write a function that counts how many times a target value appears in an
    array of integers.
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
    ### 7. Rotate an array

    Write a function that rotates an array k positions to the right. Built on
    slicing (see Appendix): rotating right by k = last k elements moved front.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. Sum the digits of a number (modulo/divide warm-up)

    Not an array problem, but the `% 10` / `// 10` digit-peeling loop is a
    classic warm-up worth keeping in muscle memory.
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
    ## Appendix — Slicing primer (`arr[start:stop:step]`)

    Slicing underpins rotate, remove, and the copy idiom, so it's worth
    knowing cold. A slice always returns a NEW list; `stop` is EXCLUSIVE.

    ```
    arr = [0, 1, 2, 3, 4, 5, 6]
           0  1  2  3  4  5  6     (indices from front)
          -7 -6 -5 -4 -3 -2 -1     (indices from back)

    arr[2:5]    -> [2, 3, 4]        start..stop-1
    arr[:3]     -> [0, 1, 2]        start defaults to 0
    arr[4:]     -> [4, 5, 6]        stop defaults to len
    arr[:]      -> full COPY        (same as list(arr) / arr.copy())
    arr[-2:]    -> [5, 6]           last 2 (used by rotate right)
    arr[:-2]    -> [0, 1, 2, 3, 4]  all but last 2
    arr[::2]    -> [0, 2, 4, 6]     every 2nd element
    arr[::-1]   -> [6, 5, 4, 3, 2, 1, 0]   reversed (negative step)
    arr[2:-2:3] -> [2, 5]           start 2, stop at index -2 (excl), step 3
    ```

    ### Quick-reference
    | Slice | Meaning |
    |---|---|
    | `arr[a:b]` | elements a .. b-1 (b exclusive) |
    | `arr[:]` | full shallow copy |
    | `arr[-k:]` | last k elements |
    | `arr[:-k]` | all but the last k |
    | `arr[::-1]` | reversed copy |
    | `arr[:] = [...]` | MUTATE contents in place (not a copy!) |

    Gotchas: out-of-range slice bounds are CLAMPED (never raise), unlike plain
    indexing which raises IndexError. And `arr[-0:]` is `arr[0:]` (the whole
    list), which is why rotate guards the k==0 case explicitly.
    """)
    return


if __name__ == "__main__":
    app.run()
