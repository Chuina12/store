from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.loguser, name='login'),
    path('register', views.register, name='register'),
    path('blog', views.blog, name='blog'),
   
    path('logout', views.outfuc, name='logout'),
    path('productlist', views.ecommerceapkListView.as_view(), name='productlist'),
   # path('list', views.list, name='list'),
    path('account', views.productaccount, name='account'),
    path('detail/<int:pk>', views.ecommerceDetailView.as_view(), name='detail'),
    path('add/<int:pk>', views.add_item_to_card, name='add')
]

