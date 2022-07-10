from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# User = settings.AUTH_USER_MODEL

class UserModel(AbstractUser):
    numero = models.CharField(max_length=18)
    class type(models.TextChoices):
        Yaounde = 'Yaounde', 'YAOUNDE'
        douala = 'Douala', 'DOUALA'
    ville = models.CharField(max_length=50, choices=type.choices, default=type.douala)
    
    
class Article(models.Model):
    nom_produit = models.CharField(max_length=50)
    prix = models.IntegerField()
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='images')
    date_ajout= models.DateTimeField()
    
    class Meta:
        verbose_name = ('Article')
        verbose_name_plural = ('Article') 
        
    def __str__(self):
        return self.nom_produit
     
     
class Panier(models.Model):
    client = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)   
    
    @property               
    def get_price(self):
        return self.quantite * self.article.prix     
            
    def __str__(self):
        return f"{self.client.username}-{self.article.nom_produit}"
    
    
class Commande(models.Model):
    client = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    panier = models.ManyToManyField(Panier, related_name='order')
    date_started = models.DateField(auto_now_add=True)
    date_ended  = models.DateField(null=True, blank=True)
    validated = models.BooleanField(default=False)
   
    
    
   
    class Meta:
        verbose_name=('Commande')
        verbose_name_plural=('Commandes')
    
    @property
    def get_total_price(self):
        total = 0
        for article in self.panier.all():
            total += article.get_price
        if self.client.ville == 'Douala':    
            return total + 1000
        if self.client.ville == 'Yaounde':
            return total + 2000
        return total
  
    
    def __str__(self):
        return f"{self.client.username}-{self.date_ended}-{self.get_total_price}"
    
        
    
        
