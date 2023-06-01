from generic import Generic
import crcmod
from Crypto.Hash import SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2b, BLAKE2s, MD5, SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE128, SHAKE256, HMAC

class Integral(Generic):
    def crc(self, polynominal: int, initial_value: int, reverse: bool):
        generator = crcmod.Crc(poly=polynominal, initCrc=initial_value, rev=reverse)
        generator.update(self.data)
        return generator.hexdigest().lower()
    
    def hash(self, algorithm: str, length: int) -> str:
        if algorithm == 'sha-1': return SHA1.new(self.data).hexdigest().lower()
        elif algorithm == 'sha-224': return SHA224.new(self.data).hexdigest().lower()
        elif algorithm == 'sha-256': return SHA256.new(self.data).hexdigest().lower()
        elif algorithm == 'sha-384': return SHA384.new(self.data).hexdigest().lower()
        elif algorithm == 'sha-512': return SHA512.new(self.data).hexdigest().lower()
        elif algorithm == 'blake-2b': return BLAKE2b.new(self.data).hexdigest().lower()
        elif algorithm == 'blake-2s': return BLAKE2s.new(self.data).hexdigest().lower()
        elif algorithm == 'md-5': return MD5.new(self.data).hexdigest().lower()
        elif algorithm == 'sha3-224': return SHA3_224.new(self.data).hexdigest().lower()
        elif algorithm == 'sha3-256': return SHA3_256.new(self.data).hexdigest().lower()
        elif algorithm == 'sha3-384': return SHA3_384.new(self.data).hexdigest().lower()
        elif algorithm == 'sha3-512': return SHA3_512.new(self.data).hexdigest().lower()
        elif algorithm == 'shake-128': return SHAKE128.new(self.data).read(length).hex().lower()
        elif algorithm == 'shake-256': return SHAKE256.new(self.data).read(length).hex().lower()
        return ''

    def signature(self, algorithm: str, key: str):
        if algorithm == 'hmac-sha-256': return HMAC.new(key.encode(), self.data, digestmod=SHA256).hexdigest().lower()
        return ''