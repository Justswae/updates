from django.shortcuts import render
from . models import Posts
# Create your views here.
def index_page(request):
    post_dets = Posts.objects.all()
    return render(request,'templates/index.html', context={'posts':post_dets})

def posts_page(request,pk):
    post_det = Posts.objects.get(id=pk)
    return render(request,'templates/post_dets.html',context={'posts':post_det})