def single_number(nums: list[int]) -> int:
    bit_expr = 0

    for n in nums:
        bit_expr ^= n # The first occurence, flips to 1 for the corresponding num, and flips to 0 for the second occurence.

    return bit_expr