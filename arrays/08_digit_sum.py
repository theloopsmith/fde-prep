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
    # 08 · Sum the digits of a number (modulo/divide warm-up)

    Not an array problem, but the `% 10` / `// 10` digit-peeling loop is a
    classic warm-up worth keeping in muscle memory.
    """)
    return


@app.cell
def _():
    def digit_sum(N):
        total = 0
        while N > 0:        # loops once per digit
            total += N % 10  # grab last digit
            N //= 10         # drop last digit
        return total

    print(digit_sum(1234))
    return


if __name__ == "__main__":
    app.run()
