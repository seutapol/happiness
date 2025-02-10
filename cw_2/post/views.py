from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm


def get_posts(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False)


def get_post_by_id(request, post_id):
    post = Post.objects.filter(id=post_id).values().first()
    return JsonResponse(post, safe=False) if post else JsonResponse({'error': 'Post not found'}, status=404)

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')  
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/posts/')  


