from django.views.generic import TemplateView, ListView
from .models import Product



class HomePageView(TemplateView):
    template_name = 'home.html'


class ProductPageView(ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return product list."""
        return Product.objects.filter(available=True).order_by('-created_at')[:25]

    def get_context_data(self, *args, **kwargs):
        context = super(ProductPageView, self).get_context_data(*args, **kwargs)
        context['books'] = ['blabla']
        return context



