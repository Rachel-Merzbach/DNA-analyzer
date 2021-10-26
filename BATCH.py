from batchDB import BatchDB
from commandsFacotry import CommandsFactory


class BATCH():
    def __init__(self):
        self.batchDB = BatchDB()
        self.saved_commands = []
        self.cm = CommandsFactory()

    def execute(self, batch_name):
        while True:
            command = input("> batch >>> ")
            if not command:
                continue
            command_parsed = command.split()
            if command_parsed[0] == "end":
                if self.saved_commands:
                    self.batchDB.insert_batch(batch_name, self.saved_commands)
                return
            processed_command = self.cm.create_command(command, command_parsed[0], command_parsed[1:])
            if processed_command and processed_command.process():
                self.saved_commands = self.saved_commands + [processed_command]
