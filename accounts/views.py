from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.db.models import Count
from django.contrib import messages
from .forms import User_Creation_Form, User_Change_Form, Login_Form
from blogs.models import Tags, Blog

def profile(request):
    tags = Tags.objects.all()
    popular_blog = Blog.objects.annotate(ncomment=Count('comment')).order_by('-ncomment').first()
    form = User_Change_Form(request.POST or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, "Your profile has been updated successfully!")
        return redirect('profile-view')
    context = {'form':form, 'tags':tags, 'popular_blog':popular_blog}
    return render(request, 'profile.html', context)

def sign_up(request):
    tags = Tags.objects.all()
    form = User_Creation_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.info(request, "Your new profile has been created successfully!")
        return redirect('sign-in-view')
    context = {'form':form, 'tags':tags}
    return render(request, 'sign_up.html', context)

def sign_in(request):
    tags = Tags.objects.all()
    form = Login_Form()
    if request.method == 'POST':
        form = Login_Form(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.info(request, "Welcome back " + request.user.username + "!")
            return redirect('profile-view')
    context = {'form':form, 'tags':tags}
    return render(request, 'sign_in.html', context)

def sign_out(request):
    logout(request)
    return redirect('sign-in-view')