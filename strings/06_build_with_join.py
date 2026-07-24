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
    # 06 · Building strings efficiently with `join`

    The practical takeaway from the `+=` trap: accumulate pieces in a list,
    then `join` once. The timing here confirms the speedup on repeated runs.
    """)
    return


@app.cell
def _():
    def concat_string_naive(s: str):
        # Inefficient: creates many temporary strings
        result = ""
        for i in range(1000):
            result += str(i) + " "
        return result

    def concat_string_join(s: str):
        # Efficient: join builds once
        pieces = [str(i) for i in range(1000)]
        result = " ".join(pieces)
        return result

    # ---- Timers: measure the inefficiency ----
    # Wrapped in a local function so its names (perf_counter, timers, loop
    # vars) stay LOCAL and don't clash with other marimo cells -- marimo
    # treats a cell's top-level names as globals and forbids duplicates.
    # Each call is tiny (1000 items), so one run is too fast to time reliably;
    # we repeat each function `repeats` times and report total + per-call time.
    def time_concat(repeats: int = 2000):
        from time import perf_counter

        t0 = perf_counter()
        for _ in range(repeats):
            concat_string_naive('hello')
        t_ineff = perf_counter() - t0

        t0 = perf_counter()
        for _ in range(repeats):
            concat_string_join('hello')
        t_eff = perf_counter() - t0

        print(f"inefficient (+=):  {t_ineff*1000:8.2f} ms total  "
              f"({t_ineff/repeats*1e6:6.1f} us/call)")
        print(f"efficient (join):  {t_eff*1000:8.2f} ms total  "
              f"({t_eff/repeats*1e6:6.1f} us/call)")
        print(f"+= is {t_ineff/t_eff:.2f}x slower")

    print(concat_string_naive('hello'))
    print(concat_string_join('hello'))
    time_concat()
    return


if __name__ == "__main__":
    app.run()
