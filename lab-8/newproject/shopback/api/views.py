from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Product, Category
# Create your views here.

def products_list(request):
    products = Product.objects.all()
    product_json = [product.to_json() for product in products]
    return JsonResponse(product_json)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id = product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(product.to_json())

def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(category.to_json())

def product_category(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)



