from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from .models import Blog, Tags, Comment
from .forms import Blog_Creation_Form, Comment_Form

# def get_popular_blog(user):
#     blogs = Blog.objects.filter(user=user)


def index(request):
    blogs = Blog.objects.filter(title__icontains= request.GET.get('search', '')).order_by('timestamp')
    popular_blog = Blog.objects.annotate(ncomment=Count('comment')).order_by('-ncomment').first()
    tags = Tags.objects.all()
    context = {'blogs':blogs, 'tags':tags, 'popular_blog':popular_blog}
    return render(request, 'index.html', context)

def your_blogs(request):
    blogs = Blog.objects.filter(user=request.user)
    tags = Tags.objects.all()
    context = {'blogs':blogs, 'tags':tags}
    return render(request, 'your_blogs.html', context)

def category_blogs(request, tag):
    tag = get_object_or_404(Tags, name=tag)
    blogs = Blog.objects.filter(tags__name=tag)
    tags = Tags.objects.all()
    popular_blog = Blog.objects.annotate(ncomment=Count('comment')).order_by('-ncomment').first()
    context = {'tag':tag, 'blogs':blogs, 'tags':tags, 'popular_blog':popular_blog}
    return render(request, 'category_blogs.html', context)

def single_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog)
    popular_blog = Blog.objects.annotate(ncomment=Count('comment')).order_by('-ncomment').first()
    tags = Tags.objects.all()
    print('----------', popular_blog)
    form = Comment_Form(request.POST or None)
    if request.POST and form.is_valid() and request.user.is_authenticated:
        form = form.save(commit=False)
        form.user = request.user
        form.blog = blog
        form.save()
        return redirect('single-blog-view', pk=pk)
    context = {'blog':blog, 'comments':comments, 'form':form, 'popular_blog':popular_blog, 'tags':tags}
    return render(request, 'single_blog.html', context)

def create_blog(request):
    form = Blog_Creation_Form(request.POST or None, request.FILES or None)
    tags = Tags.objects.all()
    if request.POST and form.is_valid():
        form_ins = form.save(commit=False)
        form_ins.user = request.user
        form_ins.save()
        form.save_m2m()
        messages.info(request, "New blog has been created successfully!")
        return redirect('single-blog-view', pk=form_ins.pk)
    context = {'flag':True, 'form':form, 'tags':tags}
    return render(request, 'create_blog.html', context)

def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = Blog_Creation_Form(instance=blog)
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = Blog_Creation_Form(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.info(request, "Your blog has been updated successfully!")
            return redirect('single-blog-view', pk=blog.pk)
    context = {'flag':False, 'form':form, 'tags':tags}
    return render(request, 'create_blog.html', context)

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    messages.info(request, "Your blog has been deleted successfully!")
    return redirect('your-blogs-view')