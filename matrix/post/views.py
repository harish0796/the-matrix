from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required(login_url='/users/login')
def view_posts(request):
    return HttpResponse("View posts", request.user)

@login_required(login_url='/users/login')
def create_posts(request):
    if request.method == 'POST':
        postname = request.POST['post_name']
        postbody = request.POST['post_body']
        post = Post.objects.create(postname=postname, postbody=postbody, owner= request.user)
        post.save()
        print(post)
    return render(request,"create_posts.html")