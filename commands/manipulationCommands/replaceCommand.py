from DnaSequence import DnaSequence
from commands.command import Command
from commandsDB import CommandsDB
from commands.commandsParser import parsing_seq_id_name


class Replace(Command):
    num_of_replaces = 1

    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.args = seq_vars[1:]
        self.seq_id = seq_vars[0]
        self.seq_name = seq_vars[0]
        self.seq = DnaSequence("")

    def process(self):
        self.seq_id, self.seq_name, self.seq = parsing_seq_id_name(self.seq_id)
        if len(self.args) < 2 or len(self.args) % 2 == 1 or not self.seq_id:
            print(self.seq_id, len(self.args))
            return False
        return True

    def execute(self):
        with_colons = self.args[-2] == ":" and self.args[-1][0] == "@"
        len_new_seq = len(self.args) - 1 if not with_colons else len(self.args) - 3
        for i in range(len_new_seq):
            self.seq[int(self.args[i])] = self.args[i + 1]
        new_name = self.args[-1][1:] if self.args[-1][1] != "@" else self.seq_name
        if not DnaSequence.is_valid_dna(self.seq):
            return "this sequence cannot be DNA sequence"
        while not self.cd.insert_seq(self.cd.id_of_seq, new_name, self.seq):
            Replace.num_of_replaces += 1
            new_name = f"{new_name}_{self.num_of_replaces}"
        print("sequence name already exist")
