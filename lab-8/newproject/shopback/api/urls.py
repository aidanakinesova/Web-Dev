from django.urls import path
from api.views import products_list, product_detail, category_detail, categories_list

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product.id>/', product_detail),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_detail),
]