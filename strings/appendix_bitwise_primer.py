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

    Mental model: **an integer is secretly a row of on/off switches (bits).**
    Each bit is a power of 2, read right-to-left:

    ```
    decimal 13 = binary 1101 = 8 + 4 + 0 + 1
                        ↑↑↑↑
                        8 4 2 1
    ```

    Run the cell below to see it. `bin(n)` shows the binary string (the `0b`
    prefix just means "this is binary"); `format(n, "04b")` pads to 4 digits.
    """)
    return


@app.cell
def _():
    # See the bits behind a number.
    print(bin(13))              # 0b1101
    print(format(13, "08b"))    # 00001101  (padded to 8 columns)
    print(format(5, "04b"))     # 0101
    print(format(3, "04b"))     # 0011
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `<<` left shift — build a single-bit mask

    Slide the bits left, filling zeros on the right. `1 << n` makes a number
    with exactly ONE bit on, at position `n`. This is how you create a
    single-bit "mask" that stands for element `n`:

    ```
    1 << 0 = 0001 = 1
    1 << 1 = 0010 = 2
    1 << 2 = 0100 = 4
    1 << 3 = 1000 = 8
    ```
    """)
    return


@app.cell
def _():
    # 1 << n = "a number whose only ON bit is at position n" = 2**n
    for shift_n in range(5):
        mask = 1 << shift_n
        print(f"1 << {shift_n} = {mask:>2}  = {format(mask, '05b')}")
    # 1 << 0 =  1  = 00001
    # 1 << 1 =  2  = 00010
    # 1 << 2 =  4  = 00100
    # 1 << 3 =  8  = 01000
    # 1 << 4 = 16  = 10000
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `|` OR — turn a bit ON (union)

    Result bit is 1 if EITHER input bit is 1. Use it to switch a bit on
    without disturbing the others:

    ```
      0101 (5)
    | 0011 (3)
      ----
      0111 (7)
    ```
    """)
    return


@app.cell
def _():
    or_result = 5 | 3
    print(f"{format(5, '04b')} | {format(3, '04b')} = {format(or_result, '04b')} = {or_result}")
    # 0101 | 0011 = 0111 = 7

    # "READ | WRITE" style permission flags: combine independent bits
    READ, WRITE, EXEC = 1 << 0, 1 << 1, 1 << 2     # 1, 2, 4
    perms = READ | WRITE
    print(f"perms = {format(perms, '03b')} = {perms}")   # 011 = 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `&` AND — TEST whether a bit is on (membership)

    Result bit is 1 only if BOTH are 1. `mask & (1 << n)` is nonzero **only if
    bit n is already set** — that's your "is element n present?" check.
    """)
    return


@app.cell
def _():
    seen = 0b0101          # bits 0 and 2 are on
    print(bool(seen & (1 << 0)))   # True  — bit 0 is set
    print(bool(seen & (1 << 1)))   # False — bit 1 is off
    print(bool(seen & (1 << 2)))   # True  — bit 2 is set
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `|=` compound assign — record "seen this"

    `mask |= x` is exactly `mask = mask | x`, just like `+=`. It OR-s the new
    bit into `mask`, so the bit stays on. This is the workhorse of "have I
    seen this character before?" trackers (see `12_uniqueness_and_first_unique.py`).
    """)
    return


@app.cell
def _():
    # Track which lowercase letters we've seen using ONE integer as a bitset.
    tracker = 0
    for ch in "abca":
        bit = 1 << (ord(ch) - ord("a"))   # a->bit0, b->bit1, c->bit2
        if tracker & bit:
            print(f"duplicate: {ch!r}")   # duplicate: 'a'
        tracker |= bit                    # mark it seen
    print(format(tracker, "05b"))         # 00111  (a, b, c all seen)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The "integer as a set" toolkit

    | Operation | Bit trick | Meaning |
    |---|---|---|
    | Add element n | `mask \|= (1 << n)` | turn bit n on |
    | Test element n | `mask & (1 << n)` | is bit n on? |
    | Remove element n | `mask &= ~(1 << n)` | turn bit n off |

    Each op is a single O(1) CPU instruction. This idiom powers **bitmask DP**
    (e.g. traveling salesman), permission flags, and set membership in tight
    loops. Run all three operations below.
    """)
    return


@app.cell
def _():
    bag = 0
    bag |= (1 << 3)                 # add element 3
    print("after add 3 :", format(bag, "05b"), "->", bool(bag & (1 << 3)))  # 01000 -> True
    bag |= (1 << 1)                 # add element 1
    print("after add 1 :", format(bag, "05b"))                              # 01010
    bag &= ~(1 << 3)                # remove element 3
    print("after rm  3 :", format(bag, "05b"), "->", bool(bag & (1 << 3)))  # 00010 -> False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `~` bitwise NOT and two's complement

    `~` flips every bit. Because computers store negatives in **two's
    complement** (`-x == ~x + 1`), flipping bits gives this clean identity:

    ```
    ~x == -(x + 1)

    ~0 == -1     ~1 == -2     ~5 == -6     ~(-1) == 0
    ```

    This is why `s[~i]` mirrors `s[i]` from the back: `~0` is `-1` (last),
    `~1` is `-2` (2nd-last), etc. It's the trick used in the Pythonic
    palindrome check in `13_palindrome.py`.
    """)
    return


@app.cell
def _():
    for x in (0, 1, 5, -1):
        print(f"~{x:>2} = {~x:>3}   (checks out: -({x}+1) = {-(x + 1)})")
    # ~ 0 =  -1   (checks out: -(0+1) = -1)
    # ~ 1 =  -2   (checks out: -(1+1) = -2)
    # ~ 5 =  -6   (checks out: -(5+1) = -6)
    # ~-1 =   0   (checks out: -(-1+1) = 0)

    # s[~i] walks from the back — mirror index of a sequence
    word = "abcd"
    print([word[~i] for i in range(len(word))])   # ['d', 'c', 'b', 'a']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Edge cases & gotchas

    1. **`1 << -1` raises ValueError** — negative shift counts are illegal.
    2. **Bitwise `& | ~` are NOT logical `and / or / not`.** `5 & 3 == 1`
       (bit math), but `5 and 3 == 3` (returns the second truthy operand).
    3. **`~True == -2`** because `True == 1`; `~` is bit-flip, not boolean not.
    4. **Bitset only scales to small, dense integer domains** (e.g. 26 letters,
       ≤64 items fits one machine word). For arbitrary keys, use a real `set`.
    5. **Precedence surprise:** `&`, `|`, `^` bind *looser* than `==`, so
       `x & 1 == 0` parses as `x & (1 == 0)`. Always parenthesize: `(x & 1) == 0`.

    ### Staff-level takeaway
    A bitmask trades **readability for raw speed and memory**: it packs a whole
    set into one integer that lives in a CPU register, so add/test/remove are
    single instructions with zero heap allocation. Reach for it when the domain
    is small and fixed and the operation is hot (DP states, feature flags,
    permission systems). Everywhere else, a `set` is clearer — and naming the
    tradeoff out loud ("I'd use a bitmask here because N ≤ 26 and this is the
    inner loop") is exactly the kind of judgment interviewers listen for.
    """)
    return


if __name__ == "__main__":
    app.run()
