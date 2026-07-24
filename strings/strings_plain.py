"""Plain-Python version of strings.py (marimo notebook)."""


# ============================================================
# Use join to concatenate strings.
# join() is much more efficient than repeated +=.
# ============================================================

def main():
    s = "Hello World"

    # Inefficient: creates many temporary strings
    result = ""
    for ch in s:
        result += ch + " "
    print(result)

    # Efficient: join builds once
    pieces = [ch for ch in s]
    result = " ".join(pieces)
    print(result)


if __name__ == "__main__":
    main()
