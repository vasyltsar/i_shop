from django.views.generic import TemplateView, ListView, CreateView, View
from .models import Product, ProductOrder
from django.contrib.auth.mixins import LoginRequiredMixin


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class HomePageView(TemplateView):
    template_name = 'shopapi/home.html'


class ProductPageView(ListView):
    template_name = 'shopapi/product_list.html'
    context_object_name = 'products'


class ProductBuyPageView(CreateView):
    template_name = 'shopapi/buy_product.html'
    http_method_names = ['post']
    model = ProductOrder

    def get_queryset(self):
        """Return product list."""
        return Product.objects.filter(available=True).order_by('-created_at')[:25]

