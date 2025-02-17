from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def home(request):
    return redirect('/threads/')

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/threads/')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect(f'/threads/{thread_id}/')
    else:
        form = PostForm()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    thread.delete()
    return redirect('/threads/')

def edit_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect(f'/threads/{thread_id}/')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/edit_thread.html', {'form': form, 'thread': thread})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    thread_id = post.thread.id
    post.delete()
    return redirect(f'/threads/{thread_id}/')

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    thread_id = post.thread.id
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/threads/{thread_id}/')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form, 'post': post})