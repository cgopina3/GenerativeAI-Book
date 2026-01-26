# 8-bit Floating-Point Toy System
# Format: 1 sign bit, 3 exponent bits, 4 mantissa bits

import math

BIAS = 3  # Exponent bias for 3-bit exponent

def encode_float8(value):
    if value == 0:
        return 0

    sign = 0 if value >= 0 else 1
    value = abs(value)

    exponent = int(math.floor(math.log2(value)))
    mantissa = value / (2 ** exponent) - 1

    exponent_bits = exponent + BIAS
    mantissa_bits = int(mantissa * (2 ** 4))

    float8 = (sign << 7) | (exponent_bits << 4) | mantissa_bits
    return float8


def decode_float8(byte):
    sign = (byte >> 7) & 1
    exponent_bits = (byte >> 4) & 0b111
    mantissa_bits = byte & 0b1111

    exponent = exponent_bits - BIAS
    mantissa = 1 + mantissa_bits / (2 ** 4)

    value = mantissa * (2 ** exponent)
    return -value if sign else value


if __name__ == "__main__":
    value = 0.15625
    encoded = encode_float8(value)
    decoded = decode_float8(encoded)

    print(f"Original value : {value}")
    print(f"Encoded (8-bit): {bin(encoded)}")
    print(f"Decoded value  : {decoded}")
