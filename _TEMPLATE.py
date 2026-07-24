# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

# ============================================================================
# TOPIC PREP TEMPLATE  (copy me -> dev/<topic>/<topic>.py)
# ----------------------------------------------------------------------------
# Skeleton for a digestible, self-contained interview-prep notebook.
# Fill in <TOPIC> and the sections; delete any Part you don't need.
#
# The proven structure (keep this order so every prep file reads the same):
#   TOC  ->  A: Fundamentals  ->  B: Perf trap  ->  C: Algorithms
#         ->  D: Applications  ->  Appendix (reference primers)
#
# Conventions used throughout:
#   - Every code cell annotates Time / Space (Big-O) in a comment.
#   - Show the brute-force AND the optimized form; name the trade-off.
#   - Inline `# expected result` comments on print() lines.
#   - Push deep reference material (bit tricks, cheat tables) to the Appendix.
#   - marimo detail: a cell's TOP-LEVEL names are globals and must be UNIQUE
#     across cells. Keep helpers/loop vars INSIDE functions to avoid clashes.
#     To share a value between cells, `return (name,)` it and accept it as a
#     parameter in the consuming cell: `def _(name):`.
# ============================================================================

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
    # <TOPIC> — interview prep notebook

    A self-contained reference. Each section is a short markdown header
    followed by a runnable cell. Read top-to-bottom the first time; jump by
    section when revisiting.

    ## Table of contents
    **Part A — Fundamentals**
    1. <foundational concept>
    2. <core mechanic / mental model>
    3. <key operations & complexity>
    4. <methods / API cheatsheet>

    **Part B — The performance trap**
    5. <the O(n^2)/O(n) gotcha for this topic> (benchmark)
    6. <the efficient idiom that fixes it>

    **Part C — Core algorithms**
    7. <classic algorithm A>
    8. <classic algorithm B>
    9. <classic algorithm C>

    **Part D — Applications**
    10. <application / composed problem A>
    11. <application / composed problem B>
    12. <application ladder: N approaches, readability -> efficiency>

    **Appendix**
    - <reference primer: the low-level trick this topic leans on>

    ---
    **Recurring theme:** <one-sentence big idea that ties the file together>.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part A — Fundamentals

    ### 1. <foundational concept>

    <Why this is the foundation everything else builds on.>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    # <what this demonstrates and why it matters>
    def example_fundamental(x):
        return x

    print(example_fundamental("demo"))  # expected: demo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. <core mechanic / mental model>

    <Use a fenced code block here for pure reference material — diagrams,
    "A vs B vs C" tables, or annotated pseudo-code that doesn't need to run.>

    ```
    <ascii diagram / mapping / rules go here>
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. <key operations & their complexity>

    <The 2-4 primitive operations for this topic and their Big-O.>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def example_operations(x):
        return x

    print(example_operations("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. <methods / API cheatsheet>

    Common built-ins worth having in muscle memory; each print shows the
    expected result inline.
    """)
    return


@app.cell
def _():
    # <stdlib methods for this type, one per line with expected output>
    print(len("hello"))  # 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part B — The performance trap

    ### 5. <the gotcha> (benchmark)

    <Name the trap for this topic and why the naive approach is slow. The
    benchmark below makes the asymptotic gap visible on large N.>
    """)
    return


@app.cell
def _():
    from time import perf_counter

    # perf_counter() is a high-resolution monotonic timer (seconds, float).
    # Small inputs are too fast to time; run each approach on a large N.
    def naive(n: int):
        # Time: O(?)  <-- the trap
        ...

    def optimized(n: int):
        # Time: O(?)  <-- the fix
        ...

    print(f"{'n':>8}  {'naive':>12}  {'optimized':>12}")
    for n in (10_000, 20_000, 40_000):
        t0 = perf_counter(); naive(n);     t_naive = perf_counter() - t0
        t0 = perf_counter(); optimized(n); t_opt = perf_counter() - t0
        print(f"{n:>8,}  {t_naive*1000:10.2f}ms  {t_opt*1000:10.2f}ms")

    # <what to watch: which column grows super-linearly as n doubles?>
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. <the efficient idiom that fixes it>

    <The practical takeaway from section 5, as a reusable pattern.>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def efficient_idiom(x):
        return x

    print(efficient_idiom("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part C — Core algorithms

    ### 7. <classic algorithm A>

    <One-line description + the trade-off between the variants shown.>
    """)
    return


@app.cell
def _():
    # Brute force -- Time: O(?)  Space: O(?)
    def algo_a_brute(x):
        return x

    # Optimized -- Time: O(?)  Space: O(?)   why it's better: <reason>
    def algo_a_optimal(x):
        return x

    print(algo_a_brute("demo"))
    print(algo_a_optimal("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. <classic algorithm B>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def algo_b(x):
        return x

    print(algo_b("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 9. <classic algorithm C>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def algo_c(x):
        return x

    print(algo_c("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part D — Applications

    ### 10. <application A>

    <A composed problem that reuses the fundamentals above. If it needs a
    value from an earlier cell, `return (thing,)` there and accept it here.>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def application_a(x):
        return x

    print(application_a("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 11. <application B>
    """)
    return


@app.cell
def _():
    # Time: O(?)   Space: O(?)
    def application_b(x):
        return x

    print(application_b("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 12. <application ladder: N approaches>

    Walk the SAME problem up the readability -> efficiency ladder and name the
    trade-off at each rung (this is a great "walk me through your options"
    interview answer). Point at the Appendix for any low-level trick used.
    """)
    return


@app.cell
def _():
    # Rung 1 — most readable   -- Time: O(?)  Space: O(?)
    def solve_v1(x):
        return x

    # Rung 2 — early exit      -- Time: O(?) best / O(?) worst   Space: O(?)
    def solve_v2(x):
        return x

    # Rung 3 — most efficient  -- Time: O(?)  Space: O(?)  (constraint: <...>)
    def solve_v3(x):
        return x

    print(solve_v1("demo"))
    print(solve_v2("demo"))
    print(solve_v3("demo"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Appendix — <reference primer>

    Deep reference for the low-level trick this topic leans on. Keep it out of
    the main flow so sections 1-12 stay skimmable, but colocated so it's one
    scroll away when you need it.

    <primer body: build from first principles, worked example, a quick-lookup
    table of the 2-3 operations, and the top gotchas.>

    | Operation | How | Meaning |
    |---|---|---|
    | <op> | `<code>` | <what it does> |
    """)
    return


if __name__ == "__main__":
    app.run()
