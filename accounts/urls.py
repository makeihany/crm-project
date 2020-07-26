from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/', views.products, name='products'),
    path('customers/<int:pk_id>', views.customers, name='customers'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<int:pk_id>', views.updateOrder, name='update_order'),

]
