from commands.command import Command
from commandsDB import CommandsDB
from commands.commandsParser import parsing_seq_id_name


class Del(Command):
    def __init__(self, command, seq_vars):
        super().__init__(command)
        self.cd = CommandsDB()
        self.seq_args = seq_vars
        self.seq_identity = seq_vars[0]

    def process(self):
        if len(self.seq_args) != 1:
            return False
        return True

    def execute(self):
        seq_id, seq_name, seq = parsing_seq_id_name(self.seq_identity)
        if not seq_id or not seq_name or not seq:
            return f"seq {self.seq_identity} not found"
        submit = input("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.\n> confirm >>> ")
        while submit not in ['Y', 'y', 'N', 'n']:
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
            submit = input("confirm >>> ")
        if submit in ['N', 'n']:
            return f"delete {seq_name} was canceled"
        if self.cd.delete_seq_by_id_name(seq_id, seq_name):
            return f"Deleted: [{seq_id}] {seq_name}: {seq}"
