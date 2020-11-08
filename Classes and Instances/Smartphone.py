class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []  # 1. First wat for solving
        self.is_on = False
        self.used_memory = 0  # 2. Second way for solving or 1.

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if (self.used_memory + app_memory) > self.memory:
            return f"Not enough memory to install {app}"
        self.apps.append(app)
        self.used_memory += app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory - self.used_memory}"
