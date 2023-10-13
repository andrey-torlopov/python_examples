def is_set_bit(number: int, index: int) -> bool:
    return (number & (1 << index)) != 0


def set_bit(number: int, index: int) -> int:
    return number | (1 << index)


def inverse_bit(number: int, index: int) -> int:
    return number ^ (1 << index)


def reset_bit(number: int, index: int) -> int:
    return number & ~(1 << index)


def get_row(bit: int) -> int:
    return bit >> 4


def get_col(bit: int) -> int:
    return bit % 16

# После переработки для работы с вектором битов


def is_set_bit(bit_vector: list[int], index: int) -> bool:
    index_row = get_row(index)
    index_col = get_col(index)
    return (bit_vector[index_row] & (1 << index_col)) != 0


def set_bit(bit_vector: list[int], index: int) -> None:
    index_row = get_row(index)
    index_col = get_col(index)
    bit_vector[index_row] |= 1 << index_col


def inverse_bit(bit_vector: list[int], index: int) -> None:
    index_row = get_row(index)
    index_col = get_col(index)
    bit_vector[index_row] ^= 1 << index_col


def reset_bit(bit_vector: list[int], index: int) -> None:
    index_row = get_row(index)
    index_col = get_col(index)
    bit_vector[index_row] &= ~(1 << index_col)


# ary = [0, 1, 2, 3, 4, 4, 5, 6, 6, 1, 2]
# readed: list[int] = [i for i in range(250)]

# for i in range(len(ary)):
#     if is_set_bit(readed, ary[i] - 1):
#         print(ary[i])
#     else:
#         set_bit(readed, ary[i] - 1)


# a = 0b10000
# b = 0b00001

# a = a ^ 0b00011
# print(bin(a))
