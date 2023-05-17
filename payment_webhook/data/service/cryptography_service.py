import hashlib


class Cryptography:
    @classmethod
    def encrypt(cls, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()

    @classmethod
    def check_equals(cls, encrypted_text: str, text: str) -> str:
        return cls.encrypt(text) == encrypted_text
