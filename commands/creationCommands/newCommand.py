from DnaSequence import DnaSequence
from commands.command import Command
from commandsDB import CommandsDB


class New(Command):
    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.seq_args = seq_vars
        self.seq = seq_vars[0]
        self.seq_name = ""

    def process(self):
        return True

    def execute(self):
        if len(self.seq_args) > 1 and '@' in self.seq_args[1][0]:
            self.seq_name = self.seq_args[1][1:]
        else:
            self.seq_name = f"seq{CommandsDB.id_of_seq}"
        cd = CommandsDB()
        if not DnaSequence.is_valid_dna(self.seq):
            return "this sequence cannot be DNA sequence"
        if cd.insert_seq(cd.id_of_seq, self.seq_name, self.seq):
            res = f"[{CommandsDB.id_of_seq}] {self.seq_name}: {self.seq}"
            CommandsDB.id_of_seq += 1
            return res
        return "sequence name already exist"
