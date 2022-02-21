from django.urls import path

from  .import views

from .views import item_list,Details, Homeview, ItemDetailView, add_to_cart, remove_from_cart

app_name = 'Estore'

urlpatterns = [
    path('',Homeview.as_view(), name = 'index'),
    path('item_list/', views.item_list, name = 'item_list'),
    path('Product/<slug>/', views.ItemDetailView.as_view(), name ='Product'),
    path('Details/', views.Details, name = 'Details'),
    path('add_to_cart/<slug>/', views.add_to_cart, name = 'add_to_cart'),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name = 'remove_from_cart'),

]