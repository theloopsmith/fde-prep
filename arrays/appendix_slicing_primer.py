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
    # Appendix · Slicing primer (`arr[start:stop:step]`)

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
