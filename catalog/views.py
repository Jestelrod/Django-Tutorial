from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
        Función vista para la página inicio del sitio.
        """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_genres= Genre.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_books_eadlg= Book.objects.filter(title__exact="el arte de la guerra").count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
        
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
                  request,
                  'index.html',
                  context={'num_books':num_books,
                           "num_genres": num_genres, 
                           'num_instances':num_instances,
                           'num_instances_available':num_instances_available,
                           "num_books_eadlg": num_books_eadlg,
                           'num_authors':num_authors,
                           'num_visits':num_visits},
                  )
    
from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author
    