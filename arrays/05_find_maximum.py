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
    # 05 · Find the maximum

    One linear pass tracking the running max.
    """)
    return


@app.cell
def _():
    def findMax(arr: list[int]):
        max = -9999999
        for i in arr:
            if i > max:
                max = i
        return max  

    print(findMax([2,21,-9,8,11]))
    return


if __name__ == "__main__":
    app.run()
