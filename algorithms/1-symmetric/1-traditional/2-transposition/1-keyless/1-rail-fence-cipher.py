def encrypt(txt: str) -> str:
    cipher = ''

    for i in range(0, len(txt), 2):
        cipher += txt[i]

    for i in range(1, len(txt), 2):
        cipher += txt[i]

    return cipher


def decrypt(cipher: str) -> str:
    txt = ''

    mid = (len(cipher) + 1) // 2

    for i in range(mid):
        txt += cipher[i]

        j = i + mid

        if j < len(cipher):
            txt += cipher[j]

    return txt


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext')))
