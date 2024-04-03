from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Vika',
        'title': 'What if all your friends got married',
        'content': "I guess it's time to start a support group for 'Single Survivors Anonymous'!",
        'date_posted': 'April 3, 2024',
    },
    {
        'author': 'Rustam',
        'title': "Why should you think in several programming languages at the same time?",
        'content': "So you can argue with yourself in C++, Python, and Kotlin!",
        'date_posted': 'April 1, 2024',
    },
    {
        'author': 'Nikita',
        'title': "Why is it cool to be a devops?",
        'content': "Because they're the masters of making chaos look like controlled chaos!",
        'date_posted': 'April 2, 2024',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, template_name='blog/about.html', context=context)
