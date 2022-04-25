from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def add_Post(request):
    submitted= False
    if request.method=='POST':
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted=True
     
    return render(request, 'add_post.html',{'form' : form, 'submitted' : submitted})


def index(request):
    posts=Post.objects.all()
    form = PostForm
    return render(request, 'index.html',{'posts':posts,"form":form})


def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request, 'post.html',{'posts':posts})
