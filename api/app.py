
from flask import Flask, escape, request, jsonify
from entity.movies import Movies, Movie

movie_list = Movies()
app = Flask(__name__)

@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(name=movie_data['name'], rating=movie_data['rating'])

    movie_list.add_movie(new_movie)

    return 'Done', 201

@app.route('/movies')
def movies():
    movies = []

    for movie in movie_list.get_movies_list():
        movies.append({'name' : movie.name, 'rating' : movie.rating})

    return jsonify({'movies' : movies})