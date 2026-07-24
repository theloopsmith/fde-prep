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
    # 05 · Why `+=` in a loop is O(n²) (benchmark)

    `+=` on an immutable str builds a brand-new string each iteration, copying
    all chars so far. The benchmark below makes the O(n²) vs O(n) gap visible.
    """)
    return


@app.cell
def _():
    from time import perf_counter

    s = "Hello World"

    # Inefficient: += on an immutable str builds a brand-new string each
    # iteration, copying all chars so far. Total work 1+2+...+n = O(n^2)
    # time, O(n) space. (CPython sometimes optimizes this to O(n) in-place,
    # but you can't rely on it.)
    result = ""
    for ch in s:
        result += ch + " "
    print(result)

    # Efficient: build a list of pieces (O(n)) then join once.
    # join walks all pieces a single time and allocates the result once.
    # Time: O(n)   Space: O(n)
    pieces = [ch for ch in s]
    result = " ".join(pieces)
    print(result)

    # ---- Benchmark: measure the O(n^2) vs O(n) gap ----
    # "Hello World" (11 chars) is far too small to time meaningfully, so we
    # run each approach on a large N and compare wall-clock time.
    # perf_counter() is a high-resolution monotonic timer (seconds, float).
    #
    # IMPORTANT CAVEAT: CPython special-cases `out += x` when `out` is the
    # SOLE reference to the string -- it resizes the buffer in place, so the
    # APPEND case runs in ~O(n), NOT the O(n^2) you'd expect. To actually
    # observe O(n^2) we also PREPEND (`out = x + out`), which cannot reuse the
    # buffer and must copy the whole string every step.
    def concat_append(n: int) -> str:
        out = ""
        for i in range(n):
            out += "x"                 # CPython optimizes this -> ~O(n)
        return out

    def concat_prepend(n: int) -> str:
        out = ""
        for i in range(n):
            out = "x" + out            # forces a full copy each step -> O(n^2)
        return out

    def concat_join(n: int) -> str:
        return "".join("x" for i in range(n))   # single pass -> O(n)

    print(f"{'n':>8}  {'append(+=)':>12}  {'prepend':>12}  {'join':>10}")
    for n in (10_000, 20_000, 40_000):
        t0 = perf_counter(); concat_append(n);  t_app = perf_counter() - t0
        t0 = perf_counter(); concat_prepend(n); t_pre = perf_counter() - t0
        t0 = perf_counter(); concat_join(n);    t_join = perf_counter() - t0
        print(
            f"{n:>8,}  {t_app*1000:10.2f}ms  {t_pre*1000:10.2f}ms  "
            f"{t_join*1000:8.2f}ms"
        )

    # Watch the 'prepend' column ~4x each time n doubles (classic O(n^2)),
    # while 'append' and 'join' only ~2x (linear).
    return


if __name__ == "__main__":
    app.run()
