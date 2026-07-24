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
    # 10 · Character frequency: manual dict

    The hash-map frequency counter, the workhorse behind anagrams, uniqueness,
    top-K, etc. Two hand-rolled variants: explicit `if/else` vs `.get()`.
    """)
    return


@app.cell
def _():
    # Time: O(n)   Space: O(k)  (k = number of distinct chars, <= alphabet)
    # Explicit branch: check membership, then increment or seed to 1.
    def count_characters(s: str):
        count ={}
        for ch in s:
            if ch in count:
                count[ch] +=1
            else:
                count[ch] = 1
        return count

    # Same O(n) time / O(k) space, but .get(ch, 0) collapses the if/else:
    # missing key returns the default 0 instead of raising KeyError.
    def count_characters_get(s: str):
        count ={}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        return count

    print(count_characters('hello'))
    print(count_characters_get('hello'))
    return


if __name__ == "__main__":
    app.run()
