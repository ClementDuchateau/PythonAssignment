import pandas as pd

def export_movies_to_csv(movies, filename="movies.csv"):
    df = pd.DataFrame([m.__dict__ for m in movies])
    df.to_csv(filename, index=False)

def export_movies_to_excel(movies, filename="movies.xlsx"):
    df = pd.DataFrame([m.__dict__ for m in movies])
    df.to_excel(filename, index=False)