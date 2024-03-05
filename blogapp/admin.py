from django.contrib import admin
from .models import Blog
# Register your models here.

# username=blog 
# email=blog123@gmail.com 
# password=blog123

class BlogAdmin(admin.ModelAdmin):
    list_display=("name","blog_name","description")
admin.site.register(Blog, BlogAdmin)