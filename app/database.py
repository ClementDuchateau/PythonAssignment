def initialize_database():
    import sqlite3
    import os
    import configparser

    config = configparser.ConfigParser()
    config.read("settings.ini")

    db_path = config["database"]["path"]

    folder = os.path.dirname(db_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS genres( id INTEGER PRIMARY KEY, name TEXT NOT NULL)
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS movies( id INTEGER PRIMARY KEY, title TEXT, year INTEGER, genre_id INTEGER, FOREIGN KEY(genre_id) REFERENCES genres(id))
    """)

    conn.commit()
    conn.close()