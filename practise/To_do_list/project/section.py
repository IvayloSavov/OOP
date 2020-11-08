# from To_do_list.project.task import Task
# from typing import List


class Section:
    # name: str
    # tasks: List[Task]

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task_names = [t.name for t in self.tasks]
        if task_name not in task_names:
            return f"Could not find task with the name {task_name}"
        task = list(filter(lambda t: t.name == task_name, self.tasks))[0]
        if not task.completed:
            self.tasks[task_names.index(task_name)].completed = True
            return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = []
        for t in reversed(self.tasks):
            if t.completed:
                completed_tasks.append(t)
                self.tasks.remove(t)
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n" + "".join([f"{t.details()}\n" for t in self.tasks])
        return res


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
