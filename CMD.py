from CLI import CLI
from BATCH import BATCH
from commandsFacotry import CommandsFactory


class CMD(CLI):

    def exe(self):
        cm = CommandsFactory()
        while True:
            command = input("> cmd >>> ")
            if not command:
                continue
            command_parsed = command.split()
            if command_parsed[0] == "batch" and len(command_parsed) >= 2:
                batch = BATCH()
                batch.execute(command_parsed[1])
                continue
            processed_command = cm.create_command(command, command_parsed[0], command_parsed[1:])
            if processed_command and processed_command.process():
                print(processed_command.execute())


if __name__ == '__main__':
    cmd = CMD()
    cmd.exe()
