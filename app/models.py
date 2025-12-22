class Genre:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"{self.id}: {self.name}"


class Movie:
    def __init__(self, id, title, year, genre_id):
        self.id = id
        self.title = title
        self.year = year
        self.genre_id = genre_id
    
    def __str__(self):
        return f"{self.id}: {self.title} ({self.year}) - Genre {self.genre_id}"