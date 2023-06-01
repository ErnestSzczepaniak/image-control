from dataclasses import dataclass
from integral import Integral
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

@dataclass
class Protected(Integral):
    def encrypt(self, algorithm: str, key: str, iv: str):
        if algorithm == 'aes-128-ebc':
            cipher = AES.new(key=key.encode(), mode=AES.MODE_ECB)
            self.data = bytearray(pad(self.data, AES.block_size))
            self.data = bytearray(cipher.encrypt(self.data))

    def decrypt(self, algorithm: str, key: str, iv: str):
        if algorithm == 'aes-128-ebc':
            cipher = AES.new(key=key.encode(), mode=AES.MODE_ECB)
            self.data = bytearray(cipher.decrypt(self.data))
            self.data = bytearray(unpad(self.data, AES.block_size))