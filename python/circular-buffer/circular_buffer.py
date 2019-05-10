class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buff = []

    def read(self):
        if len(self.buff) <= 0:
            raise BufferEmptyException("Error: the buffer is empty!")
        return self.buff.pop(0)

    def write(self, data: int):
        if len(self.buff) == self.capacity:
            raise BufferFullException("Error: the buffer is full!")
        self.buff.append(data)

    def overwrite(self, data: int):
        if len(self.buff) < self.capacity:
            self.write(data)
        else:
            self.buff.pop(0)
            self.buff.append(data)

    def clear(self):
        del self.buff[:]
