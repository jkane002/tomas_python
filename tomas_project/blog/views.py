from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [{'author': 'Tomas',
 'title': 'Blog post 1',
 'content': 'First post',
 'date_posted': 'September 13, 2020'},
 {'author': 'Tomas',
  'title': 'Blog post 2',
  'content': 'First post',
  'date_posted': 'September 13, 2020'}]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html' , {'title': 'about'})
