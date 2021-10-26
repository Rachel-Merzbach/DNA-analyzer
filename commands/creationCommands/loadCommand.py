from commands.command import Command
from commandsDB import CommandsDB
from DnaSequence import DnaSequence


class Load(Command):
    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.file_name = seq_vars[0]
        self.seq_name = ""
        self.seq_args = seq_vars

    def process(self):
        if len(self.seq_args) > 1 and '@' in self.seq_args[1][0]:
            self.seq_name = self.seq_args[1][1:]
        elif '.rawdna' in self.file_name:
            self.seq_name = f"{self.file_name[:self.file_name.index('.rawdna')]}"
        return True

    def execute(self):
        try:
            f = open(self.file_name)
            seq = f.readline()
            if not DnaSequence.is_valid_dna(seq):
                return "the sequence in file is not DNA sequence"
            if self.cd.insert_seq(self.cd.id_of_seq, self.seq_name, seq):
                view_seq = seq if len(seq) <= 40 else seq[:32] + "..." + seq[-3:-1] + seq[-1]
                CommandsDB.id_of_seq += 1
                return f"[{self.cd.id_of_seq}] {self.seq_name}: {view_seq}"
            return "sequence name already exist"
        except:
            return f"file '{self.file_name}' is not exist"
