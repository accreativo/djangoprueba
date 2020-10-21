
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from autores.models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """     """
    list_display = ('pk', 'user', 'website', 'telefono', 'foto')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'telefono', 'foto')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'telefono')
    list_filter = ('creado', 'modificado')

    fieldsets = (
        ('Autor', {
            'fields': (
                'user', 'foto',
            ),
        }),
        ('ExtraInfo', {
            'fields': (
                ('website', 'telefono'),
            ),
        }),
        ('Meta Data', {
            'fields': (
                ('creado', 'modificado'),
            ),
        })                
    )

    readonly_fields = ('creado', 'modificado')
    
class AutorInline(admin.StackedInline):
    model = Autor
    can_delete = False
    verbose_name_plural = 'autors'

class UserAdmin(BaseUserAdmin):

    inlines = (AutorInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)