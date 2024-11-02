

from db_service import DbService

flag_quit = False
db_service = DbService()
while not flag_quit:
    print("Select an option:")
    print("l - List tasks")
    print("a - Add task")
    print("u - Update task status - completed or incomplete")
    print("d - Delete task")
    print("q - Quit")
    choice = input("Enter your choice: ")


    match choice:
        case "l":
            tasks = db_service.get_tasks()
            if tasks is None:
                print("No tasks found.")
                continue
            for task in tasks:
                print(f"Task {task.id}: {task.title}, completed: {task.completed}") 
        
        case "a":
            title = input("Enter task title: ")
            db_service.create_task(title)
        
        case "u":
            task_id = int(input("Enter task ID: "))
            task_title = input("Enter task Title: ")
            value = input("Does the task is completed? ([Y]/n): ")
            is_completed = (value != "n")
        

            db_service.update_task(task_id, task_title, is_completed)
        
        case "d":
            task_id = int(input("Enter task ID: "))
            db_service.delete_task(task_id)
        
        case "q":
            flag_quit = True
        
        case _:
            print("Invalid choice. Please try again.")
