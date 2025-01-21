def print_pattern():
    n = 8
    s = "EMMANUALIKKU"

    for i in range(n):
        q = " " * (n - i - 1)
        c = "".join(s[:i + 1])
        print(f"{q}{c}")

print_pattern()
