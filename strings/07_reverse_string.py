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
    # 07 · Reverse a string (3 ways)

    Two O(n²) `+=` versions (to feel the trap) and the Pythonic O(n) slice.
    """)
    return


@app.cell
def _():
    # Time: O(n^2)  Space: O(n)
    # Walks indices back-to-front (n iterations), but res += s[i] rebuilds
    # the immutable string each time, copying the growing prefix -> O(n^2).
    # A Pythonic O(n) alternative is simply: return s[::-1]
    def reverse_loop_backward(s: str):
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res

    # Time: O(n^2)  Space: O(n)  -- same += cost as reverse_loop_backward.
    # Walks front-to-back (i = 0..n-1) but indexes from the back:
    # s[len(s)-i-1] maps i=0 -> last char, i=n-1 -> first char (s[0]).
    # The -1 keeps the index in range (max index is len(s)-1, not len(s)).
    def reverse_loop_forward(s: str):
        res = ""
        for i in range(len(s)):
            res += s[len(s)-i-1]
        return res

    # Time: O(n)   Space: O(n)
    # Pythonic: slice with step -1 builds the reversed string in one C-level
    # pass and a single allocation -- no per-char += copying.
    def reverse_slice(s: str):
        return s[::-1]

    print(reverse_loop_backward('hello world'))
    print(reverse_loop_forward('hello world'))
    print(reverse_slice('hello world'))
    return


if __name__ == "__main__":
    app.run()
