def encrypt(txt: str, k: int) -> str:
    cipher = ''

    for ch in txt.lower():
        p = ord(ch) - ord('a')
        c = (p + k) % 26
        cipher += chr(c + ord('a'))

    return cipher.upper()


def decrypt(cipher: str, k: int) -> str:
    txt = ''

    for ch in cipher.upper():
        c = ord(ch) - ord('A')
        p = (c - k) % 26
        txt += chr(p + ord('A'))

    return txt.lower()


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext', k=1), k=1))
