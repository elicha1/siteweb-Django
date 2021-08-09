from django.contrib import admin

from .models import utilisateurs,chargehoraire,annonce



class ProjectAdmin(admin.ModelAdmin):
    list_display=('full_name','departement')
    search_fields = ('full_name',)
class ProjectAdmin1(admin.ModelAdmin):
    list_display = ('user', 'nbrheures','module','matiere','cc','departement')
    search_fields = ('user__full_name',)
class ProjectAdmin2(admin.ModelAdmin):
    list_display=('titre','date')


admin.site.register(utilisateurs, ProjectAdmin)

admin.site.register(chargehoraire, ProjectAdmin1)

admin.site.register(annonce,ProjectAdmin2)


# Register your models here.
