from commands.command import Command
from commandsDB import CommandsDB
import re
from commands.commandsParser import parsing_seq_id_name


class Slice(Command):
    slice_index = 1

    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.seq_vars = seq_vars
        self.seq = ""
        self.seq_id = self.seq_vars[0][1:]
        self.seq_name = self.seq_vars[0][1:]
        self.new_seq_name = self.seq_vars[0][1:]

    def process(self):
        if len(self.seq_vars) < 3 or len(self.seq_vars) == 4:
            return False

    def execute(self):
        self.seq_id, self.seq_name, self.seq = parsing_seq_id_name(self.seq_vars[0])
        if self.seq_id and '0' <= self.seq_vars[1] <= '9' and '0' <= self.seq_vars[2] <= '9':
            from_idx = int(self.seq_vars[1])
            to_idx = int(self.seq_vars[2])
            if not from_idx < to_idx < len(self.seq):
                return "indexes don't match the sequence"
            new_seq = self.seq[from_idx:to_idx]
            if len(self.seq_vars) > 4:
                using_seq_name = re.search('@@+$', self.seq_vars[4])
                create_new_name = re.search('@+[A-Za-z0-9_-]', self.seq_vars[4])
                if not self.seq_vars[3] == ":" or (not using_seq_name and not create_new_name):
                    return "missing colons or vars"
                if using_seq_name:
                    self.new_seq_name = f"{self.seq_name}_s{self.slice_index}"
                    self.slice_index += 1
                elif create_new_name:
                    self.new_seq_name = self.seq_vars[4][1:]
                status = self.cd.insert_seq(CommandsDB.id_of_seq, self.new_seq_name, new_seq)
                if status:
                    self.cd.id_of_seq += 1
                    return f"[{CommandsDB.id_of_seq -1}] {self.new_seq_name}: {new_seq}"
            else:
                self.cd.change_seq(self.seq_name, new_seq)
                return f"[{self.seq_id}] {self.seq_name}: {new_seq}"



