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
    # 02 · Slicing (`start:stop:step`)

    `arr[start:stop:step]` returns a NEW list. `stop` is exclusive; negative
    indices count from the end; `step` can skip or (when negative) reverse.
    See appendix_slicing_primer.py for the full primer.
    """)
    return


@app.cell
def _():
    k = [1,2,3,4,5,6,7]

    print(k[:])
    print(k[1:])
    print(k[2:-2:3])
    return


if __name__ == "__main__":
    app.run()
