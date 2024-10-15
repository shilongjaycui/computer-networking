"""Computations related to computer networking."""

from helper_functions import convert_byte_from_decimal_to_binary


if __name__ == "__main__":
    decimal_byte: int = 192
    print(f"Byte (decimal): {decimal_byte}")
    binary_byte: str = convert_byte_from_decimal_to_binary(decimal_byte=decimal_byte)
    print(f"Byte (binary): {binary_byte}")
