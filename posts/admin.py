
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from autores.models import Autor
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """     """
    list_display = ('pk', 'autor',)
    list_display_links = ('pk', 'autor')
    list_filter = ('creado', 'modificado')
