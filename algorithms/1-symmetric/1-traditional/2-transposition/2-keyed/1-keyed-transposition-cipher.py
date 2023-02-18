import math
import random


def encrypt(txt: str, mapping: dict) -> str:
    cipher = ''

    group_size = math.ceil(len(txt) / len(mapping))

    for i in range(group_size):
        for j in range(len(mapping)):
            k = i * len(mapping) + mapping[j]

            if k >= len(txt):
                continue

            cipher += txt[k]

    return cipher.upper()


def decrypt(cipher: str, mapping: dict) -> str:
    txt = ''

    group_size = math.ceil(len(cipher) / len(mapping))

    for i in range(group_size):
        for j in range(len(mapping)):
            k = i * len(mapping) + mapping[j]

            if k >= len(cipher):
                continue

            txt += cipher[k]

    return txt.lower()


def generate_mapping(size: int) -> dict:
    keys = [i for i in range(size)]
    values = [i for i in range(size)]

    random.shuffle(keys)
    random.shuffle(values)

    return dict(zip(keys, values))


def invert_mapping(mapping: dict) -> dict:
    return {v: k for k, v in mapping.items()}


if __name__ == '__main__':
    mapping = generate_mapping(size=2)

    print(decrypt(encrypt(txt='plaintext', mapping=mapping), mapping=invert_mapping(mapping)))
