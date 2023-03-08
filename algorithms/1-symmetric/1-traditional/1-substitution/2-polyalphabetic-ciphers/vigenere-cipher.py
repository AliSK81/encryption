class VigenereCipher:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for i, ch in enumerate(txt.lower()):
            p = ord(ch) - ord('a')
            k = self.__get_k(self.key, i)
            c = (p + k) % 26
            cipher += chr(c + ord('a'))

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        for i, ch in enumerate(cipher.upper()):
            c = ord(ch) - ord('A')
            k = self.__get_k(self.key, i)
            p = (c - k) % 26
            txt += chr(p + ord('A'))

        return txt.lower()

    @staticmethod
    def __get_k(key: str, idx: int):
        j = idx % len(key)
        return ord(key[j].upper()) - ord('A')


if __name__ == '__main__':
    algo = VigenereCipher(key='SECRET')
    print(algo.decrypt(algo.encrypt(txt='plaintext')))
