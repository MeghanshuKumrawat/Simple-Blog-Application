from django import forms
from django.contrib.auth.models import User
from .models import Blog, Comment, Tags

class Blog_Creation_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-4"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control mb-4"}))
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={"class":"form-check-input mb-2"}), queryset=Tags.objects.all())
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags']
        

class Comment_Form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-4", "rows":3}))
    class Meta:
        model = Comment
        fields = ['content']