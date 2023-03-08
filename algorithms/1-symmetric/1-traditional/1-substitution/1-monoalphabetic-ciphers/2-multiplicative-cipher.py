class MultiplicativeCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for ch in txt.lower():
            p = ord(ch) - ord('a')
            c = (p * self.key) % 26
            cipher += chr(c + ord('a'))

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        for ch in cipher.upper():
            c = ord(ch) - ord('A')
            p = (c * self.__inverse(self.key)) % 26
            txt += chr(p + ord('A'))

        return txt.lower()

    @staticmethod
    def __inverse(key: int):
        for i in range(26):
            if (key * i) % 26 == 1:
                return i
        raise Exception(f'key {key} is not valid.')


if __name__ == '__main__':
    algo = MultiplicativeCipher(key=23)
    print(algo.decrypt(algo.encrypt(txt='plaintext')))
