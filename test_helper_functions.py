from helper_functions import convert_byte_from_decimal_to_binary


class TestClass:
    def test_one(self):
        decimal_byte: int = 192
        assert convert_byte_from_decimal_to_binary(decimal_byte=decimal_byte) == "11000000"

    def test_two(self):
        decimal_byte: int = 168
        assert convert_byte_from_decimal_to_binary(decimal_byte=decimal_byte) == "10101000"

    def test_three(self):
        decimal_byte: int = 1
        assert convert_byte_from_decimal_to_binary(decimal_byte=decimal_byte) == "00000001"

    def test_four(self):
        decimal_byte: int = 0
        assert convert_byte_from_decimal_to_binary(decimal_byte=decimal_byte) == "00000000"
