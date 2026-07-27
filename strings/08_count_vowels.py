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
        # casefold: caseless compare, folds ß->ss (stronger than lower())
        return sum(ch in vowels for ch in s.casefold())

    print(count_vowels('hello world'))            # 3
    print(count_vowels_pythonic('hello world'))    # 3
    print(count_vowels_pythonic('AEiou XYZ'))      # 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Remove vowels

    Same immutable-accumulation trap as reverse/build-with-join: growing a
    string with `out = out + ch` in a loop is O(n²). Filter-then-`join` is
    O(n); `str.translate` is the C-level fastest.
    """)
    return


@app.cell
def _():
    import string
    # Naive -- the O(n^2) TRAP: `out = out + ch` rebuilds the whole immutable
    # string every iteration (copying the growing prefix). Also un-Pythonic:
    # indexing via range(len(s)) instead of iterating the chars directly.
    # Time: O(n^2)   Space: O(n)
    def remove_vowels(s: str) -> str:
        vowels = 'aeiouAEIOU'
        out: str = ''
        for i in range(len(s)):
            if s[i] not in vowels:
                out = out + s[i]
        return out

    # Tier 1 -- filter + join (idiomatic). Iterate chars directly, test
    # membership against a set (O(1)), and join once so the result is built in
    # a SINGLE allocation instead of n growing copies.
    # Time: O(n)   Space: O(n)
    def remove_vowels_pythonic(s: str) -> str:
        vowels = set('aeiou')
        # casefold: caseless compare, folds ß->ss (stronger than lower())
        return ''.join(ch for ch in s if ch.casefold() not in vowels)

    # Tier 2 -- str.translate (fastest). maketrans('', '', chars) builds a
    # table that DELETES every listed char; translate applies it in one
    # C-level pass. Maps by exact code point, so list BOTH cases explicitly
    # ('aeiouAEIOU') -- it can't casefold on the fly.
    # Time: O(n)   Space: O(n)
    def remove_vowels_translate(s: str) -> str:
        print(str.maketrans('', '', 'aeiouAEIOU'))
        return s.translate(str.maketrans('', '', 'aeiouAEIOU'))

    # Plain asserts keep this file dependency-free (no numpy needed).
    assert remove_vowels('hello world') == 'hll wrld'
    assert remove_vowels_pythonic('hello world') == 'hll wrld'
    assert remove_vowels_translate('hello world') == 'hll wrld'
    print(string.ascii_lowercase[1:])
    return


if __name__ == "__main__":
    app.run()
