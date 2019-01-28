from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm

# Create your views here.
def index(request):
    context = {}
    posts = Post.objects.all().order_by('-date_created')
    context['posts'] = posts
    return render(request, 'index.html', context)

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = PostModelForm()
            return render(request, 'create.html', context)
    else:
        context['form'] = PostModelForm()
        return render(request, 'create.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('post:detail', post_id=post_id )
        else:
            context['form'] = PostModelForm(instance=post)
            return render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
        return render(request, 'update.html', context)

def addcomment(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post:detail', post_id=post_id)
        else:
            context['form'] = CommentModelForm()
            return render(request, 'addcomment.html', context)
    else:
        context['form'] = CommentModelForm()
        return render(request, 'addcomment.html', context)
