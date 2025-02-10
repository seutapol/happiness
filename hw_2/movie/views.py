from django.http import JsonResponse
from .models import Movie

def get_movies(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def get_movie_by_id(request, movie_id):
    movie = Movie.objects.filter(id=movie_id).values().first()
    return JsonResponse(movie, safe=False) if movie else JsonResponse({'error': 'Movie not found'}, status=404)

# Create your views here.
