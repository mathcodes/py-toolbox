from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/movies')
def movie_autofill(matches=None):
    search_term = request.args.get('search_term', '')
    # Query the database for movies that match the search term
    # and return them as a JSON response
    return jsonify(matches)
