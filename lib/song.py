from config import CONN, CURSOR
import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

#to "map" our class to a database table, create a table with the same name as our class and give that table column names that match the instance attributes of the class.
class Song:
    
    def __init__ (self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

