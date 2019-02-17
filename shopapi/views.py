from django.views.generic import TemplateView, ListView, FormView, View
from .models import Product, ProductOrder, ProductType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProductOrderForm
from django.shortcuts import get_object_or_404




class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class HomePageView(TemplateView):
    template_name = 'shopapi/home.html'


class ProductPageView(ListView):
    template_name = 'shopapi/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return product list."""
        name = self.request.GET.get('name')
        product_type_id = self.request.GET.get('product_type_id')
        gs = Product.objects.filter(available=True)
        if name:
            gs = gs.filter(name__icontains=name)
        if product_type_id:
            gs = gs.filter(product_type_id=product_type_id)
        return gs.order_by('-created_at')[:25]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['product_types'] = ProductType.objects.all()
        return data


class ProductBuyPageView(FormView):
    model = ProductOrder
    template_name = 'shopapi/buy_product.html'
    form_class = ProductOrderForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        ProductOrder.objects.create(
                amount=form.cleaned_data['amount'],
                user_name=form.cleaned_data['user_name'],
                user_middle_name=form.cleaned_data['user_middle_name'],
                user_surname=form.cleaned_data['user_surname'],
                user_email=form.cleaned_data['user_email'],
                phone_number=form.cleaned_data['phone_number'],
                callback=form.cleaned_data['callback'],
                payment_type=form.cleaned_data['payment_type'],
                shipping_type=form.cleaned_data['shipping_type'],
                product_id=self.kwargs['pk']
        )
        # here we can send a massage to user regarding his order (SMS for example)
        return super(ProductBuyPageView, self).form_valid(form)
