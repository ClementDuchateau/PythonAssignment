import sqlite3
import configparser
import os
from app.models import Movie, Genre
def get_connection():
    config = configparser.ConfigParser()
    config.read("settings.ini")

    db_path = config["database"]["path"]
    return sqlite3.connect(db_path)
def initialize_database():

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
    
    cursor.execute("SELECT COUNT(*) FROM genres")
    count = cursor.fetchone()[]
    
    if count == 0:
        default_genres = [
        ("Action",),
        ("Comedy",),
        ("Drama",),
        ("Sci-Fi",),
        ("Horror",)
        
        ]
        cursor.executemany(
        "INSERT INTO genres (name) VALUES (?)", default_genres
        )

    conn.commit()
    conn.close()


def movie_exists(title, year):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    "SELECT 1 FROM movies WHERE title = ? AND year = ?", (title, year)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
    
def genre_exists(name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    "SELECT 1 FROM genres WHERE name = ?", (name,)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
    
def add_movie(title, year, genre_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    """
    INSERT INTO movies (title, year, genre_id)
    VALUES (?, ?, ?)
    """, (title, year, genre_id)
    )
    conn.commit()
    conn.close()

def add_genre(name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    """
    INSERT INTO genres (name)
    VALUES (?)
    """, (name,)
    )
    conn.commit()
    conn.close()
    
def update_movie(movie_id, title, year, genre_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    """
        UPDATE movies
        SET title = ?, year = ?, genre_id = ?
        WHERE id = ?
    """,
    (title, year, genre_id, movie_id)
    )
    conn.commit()
    conn.close()


def get_all_movies():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT id, title, year, genre_id
        FROM movies
        ORDER BY title
        """
    )
    rows = cursor.fetchall()
    conn.close()
    movies = []
    for row in rows:
        movie = Movie(id=row[0],
            title=row[1],
            year=row[2],
            genre_id=row[3]
        )
        movies.append(movie)
    return movies

def get_all_genres():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT id, name 
        FROM genres
        ORDER BY id
        """
    )
    rows = cursor.fetchall()
    conn.close()
    genres = []
    for row in rows:
        
        genres.append(Genre(id=row[0], name=row[1]))
    return genres