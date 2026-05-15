value_table = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_integer(s: str) -> int:
    total = 0
    prev = 0

    for ch in reversed(s):
        value = value_table[ch]

        if value < prev:
            total -= value
        else:
            total += value

        prev = value

    return total