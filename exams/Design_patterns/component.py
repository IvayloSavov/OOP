class Component:
    root = Folder("C:/")

    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = self.get_path()

    @staticmethod
    def get_path(path):
        names = path.split("/")[1:]
        node = Component.root
        for name in names:
            node = node.children[name]
        return node