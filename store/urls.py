from django.urls import path, re_path
from store.views import *
from . import views

app_name = 'store'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopProductListView.as_view(), name='shop'),
    path('shop/<int:id>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('shop/<slug:category_slug>/', HomePageView.as_view(), name='category_list'),
    path('shop/<int:id>/<slug:category_slug>/', ShopProductListView.as_view(), name='shop_list'),
]