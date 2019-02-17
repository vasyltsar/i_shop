from shopapi.models import Product, ProductType, ProductOrder, ShippingType, PaymentType
from django.contrib import admin


class PaymentTypeAdmin(admin.ModelAdmin):
    model = PaymentType
    fields = ('name',)


class ShippingTypeAdmin(admin.ModelAdmin):
    model = ShippingType
    fields = ('name',)


class ProductOrderAdmin(admin.ModelAdmin):
    model = ProductOrder
    fields = ('phone_number', 'user_name', 'user_surname', 'user_middle_name',
              'user_email', 'callback', 'amount', 'status')
    readonly_fields = ('phone_number', 'user_name', 'user_surname', 'user_middle_name',
                       'user_email', 'callback', 'amount')
    list_display = ('phone_number', 'user_name', 'user_surname', 'user_middle_name',
                    'user_email', 'callback', 'amount', 'status')
    list_filter = ('status', )


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ('name', 'description', 'price', 'available', 'state', 'product_type')
    list_filter = ('product_type',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == Product:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.created_by = request.user
                instance.save()
        else:
            formset.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(ShippingType, ShippingTypeAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)

