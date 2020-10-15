from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ['author', 'posts'[:10]]
    pass