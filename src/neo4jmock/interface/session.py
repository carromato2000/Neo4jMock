class Session:
    def close(self):
        self.closed = True

    def closed(self):
        return self.closed

    def run(self, query, parameters = None, **kwargs):
        raise NotImplementedError()

    def last_bookmarks(self):
        raise NotImplementedError()

    def begin_transaction(self, **kwargs):
        raise NotImplementedError()

    def execute_read(self, transaction_function, *args, **kwargs):
        raise NotImplementedError()

    def execute_write(self, transaction_function, *args, **kwargs):
        raise NotImplementedError()