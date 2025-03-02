from django.contrib import admin
from .models import Post , PostFile


class PostFileAdmin(admin.TabularInline):
    model = PostFile
    fields = ('file',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ('title',)
    inlines = (PostFileAdmin,)
