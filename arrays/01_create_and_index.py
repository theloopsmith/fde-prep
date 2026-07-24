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
    # 01 · Creating & indexing a list

    `[0] * n` builds a length-n list of zeros. Indexing is O(1). Note the loop
    below starts at index 1, so it intentionally skips `ar[0]`.
    """)
    return


@app.cell
def _():
    ar = [0] * 5
    print(ar)
    print('ok')
    for i in range(1,5):
        print(ar[i])
    return


if __name__ == "__main__":
    app.run()
