from commands.analysisCommands import findCommand, findallCommand
from commands.creationCommands import loadCommand, dupCommand, newCommand
from commands.manipulationCommands import sliceCommand, replaceCommand
from commands.managementCommands import delCommand, saveCommand
from commands.batchCommands import batchshowCommand, batchlistCommand, runCommand


class CommandsFactory:
    current_seq_id = 1

    def __init__(self):
        self.creation_commands = {
            "new": newCommand.New,
            "load": loadCommand.Load,
            "dup": dupCommand.Dup
        }
        self.manipulation_commands = {
            "slice": sliceCommand.Slice,
            "replace": replaceCommand.Replace
        }
        self.management_commands = {
            "save": saveCommand.Save,
            "del": delCommand.Del
        }
        self.analysisCommands = {
            "find": findCommand.Find,
            "findall": findallCommand.FindAll
        }
        self.batch = {
            "run": runCommand.Run,
            "batchlist": batchlistCommand.Batchlist,
            "batchshow": batchshowCommand.Batchshow,

        }

    def create_command(self, command, command_type, command_vars):
        if command_type in self.creation_commands:
            command = (self.creation_commands[command_type])(command, command_vars)
        elif command_type in self.manipulation_commands:
            command = (self.manipulation_commands[command_type])(command, command_vars)
        elif command_type in self.management_commands:
            command = (self.management_commands[command_type])(command, command_vars)
        elif command_type in self.analysisCommands:
            command = (self.analysisCommands[command_type])(command, command_vars)
        elif command_type in self.batch:
            command = (self.batch[command_type])(command_vars)
        else:
            print(f"command <{command_type}> is not exist")
            return False
        return command
