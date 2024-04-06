from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

posts = [
    {
        'author': 'Nikita Tkachenko',
        'title': "Why are trains such great conversationalists?",
        'content': "Because they can't go in another direction of the conversation!",
        'date_posted': 'April 2, 2024',
    },
    {
        'author': 'Vika Pugach',
        'title': 'What if all your friends got married?',
        'content': "Time to change your group chat name to 'The Married and the Restless'!",
        'date_posted': 'April 3, 2024',
    },
    {
        'author': 'Rustam Radjabov',
        'title': "Why should you think in several programming languages at the same time?",
        'content': "So you can argue with yourself in C++, Python, and Kotlin!",
        'date_posted': 'April 1, 2024',
    },
]


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home Page',
    }
    return render(request, template_name='blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, template_name='blog/about.html', context=context)
