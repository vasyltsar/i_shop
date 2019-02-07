from shopapi.models import Product, ProductType
from django.contrib import admin

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ('name', 'description', 'price', 'available', 'state', 'product_type')

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
