from django.contrib import admin
from .models import Blog, Tags, Comment


admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Comment)
