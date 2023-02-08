from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'AppPeliculas/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'AppPeliculas/movie_detail.html', {'movie': movie})

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'AppPeliculas/actor_list.html', {'actors': actors})

def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'AppPeliculas/actor_detail.html', {'actor': actor})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'AppPeliculas/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'AppPeliculas/review_detail.html', {'review': review})

def add_movies(request):
    if request.method == "POST":
        miFormulario = MovieForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Movie(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppPeliculas/movie_list.html")
    else:
        miFormulario = MovieForm()
    return render(request, "AppPeliculas/movie_forms.html", {"miFormulario": miFormulario})


def search(request):
    return render(request,"AppPeliculas/search.html")

def search_res(request):
    peliculaBusqueda = request.get["Pelicula"]
    resultadoPelicula = Movie.objects.filter(name__icontains=peliculaBusqueda)

    return render(request,"AppPeliculas/res.html", {"info1":peliculaBusqueda,"info2":resultadoPelicula})