import re

from commandsDB import CommandsDB


def parsing_seq_id_name(identity):
    is_name = re.search('@+[a-zA-Z0-9_-]', identity)
    is_id = re.search('#+[0-9]', identity)
    if is_id:
        return identity[1:], CommandsDB().get_name_by_id(identity[1:]), CommandsDB().get_seq_by_id(identity[1:])
    elif is_name:
        return CommandsDB().get_id_by_name(identity[1:]), identity[1:], CommandsDB().get_seq_by_name(identity[1:])
    return None, None, None

