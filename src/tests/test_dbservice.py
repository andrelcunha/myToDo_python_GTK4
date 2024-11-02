import unittest
from app.dbservice.dbservice import DbService
from app.model.task.task import Task

class TestDbService(unittest.TestCase):
    def setUp(self):
        # Initialize DbService with an in-memory database
        self.db_service = DbService(db_file=":memory:")

    def test_create_task(self):
        task = self.db_service.create_task("Test Task")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

    def test_get_tasks(self):
        self.db_service.create_task("Task 1")
        self.db_service.create_task("Task 2")
        tasks = self.db_service.get_tasks()
        self.assertEqual(len(tasks), 2)

    def test_update_task(self):
        task = self.db_service.create_task("Initial Task")
        updated_task = self.db_service.update_task(task.id, "Updated Task", True)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertTrue(updated_task.completed)

    def test_delete_task(self):
        task = self.db_service.create_task("Task to delete")
        self.db_service.delete_task(task.id)
        self.assertIsNone(self.db_service.get_task(task.id))

    def tearDown(self):
        self.db_service._DbService__conn.close()

if __name__ == "__main__":
    unittest.main()
