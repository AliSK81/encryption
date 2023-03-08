import math
import random


class KeyedTranspositionCipher:
    def __init__(self, mapping: dict):
        self.mapping = mapping
        self.inverted_mapping = self.__invert_mapping(mapping)

    def encrypt(self, txt: str) -> str:
        cipher = ''

        group_size = math.ceil(len(txt) / len(self.mapping))

        for i in range(group_size):
            for j in range(len(self.mapping)):
                k = i * len(self.mapping) + self.mapping[j]

                if k >= len(txt):
                    continue

                cipher += txt[k].lower()

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        group_size = math.ceil(len(cipher) / len(self.inverted_mapping))

        for i in range(group_size):
            for j in range(len(self.inverted_mapping)):
                k = i * len(self.inverted_mapping) + self.inverted_mapping[j]

                if k >= len(cipher):
                    continue

                txt += cipher[k].upper()

        return txt.lower()

    @staticmethod
    def generate_mapping(size: int) -> dict:
        keys = [i for i in range(size)]
        values = [i for i in range(size)]

        random.shuffle(keys)
        random.shuffle(values)

        return dict(zip(keys, values))

    @staticmethod
    def __invert_mapping(mapping: dict) -> dict:
        return {v: k for k, v in mapping.items()}


if __name__ == '__main__':
    algo = KeyedTranspositionCipher(mapping=KeyedTranspositionCipher.generate_mapping(size=2))

    print(algo.decrypt(algo.encrypt(txt='plaintext')))
