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
    # 07 · Rotate an array

    Write a function that rotates an array k positions to the right. Built on
    slicing (see appendix_slicing_primer.py): rotating right by k = last k
    elements moved to the front.
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


if __name__ == "__main__":
    app.run()
