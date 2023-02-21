import math


def encrypt(txt: str, key: int) -> str:
    cipher = ''

    for i in range(0, key):
        for j in range(i, len(txt), key):
            cipher += txt[j]

    return cipher


def decrypt(cipher: str, key: int) -> str:
    txt = ''

    rows = math.ceil(len(cipher) / key)
    for i in range(0, rows):
        for j in range(i, len(cipher), rows):
            txt += cipher[j]

    return txt


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext', key=3), key=3))
