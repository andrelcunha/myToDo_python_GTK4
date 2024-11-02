
class Task:
    def __init__(self, title:str, id=0,  completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"Task {self.id}: {self.title}, completed: {self.completed}"