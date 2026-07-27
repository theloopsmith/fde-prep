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
    # Appendix · `str.maketrans` + `str.translate`

    Mental model: **`maketrans` BUILDS a lookup table (a dict keyed by code
    point); `translate` APPLIES it** in one C-level pass.

    `translate` walks the string once and, for each char, looks up `ord(ch)`
    in the table:
    - maps to a new char/string -> substitute it
    - maps to `None`            -> delete it
    - not in the table          -> keep it unchanged

    `maketrans` has three call forms, shown in the cells below.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Form 1 — two strings: `maketrans(from, to)`

    One-to-one replacement. The two strings MUST be equal length; `from[i]`
    maps to `to[i]`. (Unequal lengths raise ValueError.)
    """)
    return


@app.cell
def _():
    # a->1, e->2, i->3, o->4, u->5
    # (unique var name per cell: marimo requires one owner cell per global)
    swap_table = str.maketrans("aeiou", "12345")
    print("hello world".translate(swap_table))   # 'h2ll4 w4rld'

    # simple letter swap / cipher: a->x, b->y, c->z
    swap_table = str.maketrans("abc", "xyz")
    print("cab".translate(swap_table))            # 'zxy'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Form 2 — a dict: `maketrans({...})`

    Most flexible. Keys can be characters OR code points; values can be a
    string, a code point, or `None` (delete). This is the ONLY form that can
    map one char to MULTIPLE chars.
    """)
    return


@app.cell
def _():
    # leetspeak-ish single-char replacements
    dict_table = str.maketrans({"a": "4", "s": "$", "o": "0"})
    print("associate".translate(dict_table))          # '4$$0ci4te'

    # one char -> many chars (only the dict form allows this)
    dict_table = str.maketrans({"&": "and", "@": "at"})
    print("you & me @ noon".translate(dict_table))     # 'you and me at noon'

    # map to None = delete
    dict_table = str.maketrans({" ": None})
    print("a b c".translate(dict_table))               # 'abc'  (spaces removed)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Form 3 — three strings: `maketrans(from, to, delete)`

    Replace AND delete in one table. The third argument is a set of characters
    to drop entirely. This is the vowel-removal case from 08_count_vowels.py.
    """)
    return


@app.cell
def _():
    # replace nothing, delete all vowels (both cases listed explicitly)
    del_table = str.maketrans("", "", "aeiouAEIOU")
    print("Hello World".translate(del_table))    # 'Hll Wrld'

    # do both: replace o->0 AND delete spaces
    del_table = str.maketrans("o", "0", " ")
    print("foo bar boo".translate(del_table))     # 'f00barb00'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What the table actually IS

    Just a dict from **code point -> replacement**. These are all equivalent
    ways to say "delete `a`" (97 == ord('a')):

    ```python
    str.maketrans("", "", "a")   # {97: None}
    str.maketrans({"a": None})   # {97: None}
    str.maketrans({97: None})    # {97: None}
    ```
    """)
    return


@app.cell
def _():
    print(str.maketrans("", "", "a"))   # {97: None}
    print(str.maketrans({"a": None}))   # {97: None}
    print(str.maketrans({97: None}))    # {97: None}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practical one-liners
    """)
    return


@app.cell
def _():
    import string

    # remove all digits
    print("a1b2c3".translate(str.maketrans("", "", "0123456789")))   # 'abc'

    # strip punctuation (string.punctuation is a ready-made set of it)
    print("Hello, World!".translate(str.maketrans("", "", string.punctuation)))  # 'Hello World'

    # Caesar-ish substitution cipher: a->b, b->c, ... z->a
    shifted = string.ascii_lowercase[1:] + string.ascii_lowercase[0]
    print("abc xyz".translate(str.maketrans(string.ascii_lowercase, shifted)))   # 'bcd yza'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Edge cases & gotchas

    1. **Two-string form requires equal lengths** — `maketrans("ab", "x")`
       raises ValueError. `from` and `to` must line up 1:1.
    2. **Only the dict form does one -> many** — `maketrans("&", "and")` fails
       (length mismatch); use `maketrans({"&": "and"})`.
    3. **Keys are code points under the hood** — `"a"` and `97` are
       interchangeable as dict keys; `translate` does `ord(ch)` lookups.
    4. **`translate` returns a NEW string** (immutable) — it never mutates `s`.
    5. **`bytes` has its own `translate`** with a different 256-entry table
       signature — don't mix up the `str` and `bytes` versions.

    ### Staff-level takeaway
    `maketrans` (build the plan) and `translate` (run the plan) are split for
    the same reason as `re.compile` vs `re.match`: **build the table ONCE,
    reuse it many times.** In a hot loop, hoist the table to module level:

    ```python
    _VOWELS = str.maketrans("", "", "aeiouAEIOU")   # built once
    def remove_vowels(s): return s.translate(_VOWELS)
    ```

    Recognizing this "compile-then-execute" split (translation tables,
    compiled regexes, prepared SQL statements, cached query plans) as a
    recurring performance pattern is a strong senior instinct.
    """)
    return


if __name__ == "__main__":
    app.run()
