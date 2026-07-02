from django.shortcuts import render

# Create your views here.
movies_database = [
    {"id": 0, "title": "Interstellar", "year": 2014, "rating": 8.7},
]

def all_movies(req):
    return render(req, 'moviesIndex.html', {
        'movies': movies_database
    })

def movie_id(req, id):
    if 0 <= id < len(movies_database):
        movie = movies_database[id]
    else:
        movie = None

    return render(req, 'movie.html', {
        'movie': movie
    })