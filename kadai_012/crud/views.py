from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class TopView(TemplateView):
    template_name =  "crud/top.html"

class ProductListView(ListView):
    model = Product
    template_name = "crud/product_list.html"
    context_object_name = "products"
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"
    context_object_name = "product"