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
    # Appendix · Bitwise operators primer (`<<`, `|`, `&`, `|=`, `~`)

    An integer is secretly a row of on/off switches (bits). Each bit is a
    power of 2, read right-to-left:

    ```
    decimal 13 = binary 1101 = 8 + 4 + 0 + 1
                        ↑↑↑↑
                        8 4 2 1
    ```

    **`<<` left shift** — slide bits left, filling zeros on the right.
    `1 << n` builds a number with exactly ONE bit on, at position n
    (this is how you make a single-bit "mask"):

    ```
    1 << 0 = 0001 = 1
    1 << 1 = 0010 = 2
    1 << 2 = 0100 = 4
    1 << 3 = 1000 = 8
    ```

    **`|` OR** — result bit is 1 if EITHER input bit is 1. Used to turn a
    bit ON without disturbing the others:

    ```
      0101 (5)
    | 0011 (3)
      ----
      0111 (7)
    ```

    **`&` AND** — result bit is 1 only if BOTH are 1. Used to TEST a bit:
    `mask & (1 << n)` is nonzero only if bit n is already set.

    **`|=` compound assign** — `mask |= x` is just `mask = mask | x`, exactly
    like `+=`. It records "seen this" by OR-ing the new bit into `mask`.

    ### The "integer as a set" toolkit
    | Operation | Bit trick | Meaning |
    |---|---|---|
    | Add element n | `mask \|= (1 << n)` | turn bit n on |
    | Test element n | `mask & (1 << n)` | is bit n on? |
    | Remove element n | `mask &= ~(1 << n)` | turn bit n off |

    Each op is a single O(1) CPU instruction. This idiom powers `bitmask DP`
    (e.g. traveling salesman), permission flags (`READ | WRITE`), and the
    `all_unique_bitmask` function in 12_uniqueness_and_first_unique.py.
    Gotcha: `1 << -1` raises ValueError, and don't confuse bitwise `& |` with
    logical `and / or`.

    ### `~` bitwise NOT and two's complement
    `~` flips every bit. Because computers store negatives in **two's
    complement** (`-x == ~x + 1`), flipping bits gives the identity:

    ```
    ~x == -(x + 1)

    ~0 == -1     ~1 == -2     ~5 == -6     ~(-1) == 0
    ```

    This is why `s[~i]` mirrors `s[i]` from the back of a sequence: `~0` is
    `-1` (last element), `~1` is `-2` (2nd-last), etc. Two's complement also
    lets a CPU compute `a - b` as `a + (~b + 1)` using the same adder as
    addition -- no separate subtraction circuit, and only one representation
    of zero. Note: `~True == -2` (since `True == 1`); `~` is NOT logical `not`.
    """)
    return


if __name__ == "__main__":
    app.run()
