import random
import string


class MappingCipher:
    def __init__(self, mapping: dict):
        self.mapping = mapping
        self.inverted_mapping = self.__invert_mapping(mapping)

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for ch in txt.lower():
            cipher += self.mapping[ch]

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        for ch in cipher.upper():
            txt += self.inverted_mapping[ch]

        return txt.lower()

    @staticmethod
    def generate_mapping() -> dict:
        lowers = list(string.ascii_lowercase)
        uppers = list(string.ascii_uppercase)

        random.shuffle(lowers)
        random.shuffle(uppers)

        return dict(zip(lowers, uppers))

    @staticmethod
    def __invert_mapping(mapping: dict) -> dict:
        return {v.upper(): k.lower() for k, v in mapping.items()}


if __name__ == '__main__':
    algo = MappingCipher(mapping=MappingCipher.generate_mapping())

    print(algo.decrypt(algo.encrypt(txt='plaintext')))
