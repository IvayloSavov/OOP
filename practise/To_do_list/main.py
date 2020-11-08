tasks = ["baba", "dqdo", "tateddd", "mamaddd", "bateddd"]
print(tasks)
completed = [tasks.pop(i) for i, e in enumerate(reversed(tasks)) if len(e) == 4]
print(tasks)
