from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.books_list, name='index'),
    # path('filter/', views.filter_books, name='filter'),
]