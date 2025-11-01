import sqlite3

class Database:
    def __init__(self, dbname:str = "default.db") -> None:
        self.dbname = dbname

    def init_table(self) -> None:
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            value DOUBLE NOT NULL)''')
        conn.commit()
        conn.close()

    def __enter__(self):
        self.init_table()
        self.conn = sqlite3.connect(self.dbname)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def get_expenses(self) -> list:
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    def insert_expense(self, expense: dict) -> None:
        self.cursor.execute("INSERT INTO expenses (category, description, value) VALUES (?, ?, ?)",
                            (expense['category'], expense['description'], expense['value']))
    def remove_expense(self,expense_id: str) -> None:
        self.cursor.execute(f"DELETE FROM expenses WHERE id = {expense_id}")