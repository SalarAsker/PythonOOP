class TaskList:
    def __init__(self):
        self.tasks = []

    # Functio will add a task to the list.
    # Each task is of a tuple containing the priority of the task and its name. 
    def add_task(self, task_name: str, priority: int):
        self.tasks.append((priority, task_name))


    def get_next(self):
        # The list is stored first, so that when the list is sorted, 
        # the task with the highest priority is the last item on the list
        self.tasks.sort()

        # Get the highes priority tasks and remove it from the list
        tk = self.tasks.pop()
        return tk


    def return_task_list(self):
        self.tasks.sort()

        tk = ""
        for t in self.tasks:
            tk += f"Name: {t[1]}, Priority: {t[0]}\n"
        return tk

    def clear_all_tasks(self):
        self.tasks.clear()

tk = TaskList();
# Add some tasks
tk.add_task("Khana", 10)
tk.add_task("School", 40)
tk.add_task("Aata", 30)
tk.add_task("Pani", 20)

# Get the whole tasks list
print(tk.return_task_list())
# Get a highest priority tasks
print(tk.get_next())
# Clear all the tasks
print(tk.clear_all_tasks())

print(tk.return_task_list())

