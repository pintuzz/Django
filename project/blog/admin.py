from django.contrib import admin
from .models import Post,Author,Categories

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Categories)
