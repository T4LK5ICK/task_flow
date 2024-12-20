import sqlite3


def create_table_if_not_exists():
    """Ensure the tasks table exists in the database."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pending'
    )
    ''')
    conn.commit()
    conn.close()


create_table_if_not_exists()

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

def create_task(title: str, description: str):
    """Create a new task in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
                   (title, description, 'Pending'))
    conn.commit()
    conn.close()

def get_tasks():
    """Retrieve all tasks from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id: int, status: str):
    """Update a task's status."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id: int):
    """Delete a task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
