from django import forms
from .models import ProductOrder


max_order_amount = 10


class ProductOrderForm(forms.ModelForm):
    amount = forms.IntegerField(max_value=max_order_amount)
    user_name = forms.CharField(max_length=255, required=False)
    user_middle_name = forms.CharField(max_length=255, required=False)
    user_surname = forms.CharField(max_length=255, required=False)
    user_email = forms.EmailField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=12, required=True)

    class Meta:
        model = ProductOrder
        fields = ['user_name', 'user_middle_name', 'user_surname', 'user_email', 'callback', 'amount',
                  'payment_type', 'shipping_type']

