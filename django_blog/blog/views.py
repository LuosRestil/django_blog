from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Hil Phartman',
        'title': 'Wiggle Worm',
        'content': 'Spoke too soon, wiggle worm.',
        'date_posted': 'August 29, 2018'
    }
]

# Create your views here.
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)