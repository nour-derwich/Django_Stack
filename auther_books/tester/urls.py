from django.urls import path 
from . import views
urlpatterns=[
   path('', views.get_books, name='list_books'),
   path('add/book/', views.create, name='create'),
   path('show/<int:id>/', views.show_book, name='show_book'),
   path('update/<int:book_id>/', views.update, name='update_book'),
   path('delet/<int:book_id>/', views.delete, name='delete_book'),
   path('author', views.get_auther, name='list_authers'),
   path('add/auther/', views.create, name='create_auther'),
   path('show/auther/<int:id>/', views.show_auther, name='show_auther'),
  

]
