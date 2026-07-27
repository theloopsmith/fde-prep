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
    # 15 · Compress

    String Compression
    Write a function that compresses a string by replacing consecutive identical characters with the character followed by the count of repetitions.

    For example:

    "aaabbc" becomes "a3b2c1"
    "aabbccdd" becomes "a2b2c2d2"
    "abc" becomes "a1b1c1"
    Parameters:

    s: a string to compress
    Return:

    A compressed string where each character is followed by its count
    """)
    return


@app.cell
def _():
    from collections import Counter

    ## this is a wrong solution
    def compress_string(s: str) -> str:
        # WRITE YOUR BRILLIANT CODE HERE
        count = {}
        for ch in s:
            if count.get(ch):
                count[ch] +=1
            else:
                count[ch] = 1

        out: str = ''
        for ch in count:
            out = out + ch + str(count[ch])
        # print(count)
        return out

    def compress_string_correct(s: str) -> str:
        if not s:                       # guard: empty string -> nothing to flush
            return ""
        # list buffer + join instead of str += : keeps this O(n) rather than
        # the O(n^2) repeated-concatenation trap (each += rebuilds the string).
        parts = []
        prev = 0
        countInternal = 0
        for i in range(len(s)):
            if s[prev] == s[i]:
                countInternal += 1
            else:
                parts.append(s[prev] + str(countInternal))   # flush finished run
                prev = i
                countInternal = 1

        # flush the FINAL run: the loop only writes on a character change,
        # so the last group is still pending when the loop ends.
        parts.append(s[prev] + str(countInternal))
        return "".join(parts)

    print(compress_string_correct('aaabbcaa'))   # a3b2c1a2
    print(compress_string_correct('abc'))        # a1b1c1
    print(compress_string_correct(''))           # (empty)

    assert compress_string_correct('aaabbcaa') == 'a3b2c1a2'
    assert compress_string_correct('abc') == 'a1b1c1'
    assert compress_string_correct('') == ''
    assert compress_string_correct('aaaa') == 'a4'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pythonic version — `itertools.groupby`

    `groupby(s)` walks the string once and yields `(key, group)` for each run
    of *consecutive* equal chars — it does the "detect the run + flush on
    change + flush the last one" bookkeeping for you, so no off-by-one / final
    flush bug is possible. `key` is the char; `list(group)` materializes the run
    so `len(...)` gives its length.

    Same O(n) time / O(n) space as the manual version — pick the manual one in
    an interview to show you can track state, reach for this in real code.
    """)
    return


@app.cell
def _():
    from itertools import groupby

    def compress_string_groupby(s: str) -> str:
        # ch = the character of the run; g = an iterator over that run's chars
        return "".join(f"{ch}{len(list(g))}" for ch, g in groupby(s))

    print(compress_string_groupby('aaabbcaa'))   # a3b2c1a2
    print(compress_string_groupby('abc'))        # a1b1c1
    print(compress_string_groupby(''))           # (empty)

    assert compress_string_groupby('aaabbcaa') == 'a3b2c1a2'
    assert compress_string_groupby('abc') == 'a1b1c1'
    assert compress_string_groupby('') == ''
    assert compress_string_groupby('aaaa') == 'a4'
    return


if __name__ == "__main__":
    app.run()
