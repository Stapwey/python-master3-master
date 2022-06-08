def main(digit):
    A = digit & 0b11111111
    digit = digit >> 8
    B = digit & 0b111111111111
    digit = digit >> 12
    C = digit & 0b11111111111
    digit = digit >> 11
    D = digit & 0b1
    d = (((B << 20) |
          (D << 19) | (A << 11) | (C << 0)))
    return d

def main1(digit):
    A = digit & 0b1111111111
    digit = digit >> 10
    B = digit & 0b11
    digit = digit >> 2
    C = digit & 0b111111111111
    digit = digit >> 12
    D = digit & 0b1
    digit = digit >> 1
    E = digit & 0b1111111
    d = (((C << 20) |
          (E << 13) | (A << 3) | (D << 2) | (B << 0)))
    return d


print(main1(0x90685795))
print(main(0x5c143e31))