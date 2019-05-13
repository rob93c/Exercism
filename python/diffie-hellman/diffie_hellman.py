import secrets


def private_key(p: int) -> int:
    return secrets.choice(range(2, p))


def public_key(p: int, g: int, private: int) -> int:
    return pow(g, private, p)


def secret(p: int, public: int, private: int) -> int:
    return pow(public, private, p)
