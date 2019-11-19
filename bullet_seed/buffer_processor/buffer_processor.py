from .abstract_buffer import AbstractBuffer


class BufferProcessor(object):
    def __init__(self, buffer_class: AbstractBuffer):
        self._buffer = buffer_class()

    def __enter__(self):
        # do nothing
        return

    def __exit__(self):
        self.flush()

    def _reset_buffer(self):
        self._buffer.reset()

    def _has_reached_flush_threshold(self):
        return self._buffer.get_length() >= self._buffer.get_capacity()

    def _insert(self, record):
        self._buffer.insert(record)
        if self._has_reached_flush_threshold():
            self.flush()

    def flush(self):
        self._buffer.flush()

    def insert(self, record):
        self._insert(record)

    def batch_insert(self, records: list):
        if not records:
            print("EmptyInputRecordList")
            return
        for record in records:
            self._insert(record)
