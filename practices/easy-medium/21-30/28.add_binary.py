
def add_binary(a: str, b: str) -> str:
    if len(b) > len(a):
        a, b = b, a

    output = []
    carry = 0
    for i in range(1, len(a) + 1):
        digit_a = int(a[-i])
        digit_b = int(b[-i]) if i <= len(b) else 0

        total = digit_a + digit_b + carry
        output.append(str(total % 2))
        carry = total // 2

    if carry:
        output.append(str(carry))

    return "".join(output[::-1])