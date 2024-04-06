from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About Page',
    }
    return render(request, template_name='blog/about.html', context=context)
