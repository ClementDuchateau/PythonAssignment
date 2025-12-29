import pandas as pd

def export_movies_to_csv(movies,genre_map, filename="movies.csv"):
    data = []
    for movie in movies:
        data.append({
        "ID": movie.id,
        "Title": movie.title,
        "Year": movie.year;
        "Genre": genre_map.get(movie.genre_id, "Unknown")
        })
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def export_movies_to_excel(movies, filename="movies.xlsx"):
    
    data = []
    for movie in movies:
        data.append({
        "ID": movie.id,
        "Title": movie.title,
        "Year": movie.year;
        "Genre": genre_map.get(movie.genre_id, "Unknown")
        })
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)