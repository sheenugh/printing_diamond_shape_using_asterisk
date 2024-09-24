# ========== PSEUDO CODE ==========
# || ACTUAL CODE ||
# - Def function print_diamond
def print_diamond(n):
    if n % 2 == 0:
        return "Please return an odd integer."

    # - Loop syntax
    for i in range(1, n+1):
        if i <= n // 2 +1:
            print(" " * (n //2-i+1) + "*" * (2 * i -1))
        else:
            print(" " * (i - n // 2 - 1) + "*" * (2 * (n - i + 1) - 1))

print_diamond(5)
