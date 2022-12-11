

class Message:
    PAYLOAD_MAX_SIZE = 65535
    HEADER_SIZE = 2


    def __init__(self, payload, header=None):
        self.payload = bytearray(payload)
        if header != None:
            self.header = bytearray(header)
        else:
            self.header = bytearray()
            self.create_header()

    def __str__(self):
        return f"size: {Message.extract_payload_size(self.header)} bytes; payload: {self.payload.decode('utf-8')}"

    def to_bytes(self):
        return bytes(self.header) + bytes(self.payload)

    def create_header(self):
        self.append_payload_size()

    def append_payload_size(self):
        payload_size = len(self.payload)
        low_byte = self.get_byte_at_index(payload_size, 0)
        high_byte = self.get_byte_at_index(payload_size, 1)
        self.header.insert(0, low_byte)
        self.header.insert(0, high_byte)

    def get_byte_at_index(self, val, index):
        mask = 0xFF << (8 * index)
        return (val & mask) >> (8 * index)

    def extract_payload_size(header):
        return int.from_bytes(header[:2], byteorder='big')
