"""Helper functions for computer networking."""
from typing import List
from dataclasses import dataclass, field

@dataclass
class IPv4AddressDecimal:
    octet1: int = field(default=0)
    octet2: int = field(default=0)
    octet3: int = field(default=0)
    octet4: int = field(default=0)

    def __post_init__(self):
        # Validate each octet to ensure it's between 0 and 255
        for octet in (self.octet1, self.octet2, self.octet3, self.octet4):
            if not (0 <= octet <= 255):
                raise ValueError(f"Octet {octet} is not valid. Must be between 0 and 255.")

    def __str__(self):
        return f"{self.octet1}.{self.octet2}.{self.octet3}.{self.octet4}"


@dataclass
class IPv4AddressBinary:
    octet1: str = field(default="00000000")
    octet2: str = field(default="00000000")
    octet3: str = field(default="00000000")
    octet4: str = field(default="00000000")

    def __post_init__(self):
        # Validate each octet to ensure it's between 0 and 255
        for octet in (self.octet1, self.octet2, self.octet3, self.octet4):
            if len(octet) != 8:
                raise ValueError(f"Octet {octet} is not valid. It must consist of 8 bits.")
            for value in octet:
                if value not in ["0", "1"]:
                    raise ValueError(f"Octet {octet} is not valid. Each bit must be either 0 or 1.")

    def __str__(self):
        return f"{self.octet1}.{self.octet2}.{self.octet3}.{self.octet4}"


def convert_byte_from_decimal_to_binary(decimal_byte: int) -> str:
    """Convert an IP address byte from decimal integer to binary string."""
    binary_byte: List = ["0"] * 8
    for i in range(8):
        superscript: int = 7 - i
        value: int = 2 ** superscript
        if value > decimal_byte:
            continue
        else:
            binary_byte[i] = "1"
            decimal_byte -= value

    return "".join(binary_byte)
