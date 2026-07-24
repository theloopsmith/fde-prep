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
    # 03 · Mutate in place vs Rebind vs Copy

    The mental model that decides whether the *caller* sees your change. This
    is the crux of the remove-element bug in 04_remove_elements.py.

    ```
      name  = value      -> REBIND: local name points at a new list;
                            the caller's original list is UNTOUCHED.
      name[:] = value    -> MUTATE IN PLACE: same list object, new contents;
                            the caller SEES the change.
      value[:] / list(value) / value.copy()
                         -> COPY: an independent list.

      a = [9, 9]         # rebind local name only (caller unaffected)
      a[:] = [9, 9]      # mutate caller's list in place (caller sees it)
      b = a              # ALIAS: same list -> mutating one shows in both
      b = a[:]           # COPY: independent list (also list(a) / a.copy())

    SHALLOW vs DEEP (nested lists):
      a[:], list(a), a.copy()  -> shallow: outer copied, inner shared
      copy.deepcopy(a)         -> fully independent (inner objects copied)
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
