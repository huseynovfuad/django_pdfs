from django.shortcuts import render
from .models import Books
# Create your views here.



def books_list(request):
    context = {}
    books = Books.objects.order_by('-created_at')
    context['books'] = books
    return render(request, 'index.html', context)