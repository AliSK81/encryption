import math


def encrypt(txt: str, num_of_columns: int) -> str:
    cipher = ''

    for i in range(0, num_of_columns):
        for j in range(i, len(txt), num_of_columns):
            cipher += txt[j]

    return cipher


def decrypt(cipher: str, num_of_columns: int) -> str:
    txt = ''

    num_of_row = math.ceil(len(cipher) / num_of_columns)
    for i in range(0, num_of_row):
        for j in range(i, len(cipher), num_of_row):
            txt += cipher[j]

    return txt


if __name__ == '__main__':
    print(decrypt(encrypt(txt='plaintext', num_of_columns=3), num_of_columns=3))
