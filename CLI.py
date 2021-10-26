
class CLI(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not CLI.__instance:
            CLI.__instance = object.__new__(cls)
        return CLI.__instance

    def exe(self):
        pass
