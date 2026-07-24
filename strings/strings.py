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
    # Strings — interview prep notebook

    A self-contained reference. Each section is a short markdown header
    followed by a runnable cell. Read top-to-bottom the first time; jump by
    section when revisiting.

    ## Table of contents
    **Part A — Fundamentals**
    1. Immutability (the foundation)
    2. Copy vs Rebind vs Overwrite
    3. Character codes: `ord()` / `chr()` & lexicographic compare
    4. String methods cheatsheet

    **Part B — The `+=` performance trap**
    5. Why `+=` in a loop is O(n²) (benchmark)
    6. Building strings efficiently with `join`

    **Part C — Core algorithms**
    7. Reverse a string (3 ways)
    8. Count vowels
    9. Safely modify a char at an index

    **Part D — Frequency counting**
    10. Character frequency: manual dict
    11. Frequency with the stdlib: `defaultdict` & `Counter`
    12. `Counter` applications: all-unique (5 ways) & first-unique char

    **Appendix**
    - Bitwise operators primer (`<<`, `|`, `&`, `|=`)

    ---
    **Recurring theme:** strings are immutable, so `+=` in a loop rebuilds the
    whole string each step (O(n²)). The fix is almost always `join`, slicing,
    or a purpose-built container.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part A — Fundamentals

    ### 1. Immutability (the foundation)

    Strings can't be changed in place. Every "edit" builds a NEW object at a
    new address. `id(obj)` returns a unique, stable integer for an object's
    lifetime (in CPython, its memory address). The cell below proves it.
    """)
    return


@app.cell
def _():
    # Strings are immutable in Python
    t1 = "hello"

    # This raises TypeError - strings don't support item assignment
    # t1[0] = 'H'  # Error!

    # ---- Getting a string's memory address ----
    # id(obj) returns a unique, constant integer for the object's lifetime.
    # In CPython that integer IS the object's memory address. hex() shows it
    # in the usual address form. (CPython detail: the language only promises
    # id() is unique/stable, not that it's the address. id() itself is O(1).)
    addr_before = id(t1)
    print(f"t1 address before: {hex(addr_before)}")

    # Must create new string instead
    t1 = 'H' + t1[1:]
    print(t1)  # "Hello"

    # Immutability proof: rebinding built a NEW object at a DIFFERENT address.
    addr_after = id(t1)
    print(f"t1 address after:  {hex(addr_after)}")
    print(f"same object? {addr_before == addr_after}")  # False - new string

    # Each operation creates new string
    original = "hello"
    upper = original.upper()
    print(original)  # "hello" (unchanged)
    print(upper)     # "HELLO" (new string)
    # original is untouched; upper is a separate object at its own address.
    print(f"original: {hex(id(original))}  upper: {hex(id(upper))}")
    print(f"original is upper? {original is upper}")  # False (identity check)

    # Interning caveat: equal short/literal strings are often cached & shared,
    # so `is` (which compares id()) can be True for them, but not for strings
    # built at runtime.
    a = "hello"
    b = "hello"
    print(f"a is b (interned literals)? {a is b}")  # often True - same object
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Copy vs Rebind vs Overwrite

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Character codes: `ord()` / `chr()` & lexicographic compare

    `ord(c)` -> code point of a 1-char string; `chr(n)` -> char for int n.
    Both O(1). String comparison (`>`, `<`) is lexicographic by code point.
    """)
    return


@app.cell
def _():
    # ord() and chr() are both O(1) (constant time & space):
    #   - ord(c): reads the single character's already-stored code point;
    #             no scanning. Requires a length-1 string.
    #   - chr(n): builds/looks up the char for int n; small code points
    #             (<=255) return cached singletons -> just a table lookup.
    # Note: constant PER CALL. Applying ord over a whole string is O(n),
    # e.g. [ord(c) for c in s]. In hot loops, hoist constants like
    # base = ord('a') outside the loop to avoid repeated call overhead.
    def compareLexciographically(s1: str, s2: str):
        print(f"s1: {ord('a')} and s2: {ord('A')}")
        print(f"s1: {chr(97)} and s2: {chr(65)}")
        print(f"s1: {[ord(ch) for ch in s1] }")
        print(f"s2: {[ord(ch) for ch in s2] }")

        print(f"0 is {ord('0')}")
        test:str ='A'
        # Check if a char is a digit / uppercase via ranges
        print(f"ch: {test} - {ord('0') <= ord(test) <= ord('9')}")

        if s1 > s2:
            return 1
        if s1 < s2:
            return -1
        return 0

    print(compareLexciographically('a', 'A'))
    print(compareLexciographically('apple', 'Apple'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. String methods cheatsheet

    Common built-ins worth having in muscle memory. Each print shows the
    expected result inline.
    """)
    return


@app.cell
def _():
    # Length and checking
    text = "hello"
    print(len(text))           # 5
    print(text.isalpha())      # True
    print(text.isdigit())      # False
    print("123".isdigit())     # True

    # Case methods
    print("hello".capitalize())     # "Hello"
    print("hello world".title())    # "Hello World"

    # Padding
    print("42".zfill(5))            # "00042"
    print("left".ljust(10, "-"))    # "left------"
    print("right".rjust(10, "-"))   # "-----right"

    # Splitting variations
    print("a,b,,c".split(","))      # ['a', 'b', '', 'c']
    print("line1\nline2".splitlines())  # ['line1', 'line2']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part B — The `+=` performance trap

    ### 5. Why `+=` in a loop is O(n²) (benchmark)

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. Building strings efficiently with `join`

    The practical takeaway from section 5: accumulate pieces in a list, then
    `join` once. The timing here confirms the speedup on repeated runs.
    """)
    return


@app.cell
def _():
    def concatStringInefficient(s: str):
        # Inefficient: creates many temporary strings
        result = ""
        for i in range(1000):
            result += str(i) + " "
        return result

    def concatStringEfficient(s: str):
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
    def timeConcat(repeats: int = 2000):
        from time import perf_counter

        t0 = perf_counter()
        for _ in range(repeats):
            concatStringInefficient('hello')
        t_ineff = perf_counter() - t0

        t0 = perf_counter()
        for _ in range(repeats):
            concatStringEfficient('hello')
        t_eff = perf_counter() - t0

        print(f"inefficient (+=):  {t_ineff*1000:8.2f} ms total  "
              f"({t_ineff/repeats*1e6:6.1f} us/call)")
        print(f"efficient (join):  {t_eff*1000:8.2f} ms total  "
              f"({t_eff/repeats*1e6:6.1f} us/call)")
        print(f"+= is {t_ineff/t_eff:.2f}x slower")

    print(concatStringInefficient('hello'))
    print(concatStringEfficient('hello'))
    timeConcat()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part C — Core algorithms

    ### 7. Reverse a string (3 ways)

    Two O(n²) `+=` versions (to feel the trap) and the Pythonic O(n) slice.
    """)
    return


@app.cell
def _():
    # Time: O(n^2)  Space: O(n)
    # Walks indices back-to-front (n iterations), but res += s[i] rebuilds
    # the immutable string each time, copying the growing prefix -> O(n^2).
    # A Pythonic O(n) alternative is simply: return s[::-1]
    def reverse1(s: str):
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res

    # Time: O(n^2)  Space: O(n)  -- same += cost as reverse1.
    # Walks front-to-back (i = 0..n-1) but indexes from the back:
    # s[len(s)-i-1] maps i=0 -> last char, i=n-1 -> first char (s[0]).
    # The -1 keeps the index in range (max index is len(s)-1, not len(s)).
    def reverse2(s: str):
        res = ""
        for i in range(len(s)):
            res += s[len(s)-i-1]
        return res

    # Time: O(n)   Space: O(n)
    # Pythonic: slice with step -1 builds the reversed string in one C-level
    # pass and a single allocation -- no per-char += copying.
    def reverse3(s: str):
        return s[::-1]

    print(reverse1('hello world'))
    print(reverse2('hello world'))
    print(reverse3('hello world'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. Count vowels

    Explicit loop vs the Pythonic `sum()` of a boolean generator.
    """)
    return


@app.cell
def _():
    # Time: O(n)   Space: O(1)
    # One pass over the n chars; `i in vowels` scans a fixed 10-char string
    # (constant), and count is a single integer.
    def countVowels(s: str):
        vowels = 'aeiouAEIOU'
        count = 0
        for i in s:
            if i in vowels:
                count += 1
        return count

    # Pythonic: sum a generator of booleans. `ch in vowels` yields True/False,
    # and True == 1 / False == 0, so sum() counts the matches in one pass.
    # Using a set for O(1) membership and casefold() so both cases match
    # against a single lowercase set.
    # Time: O(n)   Space: O(1)  (fixed-size vowel set)
    def countVowelsPythonic(s: str):
        vowels = set('aeiou')
        return sum(ch in vowels for ch in s.casefold())

    print(countVowels('hello world'))            # 3
    print(countVowelsPythonic('hello world'))    # 3
    print(countVowelsPythonic('AEiou XYZ'))      # 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 9. Safely modify a char at an index

    Immutability means "editing" index i = building a new string from three
    slices. The bounds guard makes an out-of-range index a no-op.
    """)
    return


@app.cell
def _():
    # NOTE: pulling assert_equal from numpy.ma.testutils just for an equality
    # check drags in a heavy dependency. Prefer a plain `assert a == b` (or
    # the stdlib `unittest`) for a self-contained snippet.
    from numpy.ma.testutils import assert_equal

    # Strings are immutable, so "modifying" index i means BUILDING A NEW string
    # from three slices: everything before i, the replacement, everything after.
    # Time: O(n)   Space: O(n)  (slicing + concatenation each copy the chars).
    def safe_modify_string(s: str, index: int, new_char: str) -> str:
        # Bounds guard: out-of-range index returns the original unchanged
        # rather than raising -- hence "safe".
        if index >= 0 and index < len(s):
           # s[:index:1]  -> the `:1` step is redundant (1 is the default);
           #                 s[:index] reads the same.
           # s[index+1:len(s)] -> the `len(s)` is redundant; s[index+1:] reads
           #                 to the end. Kept as-is to match your original.
           return s[:index:1] + new_char + s[index+1:len(s)]       
        return s

    print(safe_modify_string('world', 2, 'X'))
    assert_equal(safe_modify_string('world', 2, 'X'), 'woXld')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part D — Frequency counting

    ### 10. Character frequency: manual dict

    The hash-map frequency counter, the workhorse behind anagrams, uniqueness,
    top-K, etc. Two hand-rolled variants: explicit `if/else` vs `.get()`.
    """)
    return


@app.cell
def _():

    # Time: O(n)   Space: O(k)  (k = number of distinct chars, <= alphabet)
    # Explicit branch: check membership, then increment or seed to 1.
    def countCharacters(s: str):
        count ={}
        for ch in s:
            if ch in count:
                count[ch] +=1
            else:
                count[ch] = 1
        return count

    # Same O(n) time / O(k) space, but .get(ch, 0) collapses the if/else:
    # missing key returns the default 0 instead of raising KeyError.
    def countCharacters2(s: str):
        count ={}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        return count

    print(countCharacters2('hello')) 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 11. Frequency with the stdlib: `defaultdict` & `Counter`

    Two stdlib alternatives to the manual counter. Same O(n) time, O(k) space,
    but less code and fewer chances to introduce a bug.
    """)
    return


@app.cell
def _():
    from collections import Counter, defaultdict

    # defaultdict(int): missing keys auto-initialize to int() == 0, so we can
    # do += without seeding first. No .get() and no if/else branch needed.
    def countCharacters3(s: str):
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1  # first touch of a key defaults to 0, then +1
        return dict(count)  # cast back to plain dict for clean printing

    # Counter: purpose-built for this. It consumes any iterable and tallies
    # occurrences in a single pass. This is the production-preferred one-liner.
    def countCharacters4(s: str):
        return Counter(s)  # Counter('hello') -> Counter({'l': 2, 'h': 1, ...})

    # --- VVIMP: does a lookup MUTATE the container? ---
    # defaultdict's factory fires on READ of a missing key, so merely accessing
    # count[ch] INSERTS it with the default (0) even if you never increment --
    # defaultdict can silently grow your dict if you probe keys during a lookup.
    # Counter sidesteps this: Counter(s)['z'] returns 0 for a missing key
    # WITHOUT inserting it.
    # That distinction ("does a lookup mutate the container?") is a sharp
    # interview talking point.

    print(countCharacters3('hello'))
    print(countCharacters4('hello'))
    print(countCharacters4('hello')['l'])  # 2
    print(countCharacters4('hello').most_common(1))  # [('l', 2)]
    return (Counter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 12. `Counter` applications: all-unique (5 ways) & first-unique char

    "Are all characters unique?" walked up the readability↔efficiency ladder:
    `Counter` -> `all()` -> `len(set())` -> incremental `seen` set -> bitmask.
    Plus `first_unique`, which re-walks the string IN ORDER. See the appendix
    for the bit operations used in `all_unique_bitmask`.
    """)
    return


@app.cell
def _(Counter):

    # Explicit version: tally with Counter, then scan the counts for any > 1.
    # The sorted-print loop is just for inspection/debugging, not the logic.
    # Time: O(n)   Space: O(k)   (k = distinct chars). Note: the sort adds
    # O(k log k), so drop it in a real solution -- it's here for readability.
    def allUnique(s: str):
        freq = Counter(s)
        print(freq)
        for key in sorted(freq.keys()):   # sorted() only to print keys in order
            print(key, freq[key])

        for ch in freq:                   # iterating a Counter yields its keys
            if freq.get(ch, 0) > 1:       # any char seen more than once -> not unique
                return False
        return True

    # Same idea as a one-liner. all(...) is True only if EVERY count == 1;
    # it short-circuits (returns False) at the first duplicate it finds.
    # The generator (no []) keeps the check lazy -> O(1) extra space.
    # Time: O(n)   Space: O(k)  (the Counter)
    def all_unique(s):
        freq = Counter(s)
        return all(count == 1 for count in freq.values())

    # Slickest form: a set drops duplicates, so if no chars repeated the set
    # has the same size as the string. No counts needed at all.
    # Time: O(n)   Space: O(k)   -- but always builds the FULL set first
    # (no early exit), so it scans every char even when a dup appears early.
    def all_unique_set(s):
        return len(set(s)) == len(s)

    # Best early-exit form: build a `seen` set incrementally and bail the
    # instant a repeat shows up. Best case O(1) (first two chars match);
    # worst case O(n) for an all-unique string.
    # Time: O(n) worst / O(1) best   Space: O(k)
    def all_unique_seen(s):
        seen = set()
        for ch in s:
            if ch in seen:        # O(1) average membership test
                return False      # short-circuit: duplicate found, stop early
            seen.add(ch)
        return True

    # Bitmask form: for a FIXED alphabet (here lowercase a-z) we can track
    # "have I seen this char?" in the bits of a single integer instead of a
    # set -- true O(1) extra space (one int), no hashing overhead.
    #
    # How it works:
    #   bit = ord(ch) - ord('a')   maps 'a'->0, 'b'->1, ... 'z'->25
    #   1 << bit                   a mask with only that char's bit set
    #   mask & (1 << bit)          nonzero -> that bit already on -> duplicate
    #   mask |= (1 << bit)         turn the bit on to record we've seen it
    # Also short-circuits on the first repeat, like the seen-set version.
    # Time: O(n) worst / O(1) best   Space: O(1)  (single integer)
    # CAVEAT: only valid for the assumed alphabet; other chars give wrong
    # bit positions. Assert or fall back to a set for arbitrary Unicode.
    def all_unique_bitmask(s):
        mask = 0
        for ch in s:
            bit = ord(ch) - ord('a')
            if mask & (1 << bit):     # bit already set -> seen before
                return False
            mask |= (1 << bit)        # record this char
        return True

    # Find first non-repeating character.
    # Two passes: (1) Counter tallies all frequencies, (2) re-walk s IN ORDER
    # and return the first char whose total count is 1. Iterating `s` (not the
    # Counter) is what preserves original order. Returns None if none exist.
    # Time: O(n)   Space: O(k)
    def first_unique(s):
        freq = Counter(s)
        for char in s:
            if freq[char] == 1:
                return char
        return None

    print(allUnique('hello'))
    print(all_unique('hello'))
    print(all_unique_set('hello'))      # False
    print(all_unique_seen('hello'))     # False (bails at 2nd 'l')
    print(all_unique_seen('abc'))       # True
    print(all_unique_bitmask('hello'))  # False
    print(all_unique_bitmask('abc'))    # True
    print(first_unique('leetcode'))     # 'l'

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Appendix — Bitwise operators primer (`<<`, `|`, `&`, `|=`)

    An integer is secretly a row of on/off switches (bits). Each bit is a
    power of 2, read right-to-left:

    ```
    decimal 13 = binary 1101 = 8 + 4 + 0 + 1
                        ↑↑↑↑
                        8 4 2 1
    ```

    **`<<` left shift** — slide bits left, filling zeros on the right.
    `1 << n` builds a number with exactly ONE bit on, at position n
    (this is how you make a single-bit "mask"):

    ```
    1 << 0 = 0001 = 1
    1 << 1 = 0010 = 2
    1 << 2 = 0100 = 4
    1 << 3 = 1000 = 8
    ```

    **`|` OR** — result bit is 1 if EITHER input bit is 1. Used to turn a
    bit ON without disturbing the others:

    ```
      0101 (5)
    | 0011 (3)
      ----
      0111 (7)
    ```

    **`&` AND** — result bit is 1 only if BOTH are 1. Used to TEST a bit:
    `mask & (1 << n)` is nonzero only if bit n is already set.

    **`|=` compound assign** — `mask |= x` is just `mask = mask | x`, exactly
    like `+=`. It records "seen this" by OR-ing the new bit into `mask`.

    ### The "integer as a set" toolkit
    | Operation | Bit trick | Meaning |
    |---|---|---|
    | Add element n | `mask \|= (1 << n)` | turn bit n on |
    | Test element n | `mask & (1 << n)` | is bit n on? |
    | Remove element n | `mask &= ~(1 << n)` | turn bit n off |

    Each op is a single O(1) CPU instruction. This idiom powers `bitmask DP`
    (e.g. traveling salesman), permission flags (`READ | WRITE`), and the
    `all_unique_bitmask` function above. Gotcha: `1 << -1` raises ValueError,
    and don't confuse bitwise `& |` with logical `and / or`.
    """)
    return


if __name__ == "__main__":
    app.run()
