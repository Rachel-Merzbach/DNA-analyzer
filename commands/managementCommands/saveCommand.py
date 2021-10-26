from commands.command import Command
from commandsDB import CommandsDB
from commands.commandsParser import parsing_seq_id_name


class Save(Command):
    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.seq_args = seq_vars

    def process(self):
        if 0 < len(self.seq_args) < 2:
            return True
        return False

    def execute(self):
        seq_id, seq_name, seq = parsing_seq_id_name(self.seq_args[0])
        if not seq_id or not seq_name or not seq:
            return f"seq {self.seq_args[0]} not found"
        file_to_save = f"{seq_name}.rawdna" if len(self.seq_args) == 1 else self.seq_args[1]
        try:
            f = open(file_to_save, "w")
            f.write(f"{seq}\n")
            return f"Saved [{seq_id}] {seq_name}: {seq}"
        except:
            return "inserting seq wasn't succeed"