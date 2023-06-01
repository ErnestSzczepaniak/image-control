from dataclasses import dataclass

@dataclass
class Generic:
    data: bytearray

    def size(self) -> int:
        return len(self.data)