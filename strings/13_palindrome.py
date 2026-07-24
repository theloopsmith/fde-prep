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
    # 13 · Palindrome checks

    The canonical converging two-pointers problem. Four tiers:
    slice (readable, O(n) space) -> two pointers (O(1) space, early exit) ->
    the `~i` one-liner (Pythonic AND O(1) space) -> the "valid palindrome"
    follow-up that skips non-alphanumerics (where two pointers beat a slice).
    """)
    return


@app.cell
def _():
    # Tier 1 -- Pythonic slice. Clean, but O(n) SPACE (builds a reversed copy)
    # and always scans the whole string (no early exit).
    # Time: O(n)   Space: O(n)
    def is_palindrome_slice(s: str) -> bool:
        rev: str = s[::-1]
        return s == rev

    # Tier 2 -- Two pointers converging from both ends. The interview answer:
    # O(1) space and short-circuits on the first mismatch. `while left < right`
    # stops at the middle (~n/2 comparisons) and keeps the indices in range by
    # construction -- no bounds guard needed.
    # Time: O(n)   Space: O(1)
    def is_palindrome_two_pointer(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False        # short-circuit on first mismatch
            left += 1
            right -= 1
        return True

    # Tier 3 -- Pythonic AND O(1) space. `~i` indexes from the back
    # (~0 == -1, ~1 == -2, ...), so s[i] vs s[~i] compares mirror positions.
    # all() short-circuits on the first False; range(len(s)//2) = ~n/2 checks.
    # Time: O(n)   Space: O(1)
    def is_palindrome_pythonic(s: str) -> bool:
        # ~i == -(i+1), so s[~i] is the mirror of s[i] from the back
        return all(s[i] == s[~i] for i in range(len(s) // 2))

    # Follow-up (LeetCode 125) -- "valid palindrome": ignore case and skip
    # non-alphanumeric chars. Two pointers shine here because we can advance
    # past punctuation IN PLACE -- a slice-reverse can't do that cleanly.
    # Walk each pointer past non-alnum chars, then compare casefolded.
    # Time: O(n)   Space: O(1)
    def is_valid_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].casefold() != s[right].casefold():
                return False
            left += 1
            right -= 1
        return True

    print(is_palindrome_slice('racecar'))                        # True
    print(is_palindrome_two_pointer('racecar'))                  # True
    print(is_palindrome_two_pointer('oko'))                      # True
    print(is_palindrome_two_pointer('hello'))                    # False
    print(is_palindrome_pythonic('racecar'))                     # True
    print(is_valid_palindrome('A man, a plan, a canal: Panama')) # True
    print(is_valid_palindrome('race a car'))                     # False
    return


if __name__ == "__main__":
    app.run()
