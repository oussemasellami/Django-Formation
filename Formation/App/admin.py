from django.contrib import admin
from App.models import *
# Register your models here.

class LesMembres(admin.TabularInline): #tableau cote affichage
    model=MemberShipinProject
    extra=0
@admin.register(etudiant)
class SearchEtudiant(admin.ModelAdmin):
    search_fields=['nom']

#annotation
@admin.register(projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display=('nom_projet','duree_projet','etat','temps_alloue','createur','suprviseur')
    #list_display=('nom','prenom','email','groupe')
    fieldsets=(
        ('A propos',{'fields':('nom_projet','etat')}),
        ('Duree',{'fields':('duree_projet','temps_alloue')}),
        (None,{'fields':('createur','suprviseur')})
    )
    inlines = (LesMembres,)
    autocomplete_fields=['createur']
    list_per_page=1
    list_filter=('etat','createur')
#admin.site.register(etudiant)
admin.site.register(coach)
#admin.site.register(projet,ProjetAdmin)