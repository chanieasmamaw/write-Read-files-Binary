# Define a list to hold movie data
movies = []

# Function to create (add) a movie
def create_movie(title, director, year, genre):
    movie = {
        "title": title,
        "director": director,
        "year": year,
        "genre": genre
    }
    movies.append(movie)
    print(f"Movie '{title}' added.")

# Function to read (display) all movies
def read_movies():
    if not movies:
        print("No movies found.")
    for movie in movies:
        print(f"Title: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")
        print(f"Genre: {movie['genre']}")
        print("-" * 20)

# Function to update a movie
def update_movie(old_title, new_title=None, new_director=None, new_year=None, new_genre=None):
    for movie in movies:
        if movie["title"] == old_title:
            if new_title:
                movie["title"] = new_title
            if new_director:
                movie["director"] = new_director
            if new_year:
                movie["year"] = new_year
            if new_genre:
                movie["genre"] = new_genre
            print(f"Movie '{old_title}' updated.")
            return
    print(f"Movie '{old_title}' not found.")

# Function to delete a movie
def delete_movie(title):
    global movies
    movies = [movie for movie in movies if movie["title"] != title]
    print(f"Movie '{title}' deleted.")

# Example usage:
create_movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
create_movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
create_movie("The Dark Knight", "Christopher Nolan", 2008, "Action")

print("\n--- All Movies ---")
read_movies()

update_movie("The Dark Knight", new_year=2012, new_genre="Action/Drama")

print("\n--- Updated Movies ---")
read_movies()

delete_movie("The Godfather")

print("\n--- Final List of Movies ---")
read_movies()
