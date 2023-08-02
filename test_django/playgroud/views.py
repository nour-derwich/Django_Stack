from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def say_hello(request):
    context = {
    	"all_the_movies": Movie.objects.all()
    }
    return render(request,'hello.html',context)
# def another_method(request, my_val):	# my_val would be a number from the URL
#     return render(request,'hello.html', my_val=my_val)                                # given the example above, my_val would be 23
    
# def yet_another(request, name):	        # name would be a string from the URL
#     return  render(request,'hello.html',name=name)                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color):
#      return render(request,'hello.html',id=id,color=color) 

