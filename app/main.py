from app.database import (add_movie, initialize_database, update_movie, get_all_movies, movie_exists, genre_exists, add_genre, get_all_genres)
from app.reports import export_movies_to_csv, export_movies_to_excel



def add_movie_cli():
    title = input("Movie title: ")
    year = int(input("Release year: "))
    genre_id = int(input("Genre ID: "))
    
    if movie_exists(title, year):
        print("This movie already exists in the database")
        return
    add_movie(title, year, genre_id)
    print("Movie added succesfully")

def add_genre_cli():
    genre = input("Genre name: ")
    
    if genre_exists(name):
        print("This genre already exists in the database")
        return
    add_genre(name)
    print("Genre added succesfully")

def edit_movie_cli():
    movie_id = input("Movie ID to edit: ")
    title = input("New title: ")
    year = input("New year: ")
    genre_id = input("New genre ID: ")
    
    update_movie(int(movie_id), title, int(year), int(genre_id))
    print("Movie updated succesfully")

def list_movies_cli():
    movies = get_all_movies()
    genres = get_all_genres()
    
    genre_map = {g.id: g.name for g in genres}

    if not movies:
        print("No movies found.\n")
        return

    for movie in movies:
        genre_name = genre_map(movie.genre_id, "Unknown")
        print(f"{movie.id}: {movie.title} ({movie.year}) [{genre_name}]")
    print()

def list_genres_cli():
    genres = get_all_genres()

    if not genres:
        print("No genres found.\n")
        return

    for genre in genres:
        print(genre)
    print()
    
def export_report_cli():
    movies = get_all_movies()
    genres = get_all_genres()
    genre_map = {g.id: g.name for g in genres}

    if not movies:
        print("No movies to export.\n")
        return

    print("1. Export to CSV")
    print("2. Export to Excel")

    choice = input("Choose format: ")

    if choice == "1":
        export_movies_to_csv(movies)
        print("Exported movies to movies.csv\n")
    elif choice == "2":
        export_movies_to_excel(movies)
        print("Exported movies to movies.xlsx\n")
    else:
        print("Invalid choice.\n")
        return

    
def main():
    initialize_database()
    
    while True:
        print("1. Add movie")
        print("2. List movies")
        print("3. Edit movie")
        print("4. Export report")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_movie_cli()
        elif choice == "2":
            list_movies_cli()
        elif choice == "3":
            edit_movie_cli()
        elif choice == "4":
            export_report_cli()
        elif choice == "5":
            break
        else:
            print("Not a valid answer try again")
            continue

if __name__ == "__main__":
    main()
