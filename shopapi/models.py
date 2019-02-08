from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


class ShippingType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


class Product(models.Model):
    NEW = 'NEW'
    REFURBISHED = 'REFURBISHED'
    REVALUATED = 'REVALUATED'
    STATE_CHOICES = (
        (NEW, 'new'),
        (REFURBISHED, 'refurbished'),
        (REVALUATED, 'revaluated')
    )

    name = models.CharField(max_length=250, null=False, blank=False)  # обовязкове поле null=False, blank=False
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    available = models.BooleanField(default=False, null=False, blank=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=255, null=False, blank=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Name: {self.name}; Price: {self.price}'


class ProductOrder(models.Model):
    NEW = 'NEW'
    PROCESSING = 'PROCESSING'
    REJECTED = 'REJECTED'
    CONFIRMED = 'CONFIRMED'
    DONE = 'DONE'
    STATE_CHOICES = (
        (NEW, 'new'),
        (PROCESSING, 'processing'),
        (REJECTED, 'rejected'),
        (CONFIRMED, 'confirmed'),
        (DONE, 'done')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATE_CHOICES, max_length=255, null=False, blank=False)
    amount = models.IntegerField(default=1)
    callback = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    user_middle_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    shipping_type = models.ForeignKey(ShippingType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'User_name: {self.user_name}; User_surname: {self.user_surname};' \
               f' User_email: {self.user_email}; Status: {self.status}'



