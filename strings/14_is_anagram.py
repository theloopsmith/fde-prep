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
    # 14 · Anagram

    Two strings are anagrams if they contain the same characters with the same
    frequencies, in any order. It's a frequency-counter problem. Three tiers:
    `Counter` equality (O(n)) -> `sorted()` (O(n log n), no imports) -> the
    case/space-insensitive follow-up (the "real world" definition).
    """)
    return


@app.cell
def _():
    from collections import Counter

    # Tier 1 -- Counter equality. An anagram = same characters with the same
    # frequencies, in any order. Comparing two Counters tests exactly that:
    # equal keys AND equal counts (Counter == Counter is a dict comparison, so
    # order doesn't matter). Different lengths -> unequal counts -> False.
    # Time: O(n)   Space: O(k)  (k = distinct chars; builds two frequency maps)
    def is_anagram(s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

    # Tier 2 -- sorted() comparison. Anagrams sort to the identical sequence.
    # No imports, one line, but the sort makes it O(n log n) -- asymptotically
    # slower than the Counter's O(n). Nice to know as the "no stdlib" fallback.
    # Time: O(n log n)   Space: O(n)  (sorted() builds two lists)
    def is_anagram_sorted(s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

    # Follow-up -- the "real world" anagram: ignore case and spaces, so
    # "Listen" / "Silent" and "Dormitory" / "Dirty Room" count as anagrams.
    # casefold() for robust case-insensitive matching; strip spaces first.
    # Time: O(n)   Space: O(k)
    def is_anagram_normalized(s1: str, s2: str) -> bool:
        def clean(s: str) -> str:
            # casefold: caseless compare, folds ß->ss (stronger than lower())
            return s.casefold().replace(" ", "")
        return Counter(clean(s1)) == Counter(clean(s2))

    print(is_anagram('racecar', 'carrace'))                  # True
    print(is_anagram('hello', 'world'))                      # False
    print(is_anagram('abc', 'ab'))                           # False (len differs)
    print(is_anagram_sorted('racecar', 'carrace'))           # True
    print(is_anagram_normalized('Listen', 'Silent'))         # True
    print(is_anagram_normalized('Dormitory', 'Dirty Room'))  # True
    return


if __name__ == "__main__":
    app.run()
