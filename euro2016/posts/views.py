from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.

# List all the posts
def list_post(request):
    context = {
        'posts_list': Post.objects.all(),
    }
    return render(request, 'posts/list_post.html', context)

def detail_post(request, id = None):
    instance = get_object_or_404(Post, id = id)
    context = {
        'post': instance,
    }
    return render(request, 'posts/detail_post.html', context)

def create_post(request):
    f = PostForm()
    if request.method == "POST":
        f = PostForm(request.POST)
        if f.is_valid():
            instance = f.save(commit = False)
            instance.save()
            messages.success(request, "Succesfully created post")
            return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": f,
        "title": "Create post",
    }
    return render(request, 'posts/create_post.html', context)

def update_post(request, id = None):
        instance = get_object_or_404(Post, id = id)
        f = PostForm(request.POST or None, instance = instance)
        if f.is_valid():
            instance = f.save(commit = False)
            instance.save()
            messages.success(request, "Succesfully updated post", extra_tags="some-class")
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "form": f,
            "title": "Edit post",
            "instance": instance,
        }
        return render(request, 'posts/edit_post.html', context)

def delete_post(request, id = None):
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    messages.success(request, "Succesfully deleted post")
    return redirect('posts:list_post')
