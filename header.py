from dataclasses import dataclass
from protected import Protected
from datetime import datetime
from typing import Tuple

FIELDS = {
    'header_magic':         16,
    'header_protection':    16,
    'header_crc':           16,
    'header_hash':          128,

    'firmware_id':          64,
    'firmware_author':      32,
    'firmware_file':        32,
    'firmware_version':     32,
    'firmware_stability':   32,
    'firmware_date':        32,
    'firmware_time':        32,
    'firmware_vendor':      32,
    'firmware_product':     32,
    'firmware_model':       32,
    'firmware_chip':        32,
    'firmware_mode':        32,

    'firmware_size':        16,
    'firmware_protection':  16,
    'firmware_crc':         16,
    'firmware_hash':        128,
    'firmware_signature':   128,
    'firmware_random':      128
}

@dataclass
class Header(Protected):

    header_magic: str

    header_protection: str
    header_crc: str
    header_hash: str

    firmware_id: str
    firmware_author: str
    firmware_file: str
    firmware_version: str
    firmware_stability: str
    firmware_date: str
    firmware_time: str
    firmware_vendor: str
    firmware_product: str
    firmware_model: str
    firmware_chip: str
    firmware_mode: str

    firmware_size: int
    firmware_protection: str
    firmware_crc: str
    firmware_hash: str
    firmware_signature: str
    firmware_random: str

    def __init__(self, data: bytearray = bytearray(1024)):
        self.data = data
        if sum(FIELDS.values()) != len(self.data):
            raise ValueError('Invalid header size')

    def __setattr__(self, name: str, value) -> None:
        
        if name == 'data':
            self.__dict__[name] = value
            return

        value = str(value)

        position, size = self.field_description(name)

        self.data[position:position + size] = value.ljust(size, '\0').encode('utf-8')

    def __getattr__(self, name: str):
        
        if name == 'data':
            return self.__dict__[name]

        position, size = self.field_description(name)

        cast = self.__dataclass_fields__[name].type

        return cast(self.data[position:position + size].decode('utf-8').strip('\0'))
    
    def field_description(self, name: str) -> Tuple[int, int]:
        position = 0
        size = 0
        for key, value in FIELDS.items():
            if key == name:
                size = value
                break
            position += value
        return position, size