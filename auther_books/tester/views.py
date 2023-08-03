from django.shortcuts import render , redirect ,get_object_or_404

# from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from .forms import AutherForm
from .models import Auther

# Create your views here.
def get_books(request):
    context = {"books": Book.objects.all()}	
    return render(request,'allBooks.html',context)

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            
            Book.objects.create(title=title)
            return redirect('list_books')  # Redirect to the view displaying all books
    else:
        form = BookForm()

    return render(request, 'allBooks.html', {'form': form})
def show_book(request, id):
    book = get_object_or_404(Book, pk=id)
    authors = book.authors.all()
 

    return render(request, 'show_book.html', {'book': book , 'authors': authors})


def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form})

def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')

    return render(request, 'delete_book.html', {'book': book})







##############auther
def get_auther(request):
    context = {"authers": Auther.objects.all()}	
    return render(request,'allAuther.html',context)

def create(request):
    if request.method == 'POST':
        form = AutherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            
            Auther.objects.create(name=name)
            return redirect('list_authers')  # Redirect to the view displaying all books
    else:
        form = AutherForm()

    return render(request, 'allAuther.html', {'form': form})
def show_auther(request, id):
    author = get_object_or_404(Auther, pk=id)
    
 

    return render(request, 'show_auther.html', {'author': author})