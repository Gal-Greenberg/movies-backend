
class Movies:
    def __init__(self):
        self.movies_list = []

    def add_movie(self, movie):
        self.movies_list.append(movie)

    def get_movies_list(self):
        return self.movies_list

class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating