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
    # 03 · Character codes: `ord()` / `chr()` & lexicographic compare

    `ord(c)` -> code point of a 1-char string; `chr(n)` -> char for int n.
    Both O(1). String comparison (`>`, `<`) is lexicographic by code point.
    """)
    return


@app.cell
def _():
    # ord() and chr() are both O(1) (constant time & space):
    #   - ord(c): reads the single character's already-stored code point;
    #             no scanning. Requires a length-1 string.
    #   - chr(n): builds/looks up the char for int n; small code points
    #             (<=255) return cached singletons -> just a table lookup.
    # Note: constant PER CALL. Applying ord over a whole string is O(n),
    # e.g. [ord(c) for c in s]. In hot loops, hoist constants like
    # base = ord('a') outside the loop to avoid repeated call overhead.
    def compare_lexicographically(s1: str, s2: str):
        print(f"s1: {ord('a')} and s2: {ord('A')}")
        print(f"s1: {chr(97)} and s2: {chr(65)}")
        print(f"s1: {[ord(ch) for ch in s1] }")
        print(f"s2: {[ord(ch) for ch in s2] }")

        print(f"0 is {ord('0')}")
        test:str ='A'
        # Check if a char is a digit / uppercase via ranges
        print(f"ch: {test} - {ord('0') <= ord(test) <= ord('9')}")

        if s1 > s2:
            return 1
        if s1 < s2:
            return -1
        return 0

    print(compare_lexicographically('a', 'A'))
    print(compare_lexicographically('apple', 'Apple'))
    return


if __name__ == "__main__":
    app.run()
