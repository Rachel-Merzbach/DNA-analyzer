from commands.command import Command
from commandsDB import CommandsDB


class Dup(Command):
    num_of_duplicates = 1

    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.seq_args = seq_vars
        self.seq_id = [0][1:]
        self.seq_name = [0][1:]
        self.new_name = ""

    def process(self):
        if len(self.seq_args) > 1:
            self.new_name = self.seq_args[1]
            return True
        if self.seq_args[0][0] == "#":
            self.seq_id = self.seq_args
            self.seq_name = ""
            return True
        if self.seq_args[0][0] == "@":
            self.seq_name = self.seq_args[0][1:]
            self.seq_id = ""
            return True
        return False

    def execute(self):
        if self.seq_name:
            self.seq_id = self.cd.get_id_by_name(self.seq_name)
        else:
            self.seq_name = self.cd.get_name_by_id(self.seq_id)
        if not self.seq_name and not self.seq_id:
            return "name or id not exist"
        self.new_name = f"{self.seq_name}_{self.num_of_duplicates}"
        new_seq = f"{self.cd.get_seq_by_name(self.seq_name)}{self.cd.get_seq_by_name(self.seq_name)}"
        while not self.cd.insert_seq(self.cd.id_of_seq, self.new_name, new_seq):
            Dup.num_of_duplicates += 1
            self.new_name = f"{self.seq_name}_{self.num_of_duplicates}"
        print(f"[{self.cd.id_of_seq}] {self.new_name}: {new_seq}")
        CommandsDict.id_of_seq += 1
        return True
