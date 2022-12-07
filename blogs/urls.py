from django.urls import path
from .views import index, your_blogs, category_blogs, single_blog, create_blog, edit_blog, delete_blog

urlpatterns = [
    path('', index, name='index-view'),
    path('your-blogs/', your_blogs, name='your-blogs-view'),
    path('category-blogs/<tag>/', category_blogs, name='category-blogs-view'),
    path('blog/<int:pk>/', single_blog, name='single-blog-view'),
    path('create-blog/', create_blog, name='create-blog-view'),
    path('edit-blog/<int:pk>/', edit_blog, name='edit-blog-view'),
    path('delete-blog/<int:pk>/', delete_blog, name='delete-blog-view'),
]
