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
    # 02 · Copy vs Rebind vs Overwrite

    A mental model that trips up even senior engineers. The key distinction:
    does an operation create a NEW object, mutate the SAME object in place, or
    just point a name somewhere else?

    ```
    Core idea:
      name  = value      -> REBIND: local name points at a new object;
                            the caller's original object is untouched.
      name[:] = value    -> OVERWRITE IN PLACE: same object, new contents;
                            the caller SEES the mutation. (mutable only)
      value[:] / list(value) / value.copy()
                         -> NEW COPY: an independent object.

    LISTS (mutable):
      a = [9, 9]         # rebind local name only (caller unaffected)
      a[:] = [9, 9]      # mutate caller's list in place (caller sees it)
      b = a              # ALIAS: same list -> mutating one shows in both
      b = a[:]           # COPY: independent list (also list(a) / a.copy())

    STRINGS (immutable): no in-place overwrite exists.
      s = s[::-1]        # rebind to a NEW string; original is discarded
      s[:] = "x"         # TypeError: str doesn't support item assignment
      s[:]               # just returns the same string (safe to share)
      -> out = s[::-1] is ALWAYS a new object.

    SHALLOW vs DEEP (nested structures):
      a[:], list(a), a.copy()  -> shallow: outer copied, inner shared
      copy.deepcopy(a)         -> fully independent (inner objects copied)
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
