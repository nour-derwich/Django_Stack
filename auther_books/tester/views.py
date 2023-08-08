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
            description = form.cleaned_data['description']
            imgae = form.cleaned_data['imgae']
            number_page = form.cleaned_data['number_page']
            type = form.cleaned_data['type']
            type = form.cleaned_data['type']
            Book.objects.create(title=title,description=description,imgae=imgae,number_page=number_page,type=type)
            return redirect('list_books')  # Redirect to the view displaying all books
    else:
        form = BookForm()

    return render(request, 'allBooks.html', {'form': form})
def show_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = AutherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            notes = form.cleaned_data['notes']
            
            Auther.objects.create(name=name,notes=notes)
            return redirect('list_authers')  # Redirect to the view displaying all books
    else:
        form = AutherForm()
   
 

    return render(request, 'show_book.html', {'book': book ,'form': form})


def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'book':book ,'form': form})

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

def update_auther(request, author_id):
    author = get_object_or_404(Auther, pk=author_id)
    
    if request.method == 'POST':
        form = AutherForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('list_authers')
    else:
        form = AutherForm(instance=author)

    return render(request, 'updat_author.html', {'form': form})

def delete_author(request, author_id):
    author = get_object_or_404(Auther, pk=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('list_authers')

    return render(request, 'delete_author.html', {'author': author})