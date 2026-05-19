import sqlite3
from pathlib import Path

from core.subject import Subject

class TaskModel(Subject):
    def __init__(self, db_name="pomodoro.db"):
        super().__init__()
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
            self.notify()
            return inserted_id
        except Exception as e:
            print(e)
            return -1
        
    def get_all_tasks(self) -> list[dict]:
        """Return all tasks in the database"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                query = """
                SELECT * from tasks
                """
                cursor.execute(query)
                task_list = [dict(row) for row in cursor.fetchall()]

            cursor.close()
            return task_list
        except Exception as e:
            print(e)
            return []
        
    def get_tasks(self, month: int = None, day_str: str = None, weekday: int = None) -> list[dict]:
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = "SELECT * FROM tasks"
                conditions = []
                params = []
                
                if month is not None:
                    conditions.append("strftime('%m', date) = ?")
                    params.append(f"{month:02d}")
                    
                if day_str is not None:
                    conditions.append("date = ?")
                    params.append(day_str)
                             
                if weekday is not None:
                    conditions.append("strftime('%W', date) = strftime('%W', 'now')")
                    conditions.append("strftime('%Y', date) = strftime('%Y', 'now')")
                    conditions.append("cast(strftime('%w', date) as integer) = ?")
                    params.append(weekday)
                    
                if conditions:
                    query += " WHERE " + " AND ".join(conditions)
                    
                cursor.execute(query, tuple(params))
                return [dict(row) for row in cursor.fetchall()]

        except Exception as e:
            print(f"Erreur SQL lors de la récupération dynamique : {e}")
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
            self.notify()
            return True
        except Exception as e:
            print(e)
            return False

if __name__ == "__main__":
    db = TaskModel()
    print(db.get_all_tasks())
    
   