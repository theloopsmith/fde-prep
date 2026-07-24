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
    # 09 · Safely modify a char at an index

    Immutability means "editing" index i = building a new string from three
    slices. The bounds guard makes an out-of-range index a no-op.
    """)
    return


@app.cell
def _():
    # Strings are immutable, so "modifying" index i means BUILDING A NEW string
    # from three slices: everything before i, the replacement, everything after.
    # Time: O(n)   Space: O(n)  (slicing + concatenation each copy the chars).
    def safe_modify_string(s: str, index: int, new_char: str) -> str:
        # Bounds guard: out-of-range index returns the original unchanged
        # rather than raising -- hence "safe".
        if index >= 0 and index < len(s):
           # s[:index:1]  -> the `:1` step is redundant (1 is the default);
           #                 s[:index] reads the same.
           # s[index+1:len(s)] -> the `len(s)` is redundant; s[index+1:] reads
           #                 to the end. Kept as-is to match the original.
           return s[:index:1] + new_char + s[index+1:len(s)]
        return s

    print(safe_modify_string('world', 2, 'X'))
    # A plain assert keeps this snippet dependency-free (no numpy needed).
    assert safe_modify_string('world', 2, 'X') == 'woXld'
    return


if __name__ == "__main__":
    app.run()
