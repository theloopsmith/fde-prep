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
    # 12 · `Counter` applications: all-unique (5 ways) & first-unique char

    "Are all characters unique?" walked up the readability↔efficiency ladder:
    `Counter` -> `all()` -> `len(set())` -> incremental `seen` set -> bitmask.
    Plus `first_unique`, which re-walks the string IN ORDER. See the bitwise
    primer file for the bit operations used in `all_unique_bitmask`.
    """)
    return


@app.cell
def _():
    from collections import Counter

    # Explicit version: tally with Counter, then scan the counts for any > 1.
    # The sorted-print loop is just for inspection/debugging, not the logic.
    # Time: O(n)   Space: O(k)   (k = distinct chars). Note: the sort adds
    # O(k log k), so drop it in a real solution -- it's here for readability.
    def all_unique_scan(s: str):
        freq = Counter(s)
        print(freq)
        for key in sorted(freq.keys()):   # sorted() only to print keys in order
            print(key, freq[key])

        for ch in freq:                   # iterating a Counter yields its keys
            if freq.get(ch, 0) > 1:       # any char seen more than once -> not unique
                return False
        return True

    # Same idea as a one-liner. all(...) is True only if EVERY count == 1;
    # it short-circuits (returns False) at the first duplicate it finds.
    # The generator (no []) keeps the check lazy -> O(1) extra space.
    # Time: O(n)   Space: O(k)  (the Counter)
    def all_unique_counter(s):
        freq = Counter(s)
        return all(count == 1 for count in freq.values())

    # Slickest form: a set drops duplicates, so if no chars repeated the set
    # has the same size as the string. No counts needed at all.
    # Time: O(n)   Space: O(k)   -- but always builds the FULL set first
    # (no early exit), so it scans every char even when a dup appears early.
    def all_unique_set(s):
        return len(set(s)) == len(s)

    # Best early-exit form: build a `seen` set incrementally and bail the
    # instant a repeat shows up. Best case O(1) (first two chars match);
    # worst case O(n) for an all-unique string.
    # Time: O(n) worst / O(1) best   Space: O(k)
    def all_unique_seen(s):
        seen = set()
        for ch in s:
            if ch in seen:        # O(1) average membership test
                return False      # short-circuit: duplicate found, stop early
            seen.add(ch)
        return True

    # Bitmask form: for a FIXED alphabet (here lowercase a-z) we can track
    # "have I seen this char?" in the bits of a single integer instead of a
    # set -- true O(1) extra space (one int), no hashing overhead.
    #
    # How it works:
    #   bit = ord(ch) - ord('a')   maps 'a'->0, 'b'->1, ... 'z'->25
    #   1 << bit                   a mask with only that char's bit set
    #   mask & (1 << bit)          nonzero -> that bit already on -> duplicate
    #   mask |= (1 << bit)         turn the bit on to record we've seen it
    # Also short-circuits on the first repeat, like the seen-set version.
    # Time: O(n) worst / O(1) best   Space: O(1)  (single integer)
    # CAVEAT: only valid for the assumed alphabet; other chars give wrong
    # bit positions. Assert or fall back to a set for arbitrary Unicode.
    def all_unique_bitmask(s):
        mask = 0
        for ch in s:
            bit = ord(ch) - ord('a')
            if mask & (1 << bit):     # bit already set -> seen before
                return False
            mask |= (1 << bit)        # record this char
        return True

    # Find first non-repeating character.
    # Two passes: (1) Counter tallies all frequencies, (2) re-walk s IN ORDER
    # and return the first char whose total count is 1. Iterating `s` (not the
    # Counter) is what preserves original order. Returns None if none exist.
    # Time: O(n)   Space: O(k)
    def first_unique(s):
        freq = Counter(s)
        for char in s:
            if freq[char] == 1:
                return char
        return None

    print(all_unique_scan('hello'))
    print(all_unique_counter('hello'))
    print(all_unique_set('hello'))      # False
    print(all_unique_seen('hello'))     # False (bails at 2nd 'l')
    print(all_unique_seen('abc'))       # True
    print(all_unique_bitmask('hello'))  # False
    print(all_unique_bitmask('abc'))    # True
    print(first_unique('leetcode'))     # 'l'
    return


if __name__ == "__main__":
    app.run()
