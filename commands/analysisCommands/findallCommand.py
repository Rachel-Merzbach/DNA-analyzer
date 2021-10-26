import re

from commands.command import Command
from commandsDB import CommandsDB
from commands.commandsParser import parsing_seq_id_name


class FindAll(Command):
    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.seq_args = seq_vars


    def process(self):
        if len(self.seq_args) != 2:
            return False
        return True

    def execute(self):
        seq_id_1, seq_name_1, seq_to_find_in = parsing_seq_id_name(self.seq_args[0])
        seq_id_2, seq_name_2, seq_to_find = parsing_seq_id_name(self.seq_args[1])
        if not seq_to_find:
            seq_to_find = self.seq_args[1]
        res = ""
        for oc in [m.start() for m in re.finditer(seq_to_find, seq_to_find_in)]:
            res += f"{oc} "
        return res
