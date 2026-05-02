from django.contrib import admin

from .models import Post

# Register your models here.

admin.site.register(Post)
#Modern version
#@admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_date', 'published_date')
#     list_filter = ('created_date', 'published_date')
#     search_fields = ('title', 'text')