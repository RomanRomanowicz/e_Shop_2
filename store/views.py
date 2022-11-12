from django.shortcuts import render
from django.views.generic import ListView, DetailView

from store.models.products import Products


class HomePageView(ListView):
    model = Products
    # queryset = Products.objects.filter(available=False)
    context_object_name = 'home'
    template_name = 'store/base.html'


class ShopProductListView(ListView):
    model = Products
    # queryset = Products.objects.filter(available=True)
    context_object_name = 'shop'
    template_name = 'store/shop.html'


class ProductDetailView(DetailView):
    model = Products
    slug_field = 'slug'
    context_object_name = 'product_detail'
    template_name = 'store/product_detail.html'