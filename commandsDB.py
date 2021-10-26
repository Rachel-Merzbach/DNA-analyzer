from DnaSequence import DnaSequence


class CommandsDB:
    __instance = None
    __dict_id_name = {}
    __dict_name_id = {}
    __dict_name_seq = {}
    id_of_seq = 1

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def get_name_by_id(self, id):
        return self.__dict_id_name.get(int(id))

    def get_seq_by_id(self, id):
        return self.get_seq_by_name(self.get_name_by_id(int(id)))

    def get_id_by_name(self, name):
        return self.__dict_name_id.get(name)

    def get_seq_by_name(self, name):
        return self.__dict_name_seq.get(name)

    def insert_seq(self, id, name, seq):
        if not self.get_seq_by_id(id) and not self.get_seq_by_name(name):
            self.__dict_id_name[int(id)] = name
            self.__dict_name_id[name] = id
            self.__dict_name_seq[name] = DnaSequence(seq)
            return True
        return False

    def change_seq(self, name, new_seq):
        self.__dict_name_seq[name] = DnaSequence(new_seq)

    def delete_seq_by_id_name(self, seq_id, seq_name):
        try:
            self.__dict_name_seq.pop(seq_name)
            self.__dict_name_id.pop(seq_name)
            self.__dict_id_name.pop(int(seq_id))
            return True
        except:
            return False

    def print_all_dicts(self):
        print(self.__dict_id_name)
        print(self.__dict_name_seq)
        print(self.__dict_name_id)
