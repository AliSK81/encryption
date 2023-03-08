class AdditiveCipher:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, txt: str) -> str:
        cipher = ''

        for ch in txt.lower():
            p = ord(ch) - ord('a')
            c = (p + self.key) % 26
            cipher += chr(c + ord('a'))

        return cipher.upper()

    def decrypt(self, cipher: str) -> str:
        txt = ''

        for ch in cipher.upper():
            c = ord(ch) - ord('A')
            p = (c - self.key) % 26
            txt += chr(p + ord('A'))

        return txt.lower()


if __name__ == '__main__':
    algo = AdditiveCipher(key=1)
    print(algo.decrypt(algo.encrypt(txt='plaintext')))
