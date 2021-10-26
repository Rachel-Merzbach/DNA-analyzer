from batchDB import BatchDB


class Run:
    def __init__(self, batch_name):
        self.db = BatchDB()
        self.batch_name = batch_name[0]

    def process(self):
        return True

    def execute(self):
        batch_commands = self.db.get_batch_commands(self.batch_name)
        res = batch_commands[0].execute()
        for i in range(len(batch_commands) -1):
            res += f"\n{batch_commands[i+1].execute()}"
        return res
