from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('products', views.ProductPageView.as_view(), name='products'),
    path('buy_product/<int:pk>', views.ProductBuyPageView.as_view(), name='buy_product'),
]
