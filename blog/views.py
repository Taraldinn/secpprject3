from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Post, Category
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    latest_post = Post.objects.all()[:3]
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'latest_post': latest_post,
        'categories': categories,
        'page_obj': page_obj
    }

    return render(request, 'blueberry/index.html', context)


def blog_details(request, slug):
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    latest_post = Post.objects.all()[:3]
    post = Post.objects.get(slug=slug)
    similar_post = post.tags.similar_objects()[:4]
    comments = post.comments.all()

    if request.method == 'POST':

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment.post = post

            new_comment.save()
            # redirect to a new URL:

            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)




    # if a GET (or any other method) we'll create a blank form
    else:

        comment_form = CommentForm()

    context = {
        'post': post,
        'latest_post': latest_post,
        'categories': categories,
        'similar_post': similar_post,
        'comments': comments
    }

    return render(request, 'blueberry/details.html', context)


def search_blog(request):
    categories = Category.objects.all().annotate(posts_count=Count('posts'))

    latest_post = Post.objects.all()[:3]

    queryset = Post.objects.all()
    query = request.GET.get('q')

    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(sort_description__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
    context = {
        'queryset': queryset,
        'latest_post': latest_post,
        'categories': categories,
        'query': query

    }
    print(context)
    return render(request, 'blueberry/search.html', context)


# def search_blog(request):
#     search_keyword = request.get['q']
#     if search_keyword:
#         post = Post.objects.filter(title__contains=search_keyword)
#         print( "zahid", post, "fardin")
#         return render(request, 'blueberry/search.html')


def category(request, category_slug=None):
    category = None
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    posts = Post.objects.all()
    latest_post = Post.objects.all()[:3]
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'latest_post': latest_post,
        'category': category,
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'blueberry/category.html', context)
