class Father:
    def __init__(self, name):
        self.father_name = name


class Mother:
    def __init__(self, name):
        self.mother_name = name


class Daughter(Father, Mother):
    def __init__(self, name_father, name_mother):
        Father.__init__(self, name_father)
        Mother.__init__(self, name_mother)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'


child = Daughter(name_father="Toni", name_mother="Mariq")
print(child.get_parent_info())

