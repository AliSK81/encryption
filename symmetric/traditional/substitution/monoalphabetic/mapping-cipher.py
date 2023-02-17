import random
import string


def encrypt(txt: str, mapping: dict) -> str:
    cipher = ''

    for ch in txt.lower():
        cipher += mapping[ch]

    return cipher.upper()


def decrypt(cipher: str, mapping: dict) -> str:
    txt = ''

    for ch in cipher.upper():
        txt += mapping[ch]

    return txt.lower()


def generate_mapping() -> dict:
    lowers = list(string.ascii_lowercase)
    uppers = list(string.ascii_uppercase)

    random.shuffle(lowers)
    random.shuffle(uppers)

    return dict(zip(lowers, uppers))


def invert_mapping(mapping: dict) -> dict:
    return {v.upper(): k.lower() for k, v in mapping.items()}


if __name__ == '__main__':
    mapping = generate_mapping()

    print(decrypt(encrypt(txt='plaintext', mapping=mapping), mapping=invert_mapping(mapping)))
