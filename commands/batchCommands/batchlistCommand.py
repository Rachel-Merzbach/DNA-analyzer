from batchDB import BatchDB


class Batchlist:
    def __init__(self):
        self.db = BatchDB()

    def process(self):
        return True

    def execute(self):
        return self.db.get_batch_names()