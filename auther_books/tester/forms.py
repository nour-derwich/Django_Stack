from django import forms
from .models import Book
from .models import Auther

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','imgae','number_page','type']
class AutherForm(forms.ModelForm):
    class Meta:
        model = Auther
        fields = ['name','notes','books']
