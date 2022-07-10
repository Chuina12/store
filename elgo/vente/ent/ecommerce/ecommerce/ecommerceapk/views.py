from email import message
from hashlib import new
import re
from wsgiref import validate
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . form import UserForm
from django.views.generic import CreateView, ListView, DetailView,DeleteView, UpdateView
from . models import Article, Commande, Panier

def index(request):
    return render(request, 'user/index.html')


def log(request):
    return render(request, 'user/login.html')

  
def loguser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'connexion reussie !')
            return redirect('account')
        else:
            messages.error(request, 'echec de connexion')
            
    return render(request, 'user/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'your account has been created')
    else:
        messages.error(request, form.errors)
    return render(request, 'user/register.html', {'form':form})

def blog(request):
    return render(request, 'user/blog.html')




def outfuc(request):
    logout(request)
    return redirect('index') 

class ecommerceapkListView(ListView):
    model = Article
    template_name = 'user/productlist.html'
    def get_queryset(self):
        return super().get_queryset()
        
    




def productaccount(request):
    produit = Article.objects.all() 
    
    qs = Commande.objects.filter(client=request.user, validated=False)
    qte = 0
    if qs.exists():
        total_produit = qs.first().panier.all()
        qte = len(total_produit)
    
    return render(request, 'user/account.html', {'produit':produit, 'number':qte})


class ecommerceDetailView(DetailView):
    model = Article
    template_name = 'user/detail.html'
    
    
@login_required()    
def add_item_to_card(request, pk):
    article = get_object_or_404(Article, pk=pk)
    produit, created = Panier.objects.get_or_create(article=article, client=request.user, ordered=False)
   
    print(produit)
    order_qs = Commande.objects.filter(client=request.user, validated=False)
    
    if order_qs.exists():
        qs = order_qs.first()
        if produit in qs.panier.all():
            new_quantite =  produit.quantite + 1
            produit.quantite = new_quantite
            produit.save()
            messages.info(request, 'quantite produit augmente avec success!!')
    else:
        order_qs = Commande.objects.create(client=request.user, validated=False)
        order_qs.panier.add(produit)
        messages.success(request, 'Produit ajoute avec success!')
    return redirect('account')        
        

def list_card(request, pk):
    card_list = get_object_or_404(Panier, pk=pk)