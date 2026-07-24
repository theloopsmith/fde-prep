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
    # 11 · Frequency with the stdlib: `defaultdict` & `Counter`

    Two stdlib alternatives to the manual counter. Same O(n) time, O(k) space,
    but less code and fewer chances to introduce a bug.
    """)
    return


@app.cell
def _():
    from collections import Counter, defaultdict

    # defaultdict(int): missing keys auto-initialize to int() == 0, so we can
    # do += without seeding first. No .get() and no if/else branch needed.
    def count_characters_defaultdict(s: str):
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1  # first touch of a key defaults to 0, then +1
        return dict(count)  # cast back to plain dict for clean printing

    # Counter: purpose-built for this. It consumes any iterable and tallies
    # occurrences in a single pass. This is the production-preferred one-liner.
    def count_characters_counter(s: str):
        return Counter(s)  # Counter('hello') -> Counter({'l': 2, 'h': 1, ...})

    # --- VVIMP: does a lookup MUTATE the container? ---
    # defaultdict's factory fires on READ of a missing key, so merely accessing
    # count[ch] INSERTS it with the default (0) even if you never increment --
    # defaultdict can silently grow your dict if you probe keys during a lookup.
    # Counter sidesteps this: Counter(s)['z'] returns 0 for a missing key
    # WITHOUT inserting it.
    # That distinction ("does a lookup mutate the container?") is a sharp
    # interview talking point.

    print(count_characters_defaultdict('hello'))
    print(count_characters_counter('hello'))
    print(count_characters_counter('hello')['l'])  # 2
    print(count_characters_counter('hello').most_common(1))  # [('l', 2)]
    return


if __name__ == "__main__":
    app.run()
