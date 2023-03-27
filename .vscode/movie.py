from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


db.create_all()

movies = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Godfather: Part II',
    'The Dark Knight',
    '12 Angry Men',
    'Schindler\'s List',
    'The Lord of the Rings: The Return of the King',
    'Pulp Fiction',
    'The Good, the Bad and the Ugly',
    'Fight Club',
    # Add more movies here
]

for movie in movies:
    db.session.add(Movie(title=movie))

db.session.commit()


def search_movies(search_term):
    movies = Movie.query.filter(Movie.title.like(f'%{search_term}%')).all()
    return [movie.title for movie in movies]


@app.route('/movies')
def movie_autofill():
    search_term = request.args.get('search_term', '')
    matches = search_movies(search_term)
    return jsonify(matches)

