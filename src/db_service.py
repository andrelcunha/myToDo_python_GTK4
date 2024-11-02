import sqlite3
import sqlite3

from task import Task


class DbService:
    def __init__(self):
        self.__conn = sqlite3.connect("tasks.db")
        self.__cursor = self.__conn.cursor()
        self.__create_table_if_not_exists()



    def get_tasks(self):
        self.__cursor.execute("SELECT * FROM tasks")
        tasks_rows = self.__cursor.fetchall()
        tasks = self.__map_rows_to_tasks(tasks_rows)
        return tasks
        self.__cursor.execute("SELECT * FROM tasks")
        tasks_rows = self.__cursor.fetchall()
        tasks = self.__map_rows_to_tasks(tasks_rows)
        return tasks
        

    def create_task(self, title):
        task = Task(title)
        self.__cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", (task.title, task.completed))
        self.__conn.commit()
        # inserted_task = self.__map_row_to_task(self.__get_last_task())
        last_row = self.__cursor.lastrowid
        task.id = last_row
        task = Task(title)
        self.__cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", (task.title, task.completed))
        self.__conn.commit()
        # inserted_task = self.__map_row_to_task(self.__get_last_task())
        last_row = self.__cursor.lastrowid
        task.id = last_row
        return task

    def update_task(self, task_id, title, is_completed):
    def update_task(self, task_id, title, is_completed):
        task = self.get_task(task_id)
        if task is None:
            return
        task.completed = is_completed == True
        task.title = title
        
        self.__cursor.execute("UPDATE tasks SET title = ?, completed = ? WHERE id = ?", (task.title, task.completed, task.id))
        self.__conn.commit()
        task.completed = is_completed == True
        task.title = title
        
        self.__cursor.execute("UPDATE tasks SET title = ?, completed = ? WHERE id = ?", (task.title, task.completed, task.id))
        self.__conn.commit()

        return task

    def delete_task(self, task_id):
        self.__cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.__cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return

    def get_task(self, id):
        self.__cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = self.__cursor.fetchone()
        if row is None:
            return None
        return self.__map_row_to_task(row)

    
    def __create_table_if_not_exists(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        self.__conn.commit()

    def __map_row_to_task(self, row):
        return Task(id=row[0], title=row[1], completed=(row[2] == 1))
    
    def __map_rows_to_tasks(self, rows):
        return [self.__map_row_to_task(row) for row in rows]
    
    def __get_last_task(self):
        self.__cursor.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT 1")
        row = self.__cursor.fetchone()
        return self.__map_row_to_task(row)
        self.__cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = self.__cursor.fetchone()
        if row is None:
            return None
        return self.__map_row_to_task(row)

    
    def __create_table_if_not_exists(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        self.__conn.commit()

    def __map_row_to_task(self, row):
        return Task(id=row[0], title=row[1], completed=(row[2] == 1))
    
    def __map_rows_to_tasks(self, rows):
        return [self.__map_row_to_task(row) for row in rows]
    
    def __get_last_task(self):
        self.__cursor.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT 1")
        row = self.__cursor.fetchone()
        return self.__map_row_to_task(row)