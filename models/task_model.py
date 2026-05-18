import sqlite3
from pathlib import Path

class TaskModel:
    def __init__(self, db_name="pomodoro.db"):
        self.db_name = "models" / Path(db_name)
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                duration INTEGER NOT NULL
            )
            """
            cursor.execute(query)
            conn.commit()
        
        conn.close()

    def add_task(self, name : str, date : str, duration : int) -> int:
        """Add a new task and return its id"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = """
                INSERT INTO tasks (
                    name, 
                    date, 
                    duration
                )
                VALUES (?, ?, ?)
                """
                cursor.execute(query, (name, date, duration))  
                conn.commit()
        
            inserted_id = cursor.lastrowid
            conn.close()
            return inserted_id
        except Exception as e:
            print(e)
            return -1
        
    def get_all_tasks(self) -> list:
        """Return all tasks in the database"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = """
                SELECT * from tasks
                """
                cursor.execute(query)
                task_list = cursor.fetchall()

            cursor.close()
            return task_list
        except Exception as e:
            print(e)
            return []

    def delete_task(self, task_id : int) -> bool:
        """Delete a certain task according to its ID"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = """
                DELETE from tasks 
                WHERE tasks.id = (?)
                """
                cursor.execute(query, (task_id,))
                conn.commit()

            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

if __name__ == "__main__":
    db = TaskModel()
    
   