from config import CONN, CURSOR
import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

#to "map" our class to a database table, create a table with the same name as our class and give that table column names that match the instance attributes (name, album) of the class.
class Song:

    def __init__ (self, name, album):
        self.id = None #to let SQL assign unique id
        self.name = name
        self.album = album


#crafts a SQL statement to create a songs table and give that table column names that match the attributes of an individual instance of Song.
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
    
#INSERT INTO songs (name, album) VALUES ("Hello", "25"); 
#When save a record, we are repeating the same exact steps and using the same code. The only things that are different are the values that we are inserting into our songs table. Let's abstract this functionality into an instance method, save(),that saves a given instance of our Song class into the songs table of our database..
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

    # Commit the changes to the database
    # db_connection.commit()