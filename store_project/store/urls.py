from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name = 'product_list_url'),
    path('cats/', cat_list, name = 'cat_list_url'),
    path('product/<int:pk>/', product_detail, name = 'product_detail_url'),
    path('cat/<int:pk>/', cat_detail, name = 'cat_detail_url'),
    path('save_order', save_order, name = 'product_detail_url'),
]
