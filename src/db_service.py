# import sqlite3

from task import Task


class DbService:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        if len(self.tasks) == 0 or self.tasks is None:
            return None
        # mocking database query
        
        return self.tasks
        

    def create_task(self, title):
        last_id = 0
        for task in self.tasks:
            if task.id > last_id:
                last_id = task.id
        id = last_id+1
        task = Task(title=title, id=id, completed=False)
        self.tasks.append(task)
        return task

    def update_task(self, task_id, title):
        task = self.get_task(task_id)
        if task is None:
            return
        task.completed = not task.completed
        
        # mocking database update
        for index, old_task in enumerate(self.tasks):
            if old_task.id == task.id:
                self.tasks[index] = task
                print(f"[Info] Task {task.id} - index {index} - operation: update")
                break

        return task

    def delete_task(self, task_id):
        index = self.__getindex(task_id)
        if index is None:
            print(f"[Err] Task {task_id} not found")
            return
        task = self.tasks.pod(index)
        print(f"[Info] Task {task.id} - index {index} - operation: update")
        return

    def get_task(self, id):
        for index, task in enumerate(self.tasks):
            if task.id == id:
                print(f"Task {task.id} - index {index}  operation: get")
                return task
        return None
    
    def __getindex(self, id):
        for index, task in enumerate(self.tasks):
            if task.id == id:
                return index
        return None
