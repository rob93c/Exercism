def fence_pattern(rails: int, message_size: int) -> str:
    r = 2 * (rails - 1)
    return sorted(
        ((z % r) if (z % r) < rails else r - (z % r), z)
        for z in range(message_size))


def encode(plaintext: str, rails: int) -> str:
    return ''.join(plaintext[i]
                   for _, i in fence_pattern(rails, len(plaintext)))


def decode(ciphertext: str, rails: int) -> str:
    xx = zip(fence_pattern(rails, len(ciphertext)), ciphertext)
    return ''.join(ch
                   for _, ch in sorted(xx, key=lambda i: i[0][1]))
