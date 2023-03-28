# This program will recommend the next movie a user should watch, using NLP to deduct
# which film is most like the one given based on their descriptions.


# Import modules
import spacy

# Load spaCy module
nlp = spacy.load('en_core_web_md')



# ==================================== CLASS: Movie ===================================
# This class represents a movie object.

class Movie:

    # Set constructor
    def __init__(self, movie_name, description):

        self.movie_name = movie_name
        self.description = description
        self.nlp_desc = nlp(description)

# =====================================================================================


# ================================= FUNCTION: watch_next ==============================
# This function which movie the user should watch next, based on a given list of
# movies and their descriptions, and the description of the movie they have just watched

def watch_next(movies_list, just_watched):
    
    # Initialise empty counter variables
    current_movie_rec = Movie("Placeholder", "Placeholder")
    current_highest_similarity = 0


    # Iterate over movies in list
    for movie in movies_list:

        # Compare movie description to the just watched film
        next_similarity = just_watched.nlp_desc.similarity(movie.nlp_desc)

        # DEBUGGING: Uncomment the following line to see the similarity scores for each movie
        # print(f"{movie.movie_name}: {next_similarity}")

        # If new similarity is higher than previous highest, update the counters
        if next_similarity > current_highest_similarity:
            current_highest_similarity = next_similarity
            current_movie_rec = movie

    
    # Return highest scoring movie
    return current_movie_rec

# =====================================================================================



# ==================================== MAIN PROGRAM ===================================

# Initialise empty list of movies
movies = []


# Initialise movie object for given movie (the one the user has just watched)
last_movie = Movie("Planet Hulk", "Will he save their world or destory it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttleand launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Read in text file
with open("movies.txt", "r+") as file:

    # For line read in as string
    for line in file:

        full_string = line

        # Split string using colon into name and description
        split_string = full_string.split(" :")

        # Build movie object and append to movies list
        movies.append(Movie(split_string[0], split_string[1]))


# Run function to determine which movie to watch next
next_movie = watch_next(movies, last_movie)

# Print advice to user
print()
print(f"We're so glad you enjoyed {last_movie.movie_name}! We think you'll love {next_movie.movie_name} next.")
print()