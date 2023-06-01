from protected import Protected

class Firmware(Protected):
    def __init__(self, data: bytearray = bytearray()):
        self.data = data

    def pad_to(self, size: int):
        self.data += bytearray(size - len(self.data))

    def append(self, data: bytearray):
        self.data += data

    def preppend(self, data: bytearray):
        self.data = data + self.data