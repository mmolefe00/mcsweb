from django.shortcuts import render
from home.models import Post, Comment 

# Create your views here.

# === Home / Index Page ===
def index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts":posts,
        "nbar": "home"
    }
    return render(request, 'index.html',context)

# === About Page ===
def about(request):
    context = {
        'nbar': 'about'
    }
    return render(request, 'about.html', context)


# === Philosophy Page ===
def philosophy(request):
    context = {
        'nbar': 'philosophy'
    }
    return render(request, 'philosophy.html', context)

# === Services Page ===
def services(request):
    context = {
        'nbar': 'services'
    }
    return render(request, 'services.html', context)

# === Contact Page ===
def contact(request):
    context = {
        'nbar': 'contact'
    }
    return render(request, 'contact.html', context)


# === Blog Pages ====

# -- Blog Index View
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request, 'blog/index.html', context)
    # displays a list of all posts, as well as navbar reference

# -- Blog Category View --

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


# -- Blog Detail View --

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments":comments
    }
    return render(request, "blog/detail.html", context)