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
    # 06 · Count occurrences of a target

    Write a function that counts how many times a target value appears in an
    array of integers.
    """)
    return


@app.cell
def _():
    def findOccurences(arr: list[int], key):
        occ = 0
        for i in arr:
            if i == key:
                occ += 1
        return occ

    print(findOccurences([2,21,-9,8,11, 21, 21], 21))
    return


if __name__ == "__main__":
    app.run()
