from django.contrib import admin
from . models import Article, Commande, Panier, UserModel

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom_produit', 'prix', 'description','photo', 'date_ajout')
    
class CommandAdmin(admin.ModelAdmin):
     list_display = ('client', 'date_started', 'date_ended', 'validated')   
    
    
class PanierAdmin(admin.ModelAdmin):
    list_display = ('client','article', 'quantite', 'ordered')
    
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commande, CommandAdmin)
admin.site.register(Panier, PanierAdmin)
admin.site.register(UserModel)


    

