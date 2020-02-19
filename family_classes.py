

class Kid:
    def __init__(self, name=None, age=-1):
        self.name = name
        self.age = age


class Family:
    def __init__(self, parents=[]):
        self.parents = parents
        self.kids = []

    def __str__(self):
        return_str = "Family:\n"
        return_str += "  Parents:\n"
        for parent in self.parents:
            return_str += "    "+parent+"\n"
        return_str += "  Kids:\n"
        for kid in self.kids:
            return_str += "    " + kid.name + ", " + str(kid.age) + "\n"
        return return_str

    def add_kid(self, kid=None):
        self.kids.append(kid)


