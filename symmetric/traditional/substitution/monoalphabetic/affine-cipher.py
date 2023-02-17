def encrypt(txt: str, k1: int, k2: int) -> str:
    cipher = ''

    for ch in txt.lower():
        p = ord(ch) - ord('a')
        c = (p * k1 + k2) % 26
        cipher += chr(c + ord('a'))

    return cipher.upper()


def decrypt(cipher: str, k1: int, k2: int) -> str:
    txt = ''

    for ch in cipher.upper():
        c = ord(ch) - ord('A')
        p = ((c - k2) * inverse(k1)) % 26
        txt += chr(p + ord('A'))

    return txt.lower()


def inverse(k: int):
    for i in range(26):
        if (k * i) % 26 == 1:
            return i
    raise Exception(f'key {k} is not valid.')


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext', k1=23, k2=1), k1=23, k2=1))
