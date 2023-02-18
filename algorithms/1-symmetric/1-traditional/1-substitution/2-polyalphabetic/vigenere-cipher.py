def encrypt(txt: str, key: str) -> str:
    cipher = ''

    for i, ch in enumerate(txt.lower()):
        p = ord(ch) - ord('a')
        k = get_k(key, i)
        c = (p + k) % 26
        cipher += chr(c + ord('a'))

    return cipher.upper()


def decrypt(cipher: str, key: str) -> str:
    txt = ''

    for i, ch in enumerate(cipher.upper()):
        c = ord(ch) - ord('A')
        k = get_k(key, i)
        p = (c - k) % 26
        txt += chr(p + ord('A'))

    return txt.lower()


def get_k(key: str, idx: int):
    j = idx % len(key)
    return ord(key[j].upper()) - ord('A')


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext', key='SECRET'), key='SECRET'))
