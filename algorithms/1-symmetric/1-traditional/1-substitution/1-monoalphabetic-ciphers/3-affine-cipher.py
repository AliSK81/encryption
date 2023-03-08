class AffineCipher:
    def __init__(self, key1: int, key2: int):
        self.key1 = key1
        self.key2 = key2

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for ch in txt.lower():
            p = ord(ch) - ord('a')
            c = (p * self.key1 + self.key2) % 26
            cipher += chr(c + ord('a'))

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        for ch in cipher.upper():
            c = ord(ch) - ord('A')
            p = ((c - self.key2) * self.__inverse(self.key1)) % 26
            txt += chr(p + ord('A'))

        return txt.lower()

    @staticmethod
    def __inverse(key: int):
        for i in range(26):
            if (key * i) % 26 == 1:
                return i
        raise Exception(f'key {key} is not valid.')


if __name__ == '__main__':
    algo = AffineCipher(key1=23, key2=1)
    print(algo.decrypt(algo.encrypt(txt='plaintext')))
