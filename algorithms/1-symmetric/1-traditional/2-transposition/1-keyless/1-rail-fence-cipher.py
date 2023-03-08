import math


class RailFenceCipher:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for i in range(0, self.key):
            for j in range(i, len(txt), self.key):
                cipher += txt[j]

        return cipher

    def decrypt(self, cipher: str) -> str:
        txt = ''

        rows = math.ceil(len(cipher) / self.key)
        for i in range(0, rows):
            for j in range(i, len(cipher), rows):
                txt += cipher[j]

        return txt


if __name__ == '__main__':
    algo = RailFenceCipher(key=3)
    print(algo.decrypt(algo.encrypt(txt='plaintext')))
