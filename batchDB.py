class BatchDB:
    __instance = None
    __dict_batch = {}
    id_of_seq = 1

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def insert_batch(self, batch_name, batch_commands):
        self.__dict_batch[batch_name] = batch_commands
        print(self.__dict_batch)

    def get_batch_commands(self, batch_name):
        if self.__dict_batch.get(batch_name):
            return self.__dict_batch[batch_name]
        return []

    def get_batch_names(self):
        return list(self.__dict_batch.keys())

    def get_batch_show(self, batch_name):
        show_commands = []
        batch_commands = self.get_batch_commands(batch_name)
        if not batch_commands:
            return False
        for command in batch_commands:
            show_commands.append(command.command_description)
        return show_commands

