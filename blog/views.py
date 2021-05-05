from django.shortcuts import render
from .models import Post


# Create your views here.
def blog_list(request):

    post = Post.objects.all()
    context = {
        'post': post
    }

    return render(request, 'blueberry/index.html', context)