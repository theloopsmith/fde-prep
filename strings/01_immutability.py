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
    # 01 · Immutability (the foundation)

    Strings can't be changed in place. Every "edit" builds a NEW object at a
    new address. `id(obj)` returns a unique, stable integer for an object's
    lifetime (in CPython, its memory address). The cell below proves it.
    """)
    return


@app.cell
def _():
    # Strings are immutable in Python
    t1 = "hello"

    # This raises TypeError - strings don't support item assignment
    # t1[0] = 'H'  # Error!

    # ---- Getting a string's memory address ----
    # id(obj) returns a unique, constant integer for the object's lifetime.
    # In CPython that integer IS the object's memory address. hex() shows it
    # in the usual address form. (CPython detail: the language only promises
    # id() is unique/stable, not that it's the address. id() itself is O(1).)
    addr_before = id(t1)
    print(f"t1 address before: {hex(addr_before)}")

    # Must create new string instead
    t1 = 'H' + t1[1:]
    print(t1)  # "Hello"

    # Immutability proof: rebinding built a NEW object at a DIFFERENT address.
    addr_after = id(t1)
    print(f"t1 address after:  {hex(addr_after)}")
    print(f"same object? {addr_before == addr_after}")  # False - new string

    # Each operation creates new string
    original = "hello"
    upper = original.upper()
    print(original)  # "hello" (unchanged)
    print(upper)     # "HELLO" (new string)
    # original is untouched; upper is a separate object at its own address.
    print(f"original: {hex(id(original))}  upper: {hex(id(upper))}")
    print(f"original is upper? {original is upper}")  # False (identity check)

    # Interning caveat: equal short/literal strings are often cached & shared,
    # so `is` (which compares id()) can be True for them, but not for strings
    # built at runtime.
    a = "hello"
    b = "hello"
    print(f"a is b (interned literals)? {a is b}")  # often True - same object
    return


if __name__ == "__main__":
    app.run()
