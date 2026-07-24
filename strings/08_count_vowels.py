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
    # 08 · Count vowels

    Explicit loop vs the Pythonic `sum()` of a boolean generator.
    """)
    return


@app.cell
def _():
    # Time: O(n)   Space: O(1)
    # One pass over the n chars; `i in vowels` scans a fixed 10-char string
    # (constant), and count is a single integer.
    def count_vowels(s: str):
        vowels = 'aeiouAEIOU'
        count = 0
        for i in s:
            if i in vowels:
                count += 1
        return count

    # Pythonic: sum a generator of booleans. `ch in vowels` yields True/False,
    # and True == 1 / False == 0, so sum() counts the matches in one pass.
    # Using a set for O(1) membership and casefold() so both cases match
    # against a single lowercase set.
    # Time: O(n)   Space: O(1)  (fixed-size vowel set)
    def count_vowels_pythonic(s: str):
        vowels = set('aeiou')
        return sum(ch in vowels for ch in s.casefold())

    print(count_vowels('hello world'))            # 3
    print(count_vowels_pythonic('hello world'))    # 3
    print(count_vowels_pythonic('AEiou XYZ'))      # 5
    return


if __name__ == "__main__":
    app.run()
