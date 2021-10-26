from batchDB import BatchDB
import re


class Batchshow:
    def __init__(self, batch_name):
        self.db = BatchDB()
        self.batch_name = batch_name[0]

    def process(self):
        if re.search('@+[a-zA-Z0-9_-]', self.batch_name):
            self.batch_name = self.batch_name[1:]
            return True
        return False

    def execute(self):
        batch_show = self.db.get_batch_show(self.batch_name)
        if not batch_show:
            return f"batch {self.batch_name} doesn't exist"
        return batch_show

