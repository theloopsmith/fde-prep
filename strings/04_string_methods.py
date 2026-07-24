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
    # 04 · String methods cheatsheet

    Common built-ins worth having in muscle memory. Each print shows the
    expected result inline.
    """)
    return


@app.cell
def _():
    # Length and checking
    text = "hello"
    print(len(text))           # 5
    print(text.isalpha())      # True
    print(text.isdigit())      # False
    print("123".isdigit())     # True

    # Case methods
    print("hello".capitalize())     # "Hello"
    print("hello world".title())    # "Hello World"

    # Padding
    print("42".zfill(5))            # "00042"
    print("left".ljust(10, "-"))    # "left------"
    print("right".rjust(10, "-"))   # "-----right"

    # Splitting variations
    print("a,b,,c".split(","))      # ['a', 'b', '', 'c']
    print("line1\nline2".splitlines())  # ['line1', 'line2']
    return


if __name__ == "__main__":
    app.run()
